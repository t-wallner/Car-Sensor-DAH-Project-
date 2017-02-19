# Imports
from DistanceSensor import DistanceSensor # import class
import webiopi
from webiopi.devices.digital import PCF8574A
mcp = PCF8574A(slave=0x38) # distance sensor 
import tkSnack # audio import
import Tkinter # audio import

# Rename GPIO lib
GPIO = webiopi.GPIO

# Set which PCF8574 GPIO pin is connected to the LED (negative logic)
LED0 = 0
LED1 = 1
LED2 = 2
LED3 = 3
LED4 = 4
LED5 = 5
LED6 = 6
LED7 = 7
# Set switch pin
SWITCH = 14

# Setup GPIOs
mcp.setFunction(LED0, 0) #Set Pin as output
mcp.setFunction(LED1, 0)
mcp.setFunction(LED2, 0)
mcp.setFunction(LED3, 0)
mcp.setFunction(LED4, 0)
mcp.setFunction(LED5, 0)
mcp.setFunction(LED6, 0)
mcp.setFunction(LED7, 0)
GPIO.setFunction(SWITCH,GPIO.IN) # Set Switch as input

#Method to play a note using tkSnack
def playNote(freq,duration):
        snd = tkSnack.Sound()
        filt = tkSnack.Filter('generator', freq, 30000, 0.0,'sine', int(11500*duration))
        snd.stop()
        snd.play(filter=filt, blocking =1)

# Initialize sound system
tkSnack.initializeSnack(Tkinter.Tk())

# Calling on reading method in DistanceSensor class
sensor = DistanceSensor()

# Loop for ever
while True:
        # Only run if the switch button is pressed
        if (GPIO.digitalRead(SWITCH) == GPIO.HIGH):
                # Take a distance measurement
                distance = sensor.reading(0)
                # If distance if between 0 and 5 
                # --> light all LEDs and play note
                if (distance>0 and distance<5):
                        mcp.portWrite(0)
                        playNote(1047,1)
                # If distance if between 5 and 10
                # --> light first 7 LEDs and play note
                if (distance >5 and distance<10):
                        mcp.portWrite(1)
                        playNote(784,1)
                        webiopi.sleep(0.25)
                # If distance if between 10 and 15
                # --> light first 6 LEDs and play note
                if (distance >10 and distance<15):
                        mcp.portWrite(3)
                        playNote(523,1)
                        webiopi.sleep(0.5)
                # If distance if between 15 and 20
                # --> light first 5 LEDs
                if (distance >15 and distance<20):
                        mcp.portWrite(7)
                # If distance if between 20 and 25
                # --> light first 4 LEDs
                if (distance>20 and distance<25):
                        mcp.portWrite(15)
                # If distance if between 25 and 30
                # --> light first 3 LEDs
                if (distance >25 and distance<30):
                        mcp.portWrite(31)
                # If distance if between 30 and 35
                # --> light first 2 LEDs
                if (distance >30 and distance<35):
                        mcp.portWrite(63)
                # If distance if between 35 and 40
                # --> light first LED
                if (distance >35 and distance<40):
                        mcp.portWrite(127)
                # If distance is greater than 40 
                # --> all LEDs turned off
                if (distance >40):
                        mcp.portWrite(255)