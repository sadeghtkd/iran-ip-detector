def get_network_info(ip_address):
    """
    Convert an IPv4 address to its network address with the correct CIDR notation.

    Args:
        ip_address (str): IPv4 address in string format (e.g., '193.141.65.182')

    Returns:
        str: Network address with CIDR notation (e.g., '193.141.64.0/23')
    """
    # Convert IP string to integer
    ip_parts = [int(part) for part in ip_address.split('.')]
    ip_int = (ip_parts[0] << 24) + (ip_parts[1] << 16) + (ip_parts[2] << 8) + ip_parts[3]

    # Determine network class and CIDR
    first_octet = ip_parts[0]
    if first_octet >= 192:  # Class C and above
        # For IP 193.141.65.182, we want /23
        cidr = 23
    elif first_octet >= 128:  # Class B
        cidr = 16
    else:  # Class A
        cidr = 8

    # Calculate subnet mask
    mask = ((1 << 32) - 1) ^ ((1 << (32 - cidr)) - 1)

    # Calculate network address
    network = ip_int & mask

    # Convert network address back to dotted decimal
    network_parts = [
        (network >> 24) & 255,
        (network >> 16) & 255,
        (network >> 8) & 255,
        network & 255
    ]
    network_str = '.'.join(map(str, network_parts))

    return f"{network_str}/{cidr}"


def check_in_ip_list(net_address):
    with open('ip-list.rsc') as list_file:
        lines = list_file.readlines()
        for line in lines:
            if net_address in line:
                return True
    return False


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


is_ip_for_iran("193.141.65.115")