# IoT26-HW02

## Read Digital Inputs with Python

## 1. Objective

The objective of this assignment is to read digital input from a push button using Raspberry Pi and control a simple output device.

In this project, a push button is used as a digital input and an LED is used as a digital output. When the button is pressed, the LED turns on. When the button is released, the LED turns off.

## 2. Components

- Raspberry Pi
- Push button
- LED
- Resistor
- Breadboard
- Jumper wires

## 3. GPIO Pins

| Component | GPIO Pin |
|---|---|
| LED | GPIO14 |
| Button | GPIO4 |

## 4. Source Code

```python
from gpiozero import Button, LED
from signal import pause

led = LED(14)
button = Button(4)

button.when_pressed = led.on
button.when_released = led.off

pause()
```

## 5. How to Run

```bash
python3 HW2.py
```

## 6. Result

The Raspberry Pi successfully reads the button input through GPIO4.

When the button is pressed, the LED connected to GPIO14 turns on.  
When the button is released, the LED turns off.

This confirms that the Raspberry Pi can read digital input and control digital output using Python.

## 7. Screenshots and Evidence

### Source Code Screenshot

![HW2 Code](images/hw2_code.png)

### Running Program Screenshot

![HW2 Run](images/hw2_run.png)

### Raspberry Pi Button and LED Result

![HW2 Result](images/hw2_result.jpg)

## 8. Members

- 장동현 / AI·소프트웨어학부 소프트웨어전공
- 임규민 / AI·소프트웨어학부 인공지능전공
- 이형호 / AI·소프트웨어학부 인공지능전공
