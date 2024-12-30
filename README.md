# micropython_samples
Various micropython samples mainly for raspberry pi pico boards 

# SETUP : 

git submodule update --init --recursive

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# Samples structure

Each sample has its own directory. 
Current existing samples :
- ws2812_rest_server
- ble

# Uploading sample to board


./upload_all.sh <SAMPLE_DIR> <BOARD_SERIAL> 
f.ex 
./upload_all.sh samples/ws2812_rest_server /dev/ttyUSB1

# Running sample

## WS2812_REST_SERVER

Remember to place config.py file inside samples/ws2812_rest_server directory with your network credentials like:

SSID = "MY-SSID"
PASSWORD = "MY-PASSWORD"

Upload sample:

./upload_all.sh samples/ws2812_rest_server /dev/ttyUSB1

Run application on board and open serial port session

./micropython/tools/pyboard --device /dev/ttyUSB1 samples/ws2812_rest_server/main.py

After succesfull connection to your wifi network you should see log:

Connected successfully!
Network details: ('192.168.100.33', '255.255.255.0', '192.168.100.1', '192.168.100.1')
Starting async server on 0.0.0.0:5000...

Then you can send sample HTML PUT requests that will run rainbow colors on your led strip and put random color at the end

python scripts/ws2812_requests.py