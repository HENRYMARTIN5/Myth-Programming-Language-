from time import sleep
from termcolor import cprint as cpr
import sys
import varHandlerSystem
from utils import clear
varHandler = varHandlerSystem.variableHandler()
varHandler.create("a", 1)
varHandler.create("a", varHandler.get("a") + 1)
print(str(varHandler.get('a')))
