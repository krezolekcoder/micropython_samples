import neopixel
from machine import Pin
import time 
import math

def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB.
    h: Hue (0-1, represents angle on color wheel)
    s: Saturation (0-1, 0 is grayscale, 1 is full color)
    v: Value/Brightness (0-1, 0 is dark, 1 is bright)
    Returns: Tuple (r, g, b) in range 0-255
    """
    i = int(h * 6)  # Sector 0 to 5
    f = (h * 6) - i  # Fractional part of h
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6

    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q

    # Convert to 0-255 range
    return int(r * 255), int(g * 255), int(b * 255)

# Color wheel helper for rainbow effect
def wheel(pos):
    """Generate color based on wheel position."""
    pos = pos % 256
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

def apply_brightness(color, brightness):
    """Adjust brightness of an RGB color. Brightness value in percentage"""
    r, g, b = color
    factor = brightness / 100
    return int(r * factor), int(g * factor), int(b * factor)


class LedEffects():
    def __init__(self, led_strip_pin, led_cnt):
        self.led_strip = neopixel.NeoPixel(Pin(led_strip_pin), led_cnt)
        self.led_cnt = led_cnt

    def set_leds(self, color_hex, brightness=100):
        rgb = apply_brightness(color_hex, brightness)
        # Set all LEDs to the specified color
        self.led_strip.fill(rgb)
        self.led_strip.write()

    def blink(self, color, duration, speed, brightness):
        """Blink the LEDs with a specific color."""
        rgb = apply_brightness(color, brightness)
        end_time = time.time() + duration

        print(f'LedEffects : Blink {rgb} {end_time}')
        while time.time() < end_time:
            # Turn LEDs on
            print(f' Blink on ')
            self.led_strip.fill(rgb)
            self.led_strip.write()
            time.sleep(speed)

            # Turn LEDs off
            print(f' Blink OFF')
            self.led_strip.fill((0,0,0))
            self.led_strip.write()
            time.sleep(speed)

    def fade(self, color, duration, brightness):
        """Fade in and out with a specific color."""
        start_time = time.time()
        while time.time() - start_time < duration:
            # Fade in
            for b in range(0, brightness + 1, 5):  # Step 5 for smoother fade
                adjusted_rgb = apply_brightness(color, b)
                self.led_strip.fill(adjusted_rgb)
                self.led_strip.write()
                time.sleep(0.05)
            # Fade out
            for b in range(brightness, -1, -5):
                adjusted_rgb = apply_brightness(color, b)
                self.led_strip.fill(adjusted_rgb)
                self.led_strip.write()
                time.sleep(0.05)

    def rainbow(self, duration, speed, brightness, reverse=False):
        """Create a rainbow cycling effect."""
        start_time = time.time()
        step = 1 if not reverse else -1
        while time.time() - start_time < duration:
            for j in range(256):  # Full color cycle
                for i in range(self.led_cnt):
                    pixel_index = (i * 256 // self.led_cnt + j) & 255
                    self.led_strip[i] = apply_brightness(wheel(pixel_index), brightness)
                self.led_strip.write()
                time.sleep(speed)

    def color_cycle(self, duration, speed=0.01, brightness=100, direction=1):
        """
        Cycle through colors using HSV.
        duration: Duration of animation
        brightness:
        speed: Time delay between color updates in seconds
        direction: clockwise or anticlockwise colors movement:
            1 : clockwise
            else : anticlockwise
        """

        hue = 0  # Start hue
        start_time = time.time()
        hue_increment = 0.001 if direction else -0.001

        while time.time() - start_time < duration:
            rgb = apply_brightness(hsv_to_rgb(hue, 1, 1), brightness)
            self.led_strip.fill(rgb) 
            self.led_strip.write()  # Update the strip
            hue += hue_increment  # Increment hue
            if hue > 1:
                hue -= 1  # Wrap around if hue exceeds 1
            time.sleep(speed)

    def wave(self, color, duration, speed, brightness, reverse):
        """Create a wave animation across the LEDs."""
        rgb = apply_brightness(color, brightness)
        start_time = time.time()
        direction = 1 if not reverse else -1
        while time.time() - start_time < duration:
            for offset in range(self.led_cnt):
                for i in range(self.led_cnt):
                    # Create a wave pattern
                    intensity = (math.sin((i + offset * direction) * math.pi / self.led_cnt) + 1) / 2
                    adjusted_rgb = apply_brightness(rgb, int(intensity * brightness))
                    self.led_strip[i] = adjusted_rgb
                self.led_strip.write()
                time.sleep(speed)
            if direction == -1:
                direction = 1
            else:
                direction = -1

