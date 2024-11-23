# developer.cisco.com/site/sandbox
from netmiko import ConnectHandler
csr = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345"

}

net_connect = ConnectHandler(**csr)
output = net_connect.send_command("show ip int brief")
print(output)

net_connect.disconnect()
