__author__ = 'denrico'

import time as t
import shelve

s = shelve.open('my_students', writeback=True)

while True:
    entry = input('Begin scanning or enter q to quit: ')

    if entry in ['q', 'Q']:
        s.close()
        break

    elif entry not in s.keys():
        print('ID not found; scan again.')

    else:
        print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime()))
        s[entry]['attendance'].append(t.time())



