from netmiko import ConnectHandler
import json

def configure_routers(ip, configs):
    print(f"\n Connecting to {ip}")

    ssh_info = {
            'device_type': 'cisco_ios',
            'username': 'ciscor',
            'ip': ip,
            'secret': 'cisco',
            'password': 'cisco'
        }

    try:
        #try connect to a router
        net_connect = ConnectHandler(**ssh_info)
        net_connect.enable()
        print("Connect successfully")

        #send configuration in configuration mode commands.
        print("\n Sending interface configuration")
        output = net_connect.send_config_set(configs["interface_configs"])
        print(output)

        # show ip interface brief in 
        print("\nShow ip interface brief")
        output = net_connect.send_command("show ip interface brief")
        print(output)

        #send ospf configuration in configuration mode commands.
        print("\nSending OSPF configuration")
        output = net_connect.send_config_set(configs["ospf_configs"])
        print(output)

        #show ip route
        print("\nShow ip route")
        output = net_connect.send_command("show ip route")

        #save config
        print("\nSave configuration")
        output = net_connect.save_config()

        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to {ip}")
        print(e)

def main():
    with open(routers.json) as file:
        routers = json.load(file)
        
    for ip, configs in routers.items():
         configure_routers(ip, configs)
    

if __name__ == "__main__":
     main()