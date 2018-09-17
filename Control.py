import time
import random
class robotMain:
	def mainLoop(self):
		self.done = False
		while not self.done:
			if self.remoteControl.pokerGet():
				self.poker.stab()
			self.laser.point(self.remoteControl.laserGet())
			self.motion.motor(self.remoteControl.wheelsGet())
			if self.sensor.hitSense():
				print "I got hit!"
				self.robotHealth.hit()
				if self.robotHealth.deadSense():
					self.initDeath()

	def __init__(self):
		self.robotHealth = Health()
		self.sensor = HitSensor()
		self.remoteControl = Remote()
		self.motion = Wheels()
		self.laser = Laser()
		self.poker = Poker()
	def initDeath(self):
		print "I'm dead..."
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
	def motor(self,bar):
		if bar == 'left':
			print 'Go left!'
		elif bar == 'right':
			print 'Go right!'
		else:
			print 'I am not moving'
class Laser:
	def shoot(self):
		print 'I shot!'
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
sys = robotMain()
sys.mainLoop()