import subprocess
import sys
import getpass

# fonction add user
def add_user():
    # demande à l’utilisateur de saisir le username
    username = input("Enter Username ")

    # demande à l’utilisateur de saisir le password sans echo
    password = getpass.getpass()

    try:
        # exécution de la commande useradd via le module subprocess
        subprocess.run(['useradd', '-p', password, username])
    except:
        print(f"Failed to add user.")
        sys.exit(1)


add_user()
