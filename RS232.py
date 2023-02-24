import os
import os, sys, tty, time

MIN_ANGLE = -90
MAX_ANGLE = 90


class RS232:
    def __init__(self, speed=9600):
        grpname = "dialout"
        f = os.popen("groups")
        if not f.read().split().count(grpname):
            pass
            #print("You must be a member of group: %s" % grpname)
            # exit(1)
        f.close()
        f = os.popen("ls /dev/ttyU* 2>/dev/null")
        devname = f.readline().strip()
        f.close()
        if not devname:
            pass
            #print("USB-RS232 serial port not found")
            #exit(1)
        if os.system("stty -F %s -echo raw %d 2>/dev/null" % (devname, speed)):
            pass
            #print("Error while initializing USB-RS232 serial port")
            # exit(1)
        self.device = open(devname, "wb")
        self.motor = 1

    def set_motor(self, n):
        n = int(n)
        if n < 1 or n > 3:
            print("Not valid servo number: %d. Must be from 1 to 3" % n)
            return
        self.motor = n

    def get_motor(self):
        return self.motor

    def rotate(self, angle=0):
        angle = round(angle)
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            print("Not valid angle: %d. Must be in range from -90 to +90." % angle)
            return
        if angle < 0: angle += 256
        buf = bytes.fromhex("FFFF3354%02X%02X%02X00" % (self.motor, angle, angle ^ 0xFF))
        self.device.write(buf)
        self.device.flush()


class Servos:
    def __init__(self, angle1=0, angle2=0, angle3=0, n_servos=3):
        self.initial_state = [angle1, angle2, angle3]
        self.dev = RS232()
        self.n_servos = n_servos
        self.rotate(n=-1)

    def __del__(self):
        self.rotate(n=-1)

    def __call__(self, n=0):
        if n:
            self.dev.set_motor(n)
            self.dev.rotate(self.angles[n - 1])
            return
        for i in range(self.n_servos):
            self.dev.set_motor(i + 1)
            self.dev.rotate(self.angles[i])

    def rotate(self, angle=0, n=0):
        if n > 0:
            self.angles[n - 1] = angle
            self(n)
            return
        elif n == -1:
            self.angles = self.initial_state.copy()
        else:
            self.angles = [angle for i in range(self.n_servos)]
        self()

    def inc(self, n):
        if self.angles[n - 1] == MAX_ANGLE: return
        self.angles[n - 1] += 1
        self(n)

    def dec(self, n):
        if self.angles[n - 1] == MIN_ANGLE: return
        self.angles[n - 1] -= 1
        self(n)

    def get_angles(self):
        return self.angles
