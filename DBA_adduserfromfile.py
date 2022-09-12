#Author: DavidBAEK

import subprocess,traceback,sys,getpass,string,random
import pandas as pd

#Export en CSV la liste des utilisateurs
filename = "/etc/group"
df = pd.read_csv('userlist.csv', sep=';')

with open(filename, "r") as f:
    for line in f:
        username = line.split(";")[0]
        # group_id = line.split(":")[2]
        # membre_list = line.split(":")[3]

        # n = pd.DataFrame([[
        #     group
        #     , group_id
        #     , membre_list]]
        #     , columns=['group', 'group_id', 'membre_list'])
        # df = df.append(n)
        # df.to_csv('userlist.csv', sep=';', index=False)
    '''/home/username; shell/bin/bash; chgMdpTemp@1stLogin;
    
    root@vmubuntu:/home/adminhba/PycharmProjects/adminsys# python3 adduserfromfile.py userlist
    passwd: password expiry information changed.
    passwd: password expiry information changed.
    root@vmubuntu:/home/adminhba/PycharmProjects/adminsys#
    
  
    '''

    #exécution de la commande useradd via le module subprocess
  # SUID et GUID et Stickybit
def user_add(username, user_dir=None):
    if user_dir:
        cmd = ["sudo", "useradd", "-d", user_dir, "-m", username]
    else:
        cmd = ["sudo", "useradd", username]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    output = output.strip().decode("utf-8")
    error = error.decode("utf-8")
    if p.returncode != 0:
        print(f"E: {error}")
        raise
    return output


try:
    username = "user"
    output = user_add(username)
    print(F"Success. {username} is added")
except:
    traceback.print_exc()
    sys.exit(1)

# Temporary password
temp_pw_len = 10  # new password length

pw_cadidate = string.ascii_letters + string.digits + string.punctuation


temp_pw = ""
for i in range(temp_pw_len):
    temp_pw += random.choice(pw_cadidate) #generate temporary password

print("\nTemporary password", temp_pw)

# en utilisant subprocess.Popen
def input_passwd():
    # mesg = "Password: "
    # print "You are required to change your password immediately (administrator enforced)."
    # old = getpass.getpass("Current %s" % mesg)
    # new = getpass.getpass("New %s" % mesg)
    # re_new = getpass.getpass("Retype New %s" % mesg)
    #
    # if new != re_new:
    #     print "New RandomString does not match."
    #     exit(1)
    #
    # return old, new'''
'# en utilisant passwd --expire user