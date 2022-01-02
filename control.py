#GPIO 1-2 Wheels 1&2, 3-4 wheels 3-4 
import time
import random
import RPi.GPIO as GPIO
import thread
import sys
from uuid import getnode as getMac
#import bluetooth
#print(dir(bluetooth))
from bluetooth import *

class robotMain:
	def mainLoop(self):
		self.done = False
		if len(sys.argv) == 1:
                        while not self.done:
                                if self.remoteControl.pokerGet():
                                        self.poker.stab()
                                self.laser.point(self.remoteControl.laserGet())
                                if not raw_input("Should I shoot?\n").startswith('f'):
                                        self.laser.shoot()
                                self.motion.motor(self.remoteControl.wheelsGet())
                                if self.sensor.hitSense():
                                        print "I got hit!"
                                        self.robotHealth.hit()
                                        if self.robotHealth.deadSense():
                                                self.initDeath()
                else:
                        while True:
                                self.motion.motor("forward")
                                time.sleep(0.5)
                                self.motion.motor("left")
                                time.sleep(0.5)
                                self.motion.motor("backwards")
                                time.sleep(0.5)
                                self.motion.motor("forward")
                                time.sleep(0.5)
                                self.motion.motor("right")
                                time.sleep(0.5)
                                self.motion.motor("backwards")
                                time.sleep(0.5)
	def __init__(self):
                GPIO.setwarnings(False)
                GPIO.cleanup()
                GPIO.setmode(GPIO.BOARD)
                self.GPIOlist = [0,0,3,5,7,29,31,26,24,21,19,23,32,33,8,10,36,11,12,35,38,40,15,16,18,22,37,13]
                for n in range(2,27):
                        GPIO.setup(self.GPIOlist[n],GPIO.OUT)
                        GPIO.output(self.GPIOlist[n],False)
                lw = [self.GPIOlist[2],self.GPIOlist[3]]
                rw = [self.GPIOlist[4],self.GPIOlist[5]]
                self.robotHealth = Health()
		self.sensor = HitSensor()
		self.remoteControl = Remote()
		self.motion = Wheels(lw,rw)
		self.laser = Laser(self.GPIOlist[10])
		self.poker = Poker()
		self.bluetooth = Bluetooth()
		self.bluetooth.open()
	def initDeath(self):
		print "I'm dead..."
		for n in range(2,27):
                        GPIO.output(self.GPIOlist[n],False)
		self.done = True
class Health:
	def __init__(self):
		self.life = 5
	def hit(self):
		if self.life > 0:
			self.life -= 1
		print ("My health is " + str(self.life))
	def deadSense(self):
		if self.life < 1:
			return True
		else:
			return False
class HitSensor:
	def hitSense(self):
		hit = (raw_input("Am I hit?\n"))
		if len(hit) > 0:
			if hit[0].lower() == 'f':
				return False
			else:
				return True
		else:
			return True
class Remote:
	def wheelsGet(self):
		wheelsInput = raw_input("Where are you moving?\n")
		if wheelsInput.lower() == 'left':
			return 'left'
		elif wheelsInput.lower() == 'right':
			return 'right'
		elif wheelsInput.lower() == 'forward':
                        return 'forward'
                elif wheelsInput.lower() == 'backwards':
                        return 'backwards'
		else:
			return ''
	def laserGet(self):
		laserInput = raw_input("Where is my laser pointing?\n")
		if laserInput.lower() == 'up':
			return 'up'
		elif laserInput.lower() == 'down':
			return 'down'
		else:
			return ''
	def pokerGet(self):
		stabInput = raw_input("Should I stab?\n")
		if len(stabInput) > 0:
			if stabInput[0] == 'f':
				return False
			else:
				return True
		else:
			return True
class Wheels:
#Wheel 0 bottom left, wheel 1 bottom left, wheel 2 forward left, wheel 3 forward right
#First GPIO makes forward, other makes backward
        def __init__(self,lw,rw):
                self.wheelList = [lw,rw]
        def activateWheel(self,wheelPair,direction):
                self.deactivateWheels(wheelPair)
                GPIO.output(self.wheelList[wheelPair][0],direction)
                GPIO.output(self.wheelList[wheelPair][1],not direction)
        def deactivateWheels(self,wheelPair):
                for pin in self.wheelList[wheelPair]:
                        GPIO.output(pin,False)
        def deactivateAllWheels(self):
                for wheelPair in range(0,len(self.wheelList)):
                        self.deactivateWheels(wheelPair)
        def motor(self,direction):
		if direction == 'left':
			self.activateWheel(0,False)
			self.activateWheel(1,True)
			time.sleep(1)
			self.deactivateAllWheels()
		elif direction == 'right':
			self.activateWheel(0,True)
			self.activateWheel(1,False)
			time.sleep(1)
			self.deactivateAllWheels()
                elif direction == 'forward':
                        for n in range(0,2):
                                self.activateWheel(n,True)
                        time.sleep(1)
                        self.deactivateAllWheels()
                elif direction == 'backwards':
                        self.activateWheel(0,False)
                        self.activateWheel(1,False)
                        time.sleep(1)
                        self.deactivateAllWheels()
                else:
			print 'I am not moving'
class Laser:
        def __init__(self,pin):
                self.pin = pin
	def shootProcess(self):
		GPIO.output(self.pin,True)
		time.sleep(5)
		GPIO.output(self.pin,False)
        def shoot(self):
                thread.start_new_thread(self.shootProcess,())
	def point(self,direction):
		if direction.lower() == 'up':
			print 'Laser is pointing up'
		elif direction.lower() == 'down':
			print "Laser is pointing down"
		else:
			print 'Laser is not moving'
class Poker:
	def stab(self):
		print "I'm stabbing!"
class Bluetooth:
        def __init__(self):
                self.mac = getMac()
                self.uuid = "00001108-0000-1000-8000-00805f9b34fb"
        def open(self):
                self.serverSock = BluetoothSocket( RFCOMM )
                self.serverSock.bind(("",PORT_ANY))
                self.serverSock.listen(1)
                print("I am not advertising Robot-%s" %self.mac)
                advertise_service(self.serverSock,"Robot-%s" %self.mac,service_id=self.uuid,service_classes=[self.uuid,HEADSET_CLASS],profiles=[HEADSET_PROFILE])
                print("Advertising")
                self.client_sock, self.client_info = self.serverSock.accept()
                print(self.serverSock.accept())
robot = robotMain()
robot.mainLoop()

