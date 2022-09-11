#identifié les fichiers et les répertoires contenu du HOMEDIR du user
#   else:
#     print('file:   {0}'.format(path))
import os
import shutil
import datetime

dirname = os.getenv('HOME') # get environment HOME_dba

os.mkdir( ’/tmp/files’, '/tmp/archives')
shutil.copy(dirname, '/tmp/files')
path = os.path.join(dirname, basename)
date_mtime = os.path.getmtime('/tmp/archive')
#Déplacer uniquement les fichiers dont la date de dernière modification est supérieur à 2 jours dans /tmp/archive
for basename in os.listdir(dirname):
  pass
if date_mtime > 86400*2:
  shutil.copy(dirname, '/tmp/files')

print(date_mtime)



'''os.path
os.path.getmtime
os.walk

os.path.expanduser("~")
86400s 24h'''