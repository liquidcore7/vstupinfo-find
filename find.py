import re, sys, os

pos_pattern = r'^[ \d]{4}'
rm = r'[\n]'
name = sys.argv[1] if len(sys.argv) > 1 else ""

if not os.path.exists('dbase.txt'):
    import cache
    

db = open('dbase.txt', 'r', 1, 'utf-8')
uni, fac = '', ''
print("   #", 'П.І.Б'.rjust(25), '\t', 'Сер. бал, пріоритет'.rjust(6), 'Факультет(ВНЗ)'.rjust(45))
for line in db:
    if len(line) > 0:
        if re.match(pos_pattern, line) is None:
            if line[0] != ' ':
                uni = re.sub(rm, '', line)
            else:
                fac = re.sub(rm, '', line)
        else:
            if name in line:
                print(re.sub(rm, '', line), '\t', "{}({})".format(fac, uni))
                
db.close()
        
    


