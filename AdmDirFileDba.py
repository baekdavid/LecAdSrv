#identifié les fichiers et les répertoires contenu du HOMEDIR du user
import os

dirname = os.getenv('HOME') # get environment HOME_dba
for basename in os.listdir(dirname):
  path = os.path.join(dirname, basename)
  if os.path.isdir(path):
    print('folder: {0}'.format(path))
  else:
    print('file:   {0}'.format(path))
