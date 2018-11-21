from datetime import *
import locale
locale.setlocale(locale.LC_ALL, "ru")
date = '02.11.2013'

date_total = datetime.date(datetime.strptime(date, '%d.%m.%Y'))
date_total2 = date_total.strftime('%A %B %Y ' + "года")
print(date_total2)