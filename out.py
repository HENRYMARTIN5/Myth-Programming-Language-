from time import sleep
from termcolor import cprint as cpr
import sys
import varHandlerSystem
from utils import clear
varHandler = varHandlerSystem.variableHandler()
print("The OUT function prints text in the console.
")
print("This is a delay of 1 second.
")
try:
	sleep(float(1))
except ValueError:
	sys.exit()
print("This was printed after a delay!
")
cpr('This is red.
', 'red')
cpr('This is yellow.
', 'yellow')
cpr('This is green.
', 'green')
cpr('This is cyan.
', 'cyan')
cpr('This is blue.
', 'blue')
cpr('This is magenta.
', 'magenta')
cpr('This is grey.
', 'grey')
cpr('This is white.
', 'white')
varHandler.create("greeting", "Hello there!")
varHandler.create("greeting", "Hello! Nice weather we're having, isn't it?")
print("Here is a greeting for you:
")
print("\n
")
print(str(varHandler.get('greeting')))
varHandler.create("thisIsANumber", 120)
print(str(varHandler.get('thisIsANumber')))
varHandler.create("thisIsANumber", varHandler.get("thisIsANumber") + -60)
print(str(varHandler.get('thisIsANumber')))
varHandler.create("thisIsANumber", varHandler.get("thisIsANumber") + 20)
print(str(varHandler.get('thisIsANumber')))
try:
	sleep(float(35))
except ValueError:
	sys.exit()
print("The console was just cleared!
")
try:
	sleep(float(20))
except ValueError:
	sys.exit()
sys.exit()
