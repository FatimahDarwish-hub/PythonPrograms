#This code helps identify whether an IP address is within a private range, commonly used in local networks, or if it is a public IP address accessible over the internet.


def is_private_ip(ip_address):
    # Split the IP address into its four octets
    octets = ip_address.split('.')
    
    # Convert octets to integers
    octets = [int(octet) for octet in octets]
    
    # Check if the IP address falls within private IP ranges
    if (octets[0] == 10):
        return True
    elif (octets[0] == 172 and 16 <= octets[1] <= 31):
        return True
    elif (octets[0] == 192 and octets[1] == 168):
        return True
    else:
        return False

# Get user input for the IP address
ip_address = input("Please enter an IPv4 address: ")

# Check if the IP address is private or public
if is_private_ip(ip_address):
    print(f"The IP address {ip_address} is a private IP address.")
else:
    print(f"The IP address {ip_address} is a public IP address.")
