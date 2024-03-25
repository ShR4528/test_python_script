from getpass import getpass

from paramiko import client

hostname = "crs1.test.lab"




username = input('Enter Username:')

if not username:
    username = "admin"
    print(f"No username provided, using default username: {username}")

password = getpass(f"Enter Password of the user {username}:") or 'admin'


ssh_client = client.SSHClient()

ssh_client.connect(hostname=hostname,
                   port=22,
                   username=username,
                   password=password,
                   look_for_keys=False,allow_agent=False)

print('Connected successfully')

divece_access = ssh_client.invoke_shell()

divece_access.send('show run')


output = divece_access.recv(65535)
print(output) 

