import requests

def get_public_ip():
    try:
        # Use a free API service to get the public IP address
        response = requests.get('https://ipinfo.io')
        data = response.json()

        # Extract the IP address from the response
        ip_address = data.get('ip', 'Unknown')

        return ip_address

    except requests.RequestException:
        return 'Unable to retrieve IP address'

if __name__ == "_main_":
    # Ask for permission to access location (in this case, we're getting the public IP address)
    user_input = input("Do you want to get your public IP address? (y/n): ")
    
    if user_input.lower() == 'y':
        ip_address = get_public_ip()
        print(f"Your public IP address is: {ip_address}")
    else:
        print("Permission denied.")