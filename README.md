# Offline checker that detect an IP address is for Iran or no.
A Python script to detect IP addresses related to Iran without any external or third party API.
This repository use a comprehensive list of public IP addresses assigned to Iran.
I have used the ip list from the following repository:
https://github.com/Ramtiiin/iran-ip

## How its work  

1. the get_network_info method calculate subnet mask and find the network address for the given ip.
example :
```
IP: 193.141.65.115 → Network: 193.141.64.0/23
```
2. The network address searched inside the ip-list.rsc file and return a boolean that indicate the IP is for Iran or not.

## Sample Usage 
```

def is_ip_for_iran(ip):
    # Example usage
    test_ips = [
        "193.141.65.182",  # Should give 193.141.64.0/23
        "192.168.1.1",  # Class C network
        "10.0.0.1"  # Class A network
    ]

    try:
        network = get_network_info(ip)
        print(f"IP: {ip} → Network: {network}")
        is_ip_in_iran = check_in_ip_list(network)
        print(f"Is IP {ip} for IRAN: {is_ip_in_iran}")
        return is_ip_in_iran
    except ValueError as e:
        print(f"Error processing {ip}: {e}")
```

## Disclaimer
Please note that the use of public IP addresses listed in this repository is subject to legal regulations and restrictions. It is your responsibility to ensure compliance with applicable laws and regulations when using these IP addresses. The contributors of this repository do not guarantee the accuracy or availability of these IP addresses and are not liable for any consequences arising from their use.

## License
This project is licensed under the MIT License.
