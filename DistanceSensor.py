# imports
import time
import webiopi

class DistanceSensor:
        # relabel webiopi GPIO
        GPIO = webiopi.GPIO

        # method for making a distance measurement
        def reading(self,sensor):

                TRIG  = 17 # the pin that's connected to "Trig"
                ECHO = 27 # the pin that's connected to "Echo"

                # Disable any warning message
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BCM)

                if sensor ==0:

                         # set TRIG pin as output
                        GPIO.setFunction(TRIG,GPIO.OUT)
                        # set ECHO pin as in
                        GPIO.setFunction(ECHO,GPIO.IN)
                        # set TRIG to active low
                        GPIO.digitalWrite(TRIG, GPIO.LOW) 

                        time.sleep(0.3)

                        # sensor manual says a pulse length of
                        # 10Us will trigger the sensor to
                        # transmit 8 cycles of ultrasonic burst
                        # at 40kHz and wait for the reflected
                        # ultrasonic burst to be received

                        # To get a pusle length of 10Us we need 
                        # to start the pulse, then wait for 10 
                        # microseconds,then stop the pulse.
                        # This will result in the pulse length
                        # being 10Us.

                        GPIO.digitalWrite(TRIG, True)
                        time.sleep(0.00001)
                        GPIO.digitalWrite(TRIG, False)

                        # listen to the input pin. 0 means 
                        # nothing is happening. Once a signal
                        # is received the value will be 1 so
                        # the while loop stops and has the last 
                        # recorded time the signal was 0
                        while GPIO.digitalRead(ECHO) == 0:
                                signaloff = time.time()

                        # listen to the input pin. Once a signal
                        # is received, record the time the
                        #  signal came through
                        while GPIO.digitalRead(ECHO) == 1:
                                signalon = time.time()

                        # work out the difference in the two
                        # recorded times above to calculate the
                        # distance of an object to sensor
                        timepassed = signalon - signaloff

                        # we now have our distance but it's not
                        # in a useful unit of measurement.
                        # Convert this distance into cm.
                        # The speed of sound is 34000 cm/s
                        distance = timepassed *34000/2

                        # return the distance of an object in
                        # front of the sensor in cm
                        return distance

                        # Cleanup GPIO
                        GPIO.cleanup()
                # catch if sensor 0 is not called on
                else:
                        print "Incorrect usonic() function variable."
                        return 0