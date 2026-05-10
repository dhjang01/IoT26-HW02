from gpiozero import Button, LED
from signal import pause

led = LED(14)
button = Button(4)

# LED ON when pressed
button.when_pressed = led.on
# LED OFF when unpressed
button.when_released = led.off

pause()
