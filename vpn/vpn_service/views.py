import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import SignUpForm, UserSiteForm
from .models import Site
from .services import modify_content


@login_required
def proxy_view(request, user_site_name, routes_on_original_site=''):
    method = request.method
    params = request.GET if method == 'GET' else request.POST
    data = request.body if method in ['POST', 'PUT', 'PATCH'] else None
    site = Site.objects.get(user=request.user, name=user_site_name)
    if data:
        site.data_sent += len(request.body)
    site.page_views += 1

    original_url = routes_on_original_site if routes_on_original_site else site.url
    response = requests.request(method, original_url, params=params, data=data)

    site.data_received += len(response.content)
    site.save()

    modified_content = modify_content(response=response, user_site_name=user_site_name)

    proxy_response = HttpResponse(
        str(modified_content),
        content_type=response.headers['content-type'],
        status=response.status_code)
    return proxy_response


@login_required
def home(request):
    user_sites = request.user.sites.all()
    form = UserSiteForm()
    if request.method == 'POST':
        form = UserSiteForm(request.POST)
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.user = request.user
            new_site.save()
            return redirect('profile')
    return render(request, 'base.html', {'user_sites': user_sites, 'form': form})


@login_required
def statistics(request):
    user_sites = request.user.sites.all()
    return render(request, 'statistics.html', {'user_sites': user_sites})


@login_required
def logout_view(request):
    logout(request)
    return redirect('profile')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})