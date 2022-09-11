# import datetime
#
# today = datetime.datetime.now()
# date_time = today.strftime('%d/%M/%Y,%h:%m:%s')
# print(date_time)

import re
fichier = '/etc/group'
pattern = r'\w*:\w:\d*:\w*'

with open(fichier)