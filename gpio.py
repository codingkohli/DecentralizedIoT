import RPi.GPIO as GPIO #Import Raspberry Pi GPIO Library
import time
import requests
import sys

class EventCapture:

  def __init__(self, device_ip_address, device_port_number, button_pin):
    self.device_address = device_ip_address
    self.device_port = device_port
    self.button = button_pin
    self.url_report_state_change = "http://" + self.device_address + ":" + self.device_port + "/receiveStateChange"
    # Setup GPIO
    GPIO.setwarnings(False) # Ignore warnings for now.
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering.
    GPIO.setup(int(self.button), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

  def capture_event_and_report(self):
    while True:
      if GPIO.input(int(self.button)) == GPIO.HIGH:
        response = requests.get(self.url_report_state_change)
        time.sleep(0.5)

if __name__ == '__main__':
  device_ip_address = sys.argv[1]
  device_port = sys.argv[2]
  button_pin = sys.argv[3]
  event_handler = EventCapture(device_ip_address, device_port, button_pin)
  event_handler.capture_event_and_report()
