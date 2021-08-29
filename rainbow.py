from time import sleep
from rgbkeypad import RGBKeypad
from rgb import RGB

rgb = RGB()

keypad = RGBKeypad(auto_update=False)
keypad.brightness = 0.5

NUM_PADS = 16
button_states = keypad.get_keys_pressed

def map(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def clear():
    keypad.clear
    
def color(wait:float,fade:str=None, rgb_value:RGB=None):
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
        # sleep(wait)
    
    if fade == "out":
        for i in range(0,255):
            for x in range(4):
                for y in range(4):
                    key = keypad[x,y]
                    r = rgb_value.red - i
                    g = rgb_value.green - i
                    b = rgb_value.blue - i
                    key.color = (r,g,b)
        # sleep(wait)
        # for i in range(0,255):
        #     for pad in range (NUM_PADS):
        #         r = rgb_value.red - i
        #         g = rgb_value.green - i
        #         b = rgb_value.blue - i
        #         if r <1: r = 0
        #         if g <1: g = 0
        #         if b <1: b = 0
        #         keypad.illuminate(pad, r, g, b)
        #         keypad.update()
        # sleep(wait)

def fade_in_out(color_value:RGB, wait):
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
            # print("key", x, y, "pressed")
            # key.clear()
            key.color = (0,255,255)
            keypad.update()
            # return
        # sleep(wait)        
        keypad.update()

def fade_to(color_from:RGB, color_to:RGB, wait:float, name):
    # print(name)
    
    for n in range(0, 100, 2):
        r = int(map(n,0,100,color_from.red, color_to.red))
        g = int(map(n,0,100,color_from.green, color_to.green))
        b = int(map(n,0,100,color_from.blue, color_to.blue))
        for x in range (4):
            for y in range(4):
                key = keypad[x,y]
                key.color = (r, g, b)
                if key.is_pressed():
                    # print("key", x, y, "pressed")
                    # key.clear()
                    key.color = (0,255,255)
                    keypad.update()
                    # return
        # sleep(wait)        
        keypad.update()
        
clear()
wait = 0.0001
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

def rainbow():
    fade_to(black, cyan, wait,name="cyan blue")
    fade_to(cyan, blue, wait,name="cyan blue")
    fade_to(blue, green, wait, name="blue green")
    fade_to(green, yellow, wait,name="green yellow")
    fade_to(yellow, orange, wait, name="yellow orange")
    fade_to(orange, red, wait, name="orange red")
    fade_to(red, orange, wait, name="red orange")
    fade_to(orange, yellow, wait, name="orange yellow")
    fade_to(yellow, green, wait,name="yellow green")
    fade_to(green, red, wait,name="green, red")
    fade_to(red, purple, wait,name="green, red")
    fade_to(purple, green, wait,name="green, red")
    fade_to(green, blue, wait, name="green blue")
    fade_to(blue, cyan, wait, name="blue, cyan")
    fade_to(cyan, black, wait, name="blue, cyan")

button1 = keypad.get_key(0,3)
button2 = keypad.get_key(0,2)
button3 = keypad.get_key(0,1)
start_button = keypad.get_key(1,2)
end_button = keypad.get_key(3,0)
while not start_button.is_pressed():
    fade_key(black, red,1,2)
    fade_key(red, black,1,2)
    sleep(0.1)

while not end_button.is_pressed():
    if button1.is_pressed():
        fade_to(black, green, wait, name="green")
        fade_to(green, black, wait, name="green")
    if button2.is_pressed():
        fade_to(black, yellow, wait, name="green")
        fade_to(yellow, black, wait, name="green")
    if button3.is_pressed():
        rainbow()
    else:
        fade_to(black, red, wait, name="red to white")
        fade_to(red,black, wait, name="red to white")

keypad.clear()
    