import serial
import time

"""
Simple parser for interfacing with the Waterrower S4 computer over a tty
on a Raspberry Pi.   This most-likely will work on other host computers
with some simple modification.

Information for the S4 proocol came from:
    Water Rower S4 & S5 USB Protocol
    Issue 1.04 - Aug 2009

"""
class S4State:
    CONNECTING = 1
    IDLE = 2
    
class S4Interface(object):
    def __init__(self):
        self.port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=0.2)
        # Send the intro "USB" message to kick off the S4 so it starts streaming data
        self.port.write("USB\r\n")
        self.Reset()
        
    def  DoIt(self):  

        S4Process = 1
        start_time = time.time()

        # Run for most 0.5 seconds and bail when completely idle
        while S4Process and (time.time() - start_time < 0.5):
            rcv = self.port.readline()

            if rcv:
                self.parse(rcv)
                # If 0.5 second has elapsed from the previous query, query kcal memory again
                if (time.time() - self.query_time) >= 0.5:
                    self.port.write("IRT08A\r\n")
                    self.query_time = time.time()
            else:
                # readline got nothing, so bail
                S4Process = 0

    def parse(self, rcv):
        
        if 'PING\r\n' == rcv:
            pass
        elif '_WR_\r\n' == rcv:
            # Acked USB start
            pass
        elif 'ERROR\r\n' == rcv:
            print("Error message from S4!")
            
        elif 'OK\r\n' == rcv:
            #
            pass
        elif rcv[0] == 'P':
            # TODO: handle Pulse values of encoder wheel
            pass
        elif 'SE\r\n' == rcv:
            # Stroke end
            self.stroke_count = self.stroke_count + 1
            self.last_stroke_time = time.time()
        elif 'SS\r\n' == rcv:
            # Stroke start
            # TODO: maybe calculate average stroke duration?
            pass
        elif rcv[0] == 'I':
            # Only thing starting with I should be the response with kcal data
            kcal_string = rcv[6:6+6]
            kcal = int(kcal_string, 16)

            if self.first_kcal:
                self.last_kcal = kcal
                self.first_kcal = 0

            self.kcal = (kcal - self.last_kcal)
            self.last_kcal = kcal
            
            print('KCAL:' + repr(self.kcal))
        elif 'AKR\r\n' == rcv:
            self.Reset()
        else:
            print("Got: [" + repr(rcv) + "] but don't know what it means.")

    def Exit(self):
        self.port.write("EXIT\r\n")

    def Reset(self):
        self.query_time = 0
        self.stroke_count = 0
        self.kcal = 0
        self.last_kcal = 0
        self.first_kcal = 1 # flag for first time we get the kcal tally - use the current value as a base
        self.last_stroke_time = time.time()

# Example of running this as a standalone test

#s4 = S4Interface()
#s4.DoIt()
   

    
