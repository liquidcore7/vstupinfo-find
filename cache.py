import requests
import extr_unis as eu
import extr_facs as ef
import abi_list as al


all_unis = ['http://vstup.info/2017/i2017i97.html', 'http://vstup.info/2017/i2017i244.html', 'http://vstup.info/2017/i2017i121.html', 'http://vstup.info/2017/i2017i282.html', 'http://vstup.info/2017/i2017i41.html', 'http://vstup.info/2017/i2017i174.html', 'http://vstup.info/2017/i2017i79.html']
# you can add an url to this list. however, there is no guarantee it will work.

db = open('dbase.txt', 'w', 1, 'utf-8')

for uni in all_unis:
    uni_facs, uni_name = ef.extr_faculties(requests.get(uni).content.decode('utf-8'))
    for f in uni_facs:
        db.write(uni_name + '\n' + f[0] + '\n')
        fac = al.abi_list(requests.get(f[1]).content.decode('utf-8'))
        for stud in fac:
            db.write( stud.to_string() + '\n' )
        db.write('\n')
db.close()
