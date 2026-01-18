import rpi_gpio as GPIO
import time

# ----------------------------
# CONFIG
# ----------------------------

# All LEDs
LED_PINS = [4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23]

# One LED that should stay solid when tilt is active
STEADY_PIN = 21   # change this to whichever LED you want solid

# All *blinking* LEDs = all LEDs except the steady one
BLINK_PINS = [pin for pin in LED_PINS if pin != STEADY_PIN]

# Tilt sensor GPIO pin (change to your actual wiring)
TILT_PIN = 24     # example GPIO24

BLINK_INTERVAL = 0.5  # seconds


# ----------------------------
# SETUP
# ----------------------------

def setup():
    # LEDs as outputs
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    # Tilt sensor as input
    GPIO.setup(TILT_PIN, GPIO.IN)


setup()


# ----------------------------
# HELPERS
# ----------------------------

def turn_off_all():
    """Turn *all* LEDs off, including the steady one."""
    for pin in LED_PINS:
        GPIO.output(pin, GPIO.LOW)


def blink_step():
    """One blink step: blink only BLINK_PINS, keep STEADY_PIN solid ON."""
    # Steady LED ON
    GPIO.output(STEADY_PIN, GPIO.HIGH)

    # Blink others ON
    for pin in BLINK_PINS:
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(BLINK_INTERVAL)

    # Blink others OFF, steady stays ON
    for pin in BLINK_PINS:
        GPIO.output(pin, GPIO.LOW)
    time.sleep(BLINK_INTERVAL)


def is_tilted():
    """Return True if tilt is active."""
    value = GPIO.input(TILT_PIN)
    # Pick the one that matches your sensor:
    return value == GPIO.HIGH      # if HIGH = tilted
    # return value == GPIO.LOW     # if LOW = tilted (flip if needed)


# ----------------------------
# MAIN LOOP
# ----------------------------

try:
    turn_off_all()

    while True:
        if is_tilted():
            # Tilt detected → runway active
            blink_step()
        else:
            # No tilt → everything off
            turn_off_all()
            time.sleep(0.1)

except KeyboardInterrupt:
    turn_off_all()
    # If you have GPIO.cleanup() available, you can call it here.
