from RPi import GPIO
from firebase import firebase

token = 'LQdeuWHXvtgCg5Sdx3JUfuGV1ZaUmfbA7Nah5hE3'
url = 'https://dmini-internet-of-things.firebaseio.com/'

firebase = firebase.FirebaseApplication(url, token)

GPIO.setmode(GPIO.BCM)
ledcolor = {'yellow': 20, 'red': 21}

GPIO.setup(ledcolor.values(), GPIO.OUT)


def setLED(ledno, status):
	if status == 'down':
		GPIO.output(ledno,GPIO.HIGH)
	else:
		GPIO.output(ledno, GPIO.LOW)


while True:
	status_list = firebase.get('/lights', '/')
	setLED(ledcolor['yellow'], status_list[0])
	setLED(ledcolor['red'], status_list[1])
