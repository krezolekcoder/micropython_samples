# micropython_samples

Various MicroPython samples mainly for Raspberry Pi Pico boards.

---

## SETUP

To set up the environment and install dependencies, follow these steps:

1. **Update git submodules**:
   ```bash
   git submodule update --init --recursive
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Samples structure

Each sample has its own directory. Current existing samples:

- `ws2812_rest_server`
- `ble`

---

## Uploading sample to board

You can manually upload each file without bash script (Cross platform): 
```bash
./micropython/tools/pyboard --device /dev/ttyUSB1 -f cp samples/ws2812_rest_server/main.py :main.py
./micropython/tools/pyboard --device /dev/ttyUSB1 -f cp samples/ws2812_rest_server/wifi.py :wifi.py
./micropython/tools/pyboard --device /dev/ttyUSB1 -f cp samples/ws2812_rest_server/lib/microdot/microdot.py :microdot.py
...
```

Helper script is provided that automates this on unix based systems 
```bash
./upload_all.sh <SAMPLE_DIR> <BOARD_SERIAL>
```

For example, to upload the `ws2812_rest_server` sample to a board with serial `/dev/ttyUSB1`, use:

```bash
./upload_all.sh samples/ws2812_rest_server /dev/ttyUSB1
```

---

## Running a sample

### WS2812_REST_SERVER

For the **WS2812_REST_SERVER** sample, follow these steps:

1. **Place the `config.py` file inside the `samples/ws2812_rest_server` directory** with your network credentials:

   ```python
   SSID = "MY-SSID"
   PASSWORD = "MY-PASSWORD"
   ```

2. **Upload the sample to the board**:

   ```bash
   ./upload_all.sh samples/ws2812_rest_server /dev/ttyUSB1
   ```

3. **Run the application on the board and open a serial port session**:

   ```bash
   ./micropython/tools/pyboard --device /dev/ttyUSB1 samples/ws2812_rest_server/main.py
   ```

4. Once successfully connected to the WiFi network, you should see a log similar to this:

   ```
   Connected successfully!
   Network details: ('192.168.100.33', '255.255.255.0', '192.168.100.1', '192.168.100.1')
   Starting async server on 0.0.0.0:5000...
   ```

5. You can now send sample **HTML PUT requests** to control the rainbow colors on your LED strip and set a random color at the end. Use the following script to interact with the sample:

   ```bash
   python scripts/ws2812_requests.py
   ```

---

### Additional Resources

- For more details about the `pyboard` tool, refer to the official documentation:  
  [Pyboard Tool Documentation](https://docs.micropython.org/en/latest/reference/pyboard.py.html)

- Or see the source code of the `pyboard` tool:  
  `micropython/tools/pyboard.py`