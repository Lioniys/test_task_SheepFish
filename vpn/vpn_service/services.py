from bs4 import BeautifulSoup


def modify_content(*, response, user_site_name):
    soup = BeautifulSoup(response.content, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        a_tag['href'] = f"http://localhost:8000/proxyy/{user_site_name}/{a_tag['href']}"
    return soup
