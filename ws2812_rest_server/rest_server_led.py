from led_effects import LedEffects
from microdot import Microdot

LED_STRIP_PIN = 0
LED_CNT = 28 

class LedEffectsRESTServer:

    def __init__(self):
        self.leds = LedEffects(LED_STRIP_PIN, LED_CNT)
        self.app = Microdot()
        self.app.route('/set-leds', methods=['POST'])(self.set_leds)
        self.app.route('/set-rainbow', methods=['POST'])(self.set_rainbow)

    def server_run(self):
        self.app.run(debug=True)

    def set_leds(self, request):
        try:
            # Parse JSON payload
            data = request.json

            # Extract color
            color_hex = data.get('color', '#000000')
            red = int(color_hex[1:3], 16)
            green = int(color_hex[3:5], 16)
            blue = int(color_hex[5:7], 16)
            print(f"Set leds request R: {red} G: {green} B:{blue}") 

            self.leds.set_leds((red, green, blue)) 
            
            return {"status": "success", "color": color_hex}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 400

    def set_rainbow(self, request):
        try:
            # Parse JSON payload
            data = request.json
            print(f' Rainbow data : {data}')
            self.leds.rainbow(duration=data['duration'], speed=data['speed'], brightness=data['brightness'])  
            return {"status": "success"}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 400

    def led_samples_test(self):
        print(f'Blink an LED')
        self.leds.blink((255, 0, 0), 5, 1, 100)
        print(f'Fade')
        self.leds.fade((255, 0, 0), 10, 100)
        print(f'Rainbow')
        self.leds.rainbow(60, 0.01, 100, False)
        self.leds.wave((0, 255, 0), 20, 0.05, 100, reverse=False)