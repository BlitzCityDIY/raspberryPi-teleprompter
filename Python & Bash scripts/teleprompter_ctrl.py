import time
import board
import digitalio
import pynput.mouse
from pynput.keyboard import Key, Controller

faster = digitalio.DigitalInOut(board.D17)
faster.direction = digitalio.Direction.INPUT
faster.pull = digitalio.Pull.UP

slower = digitalio.DigitalInOut(board.D4)
slower.direction = digitalio.Direction.INPUT
slower.pull = digitalio.Pull.UP

toggle = digitalio.DigitalInOut(board.D27)
toggle.direction = digitalio.Direction.INPUT
toggle.pull = digitalio.Pull.UP

fullscreen = digitalio.DigitalInOut(board.D18)
fullscreen.direction = digitalio.Direction.INPUT
fullscreen.pull = digitalio.Pull.UP

mouse = pynput.mouse.Controller()
keyboard = Controller()

#  default teleprompter speed
delay = 2

running = False
faster_state = False
slower_state = False
maximized = True
fullscreen_state = False

while True:
    if not faster.value and faster_state:
        faster_state = False
    if not slower.value and slower_state:
        slower_state = False
    if not fullscreen.value and fullscreen_state:
        fullscreen_state = False
    if running:
        mouse.scroll(0, -1)
        print(delay)
        time.sleep(delay)
    if faster.value and not faster_state:
        delay -= 0.5
        if delay < 0:
            delay = .5
        faster_state = True
        print("faster")
    if slower.value and not slower_state:
        delay += 0.5
        slower_state = True
        print("slow down")
    if maximized and (fullscreen_state and not fullscreen.value):
        fullscreen_state = True
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        maximized = False
    if not maximized and (fullscreen_state and not fullscreen.value):
        fullscreen_state = True
        keyboard.press(Key.f1)
        keyboard.release(Key.f1)
        maximized = True
    if running and not toggle.value:
        running = False
    if not running and toggle.value:
        running = True
        print("starting")
