import requests
import random
import time 

# Pico W IP address and endpoint
PICO_IP = "192.168.100.34"  # Replace with your Pico's IP address
ENDPOINT_SET_LEDS = f"http://{PICO_IP}:5000/set-leds"
ENDPOINT_SET_RAINBOW = f"http://{PICO_IP}:5000/set-rainbow"

# JSON payload with the desired LED color
payload = {
    "color": "#FF5733"  # Example: Bright orange
}

rainbow_payload = {
    "duration": 20, 
    "speed": 0.01,
    "brightness": 100
}

def generate_random_color():
    """Generate a random hexadecimal color."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def send_request(endpoint, json_payload):

    print(f'Sending request: {json_payload}')

    response = requests.post(endpoint, json=json_payload)
    
    # Print the response
    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response body:", response.text)

try:
    send_request(ENDPOINT_SET_RAINBOW, rainbow_payload)
    time.sleep(1.0)
    send_request(ENDPOINT_SET_LEDS, payload)
    # while True:
    #     # Generate a random color
    #     random_color = generate_random_color()
    #     payload = {"color": random_color}

    #     send_request(payload) 
        
    #     # Wait for 5 seconds before sending the next request
    #     time.sleep(5)
except KeyboardInterrupt:
    print("Stopped sending requests.")
except Exception as e:
    print(f"Failed to connect to Pico W: {e}")