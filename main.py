from time import sleep
from rgbkeypad import RGBKeypad
from rgb import RGB

rgb = RGB()

# define some colours using RGB values
blue = RGB(0,0,255)
red = RGB(255,0,0)
green = RGB(0,255,0)
purple = RGB(255,0,255)
plum = RGB(221,160,221)
yellow = RGB(255,255,0)
cyan = RGB(0,255,255)
orange = RGB(255,128,0)
white = RGB(255,255,255)
black = RGB(0,0,0)

# Set the auto_update to false - we can make changes then update the lights
# we do this because its quicker
keypad = RGBKeypad(auto_update=False)
keypad.brightness = 0.5

NUM_PADS = 16
button_states = keypad.get_keys_pressed

def map(x, in_min, in_max, out_min, out_max):
    # maps the value x between two sets of values and scales the result
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def clear():
    """ Clears the keypad """
    keypad.clear
    
def color(wait:float,fade:str=None, rgb_value:RGB=None):
    """ Sets the rgb value of all keys """
    if fade is None:
        fade = "in"
    if rgb_value is None:
        rgb_value = 0xFF
    if fade == "in":
        for i in range(0,255):
            for x in range(4):
                for y in range(4):
                    key = keypad[x,y]
                    r = rgb_value.red & i
                    g = rgb_value.green & i
                    b = rgb_value.blue & i
                    key.color = (r,g,b)
    
    if fade == "out":
        for i in range(0,255):
            for x in range(4):
                for y in range(4):
                    key = keypad[x,y]
                    r = rgb_value.red - i
                    g = rgb_value.green - i
                    b = rgb_value.blue - i
                    key.color = (r,g,b)

def fade_in_out(color_value:RGB, wait):
    """ fade from one colour to another """
    color(fade="in", rgb_value=color_value, wait=wait)
    color(fade="out", rgb_value=color_value, wait=wait)

def fade_key(color_from:RGB, color_to:RGB, x, y):
    for n in range(0, 100, 2):
        r = int(map(n,0,100,color_from.red, color_to.red))
        g = int(map(n,0,100,color_from.green, color_to.green))
        b = int(map(n,0,100,color_from.blue, color_to.blue))
        
        key = keypad[x,y]
        key.color = (r, g, b)
        if key.is_pressed():
            print("key", x, y, "pressed")
            key.color = (0,255,255)
            keypad.update()       
        keypad.update()

def fade_to(color_from:RGB, color_to:RGB, wait:float):  
    """ fade from one colour to another """  
    for n in range(0, 100, 2):
        r = int(map(n,0,100,color_from.red, color_to.red))
        g = int(map(n,0,100,color_from.green, color_to.green))
        b = int(map(n,0,100,color_from.blue, color_to.blue))
        for x in range (4):
            for y in range(4):
                key = keypad[x,y]
                key.color = (r, g, b)
                if key.is_pressed():
                    print("key", x, y, "pressed")
                    # key.clear()
                    key.color = (0,255,255)
                    keypad.update()       
        keypad.update()
        
clear()
wait = 0.0001


def rainbow():
    fade_to(black, cyan, wait)
    fade_to(cyan, blue, wait)
    fade_to(blue, green, wait)
    fade_to(green, yellow, wait)
    fade_to(yellow, orange, wait)
    fade_to(orange, red, wait)
    fade_to(red, orange, wait)
    fade_to(orange, yellow, wait)
    fade_to(yellow, green, wait)
    fade_to(green, red, wait)
    fade_to(red, purple, wait)
    fade_to(purple, green, wait)
    fade_to(green, blue, wait)
    fade_to(blue, cyan, wait)
    fade_to(cyan, black, wait)

button1 = keypad.get_key(0,3)
button2 = keypad.get_key(0,2)
button3 = keypad.get_key(0,0)
start_button = keypad.get_key(1,2)
end_button = keypad.get_key(3,0)
while not start_button.is_pressed():
    fade_key(black, red,1,2)
    fade_key(red, black,1,2)
    sleep(0.1)

while not end_button.is_pressed():
    if button1.is_pressed():
        fade_to(black, green, wait)
        fade_to(green, black, wait)
    if button2.is_pressed():
        fade_to(black, yellow, wait)
        fade_to(yellow, black, wait)
    if button3.is_pressed():
        rainbow()
    else:
        fade_to(black, red, wait)
        fade_to(red,black, wait)

keypad.clear()
    