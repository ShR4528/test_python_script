from netmiko import Netmiko

my_router = Netmiko(ip ='192.168.122.1',
                    username='shamilr',
                    password='qwerty-1789',
                    device_type='cisco_ios')

print(my_router.find_prompt())

show_run = my_router.send_command('show run')

print(show_run)
