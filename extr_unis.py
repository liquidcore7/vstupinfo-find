from bs4 import BeautifulSoup
    
def university_spawner(html_data):
    parser = BeautifulSoup(html_data, 'html.parser')
    url_arr = []
    for uni in parser.find_all('tr'):
        url_arr.append("http://vstup.info/2017" + uni.a.get('href')[1:])
    return url_arr
    
