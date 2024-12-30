import network
import time
import config

def connect_to_network():

    # Initialize the Wi-Fi interface
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("Connecting to network...")
    wlan.connect(config.SSID, config.PASSWORD)

    # Wait for connection
    max_retries = 10
    retries = 0

    while not wlan.isconnected() and retries < max_retries:
        print("Waiting for connection...")
        time.sleep(1)
        retries += 1

    if wlan.isconnected():
        print("Connected successfully!")
        print("Network details:", wlan.ifconfig())
    else:
        print("Failed to connect to the network.")