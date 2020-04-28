from Tkinter import *
import tkFont
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
##hardware
led = LED(24)

##  GUI DEFINITIONS ##
win = Tk()
win.title("Morse Code")
myFont = tkFont.Font(family='Helvetica',size = 12, weight="bold")

### Label creation
Label_1 = Label(win, text = "Enter the text: ")
Label_1.pack()

### Word Limit
word = StringVar()
max_length =12
def letter_limit(*arg):
	user_input =word.get()
	if len(user_input)>max_length:
		word.set(user_input[:max_length])
word.trace_variable("w",letter_limit)

### Text Box
textBox = Entry(win, bd = 10, textvariable = word)
textBox.pack(side=LEFT)

### EVENT FUNCTIONS ###
def longDash():
	led.on()
	time.sleep(3)
	led.off()
	time.sleep(1)

def shortDash():
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)

def space():
	led.off()
	time.sleep(6)

def Blink(letter):
	if letter == "a":
		shortDash()
		longDash()

	if letter == "b":
                longDash()
		shortDash()
		shortDash()
		shortDash()

	if letter == "c":
		longDash()
                shortDash()
                longDash()
		shortDash()

	if letter == "d":
                longDash()
		shortDash()
		shortDash()

	if letter == "e":
                shortDash()

	if letter == "f":
		shortDash()
		shortDash()
                longDash()
                shortDash()

	if letter == "g":
                longDash()
                longDash()
                shortDash()
	if letter == "h":
                shortDash()
                shortDash()
                shortDash()
		shortDash()

	if letter == "i":
                shortDash()
                shortDash()

	if letter == "j":
		shortDash()
                longDash()
		longDash()
		longDash()

	if letter == "k":
                longDash()
                shortDash()
               	longDash()

	if letter == "l":
		shortDash()
                longDash()
                shortDash()
                shortDash()

	if letter == "m":
                longDash()
                longDash()

	if letter == "n":
                longDash()
                shortDash()

	if letter == "o":
                longDash()
                longDash()
                longDash()

	if letter == "p":
		shortDash()
                longDash()
                longDash()
                shortDash()

	if letter == "q":
		longDash()
                longDash()
                shortDash()
                longDash()

	if letter == "r":
                shortDash()
                longDash()
                shortDash()

	if letter == "s":
                shortDash()
                shortDash()
                shortDash()

	if letter == "t":
                longDash()

	if letter == "u":
                shortDash()
                shortDash()
                longDash()

	if letter == "v":
                shortDash()
                shortDash()
                shortDash()
		longDash()

	if letter == "w":
		shortDash()
                longDash()
                longDash()
                shortDash()

	if letter == "x":
                longDash()
                shortDash()
                shortDash()
		longDash()

	if letter == "y":
                longDash()
                shortDash()
                longDash()
		longDash()

	if letter =="z":
                longDash()
                longDash()
                shortDash()
		shortDash()

        if letter =="1":
                shortDash()
                longDash()
                longDash()
                longDash()
		longDash()

        if letter =="2":
		shortDash()
                shortDash()
                longDash()
                longDash()
                longDash()

        if letter =="3":
                shortDash()
                shortDash()
                shortDash()
                longDash()
		longDash()

        if letter =="4":
                shortDash()
                shortDash()
                shortDash()
                shortDash()
		longDash()

        if letter =="5":
                shortDash()
                shortDash()
                shortDash()
                shortDash()
		shortDash()

        if letter =="6":
                longDash()
                shortDash()
                shortDash()
                shortDash()
		shortDash()

        if letter =="7":
                longDash()
                longDash()
                shortDash()
                shortDash()
		shortDash()

        if letter =="8":
                longDash()
                longDash()
		longDash()
                shortDash()
                shortDash()

        if letter =="9":
                longDash()
                longDash()
		longDash()
                longDash()
                shortDash()

        if letter =="0":
                longDash()
                longDash()
                longDash()
                longDash()
                longDash()

	if letter ==' ':
		space()

def runProgram():
	text = textBox.get()
	for answer in text.lower():
		Blink(answer)

def exitProgram():
	GPIO.cleanup()
	win.quit()

### WIDGETS ###
generateButton = Button(win, text = 'Generate', font = myFont, command = runProgram,bg ='green',height =1, width = 5)
generateButton.pack(side=TOP)

exitButton = Button(win, text = 'Exit', font = myFont, command = exitProgram,bg ='red',height =1, width = 5)
exitButton.pack(side= BOTTOM)

win.mainloop() #loop forever

