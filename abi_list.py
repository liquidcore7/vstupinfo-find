from bs4 import BeautifulSoup

class Azubi:
    def __init__(self, pos, name, prio, points):
        self.position = str(pos)
        self.name = str(name)
        self.priority = str(prio)
        self.average = str(points)
    def to_string(self):
        return self.position.rjust(4) + self.name.rjust(25) + '\t' + self.average.rjust(6) + self.priority.rjust(2)

def abi_list(fac_html):
    parser = BeautifulSoup(fac_html, 'html.parser')
    az_rating = []
    abi_table = parser.find_all('tbody')
    for varia in abi_table:
        for stud in varia.find_all('tr'):
            row = [x.string for x in stud.find_all('td')]
            if len(row) >= 4:
                az_rating.append(Azubi(row[0], row[1], row[2], row[3]))
    return az_rating


if __name__ == '__main__':
    import requests
    html_code = requests.get('http://vstup.info/2017/244/i2017i244p417581.html').content.decode('utf-8')
    lst = abi_list(html_code)
    for abi in lst:
        print(abi.to_string())
    
