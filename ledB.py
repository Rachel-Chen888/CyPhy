import rpi_gpio as GPIO
import time

# ----------------------------
# CONFIG
# ----------------------------

# All LEDs
LED_PINS = [4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23]

# One LED that should stay solid
STEADY_PIN = 21   # change this to whichever LED you want solid

# All *blinking* LEDs = all LEDs except the steady one
BLINK_PINS = [pin for pin in LED_PINS if pin != STEADY_PIN]

# Tilt sensor GPIO pin (change to your actual wiring)
TILT_PIN = 24     # example GPIO24

# Flicker speeds
BLINK_INTERVAL_NORMAL = 0.5   # no tilt
BLINK_INTERVAL_TILTED = 0.2   # faster when tilted

# Attack timing: deliver "exploit" 10 seconds after program start
ATTACK_DELAY_SECONDS = 10.0

# ----------------------------
# GLOBAL STATE
# ----------------------------

SYSTEM_COMPROMISED = False

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


def blink_step(interval):
    """
    One blink step: blink only BLINK_PINS, keep STEADY_PIN solid ON.
    interval = how long to wait in each on/off phase.
    """
    # Steady LED ON
    GPIO.output(STEADY_PIN, GPIO.HIGH)

    # Blink others ON
    for pin in BLINK_PINS:
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)

    # Blink others OFF, steady stays ON
    for pin in BLINK_PINS:
        GPIO.output(pin, GPIO.LOW)
    time.sleep(interval)


def is_tilted():
    """Return True if tilt is active."""
    value = GPIO.input(TILT_PIN)
    return value == GPIO.LOW      # flip to GPIO.LOW if your sensor is inverted


# ----------------------------
# "EXPLOIT" SIMULATION
# ----------------------------

def simulate_oob_attack():
    """
    Simulate an out-of-bounds write style bug and mark system as compromised.
    This is just for demo; it does NOT touch real QNX internals.
    """
    global SYSTEM_COMPROMISED

    print("\n[ATTACK] Simulating memory corruption (CVE-2025-2474 / CWE-787)...")

    buffer = [0, 0, 0, 0]
    try:
        for i in range(10):  # deliberately go out of bounds
            buffer[i] = 1
    except IndexError:
        print("[ATTACK] Out-of-bounds write detected. Controller state corrupted.")

    SYSTEM_COMPROMISED = True
    print("[ATTACK] SYSTEM_COMPROMISED = True → runway logic now blacked out.\n")


def attack_effect():
    """Cyber-physical effect after compromise: runway blackout."""
    turn_off_all()


# ----------------------------
# MAIN LOOP
# ----------------------------

try:
    turn_off_all()
    startT = time.time()  # program start time

    while True:
        # Check if we should trigger the attack (purely time-based)
        if not SYSTEM_COMPROMISED:
            elapsed = time.time() - startT
            if elapsed >= ATTACK_DELAY_SECONDS:
                simulate_oob_attack()

        if SYSTEM_COMPROMISED:
            # COMPROMISED MODE: ignore tilt, keep everything OFF
            attack_effect()
            time.sleep(0.2)
            continue

        # NORMAL MODE: always flicker; tilt just changes speed
        tilted = is_tilted()

        if tilted:
            # Faster flicker when tilt is active
            blink_step(BLINK_INTERVAL_TILTED)
        else:
            # Slower flicker when no tilt
            blink_step(BLINK_INTERVAL_NORMAL)

except KeyboardInterrupt:
    print("\n[INFO] Stopping program, cleaning up GPIO...")
    turn_off_all()
    GPIO.cleanup()
