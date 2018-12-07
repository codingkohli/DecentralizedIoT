import RPi.GPIO as GPIO #Import Raspberry Pi GPIO Library

# Change the status of the green/red lights based on the status.
def status_change_led(status, green_pin, red_pin):
  GPIO.setwarnings(False) # Ignore warnings for now.
  GPIO.setmode(GPIO.BOARD) # Use physical pin numbering.
  GPIO.setup(int(green_pin), GPIO.OUT)
  GPIO.setup(int(red_pin), GPIO.OUT)
  if status == 0:
    # Turn the green LED off.
    GPIO.output(int(green_pin), GPIO.LOW)
    # Turn the red LED on.
    GPIO.output(int(red_pin), GPIO.HIGH)
  else:
    # Turn the grren LED on.
    GPIO.output(int(green_pin), GPIO.HIGH)
    GPIO.output(int(red_pin), GPIO.LOW)