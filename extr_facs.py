from bs4 import BeautifulSoup


def isnum(string):
    for c in string:
        if c > '9' or (c < '0' and c != '.'):
            return False
        return True



def extr_faculties(html_data):
    parser = BeautifulSoup(html_data, 'lxml')
    url_arr = []
    uni_name = parser.find("h3").string
    faclist = parser.find('tbody')
    for fac in faclist.find_all('tr'):
        facname = fac.td.find_all('span')[3].string
        splname = facname.split(' ')
        if isnum(splname[0]):
            del splname[0]
        facname = ' ' + ' '.join(splname)
        faculty = [facname, ]
        for i in fac.find_all('td'):
            if i.find('a') is not None:
                faculty.append("http://vstup.info/2017" + i.a.get('href')[1:])
                url_arr.append(faculty)
    return url_arr, uni_name
    
    
if __name__ == '__main__':
    import requests
    html_code = requests.get('http://vstup.info/2017/i2017i282.html').content.decode('utf-8')
    all_fcs, uname = extr_faculties(html_code)
    print(uname)
    for f in all_fcs:
        print(f[0], '\t', f[1])
