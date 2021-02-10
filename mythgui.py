import PySimpleGUI as sg 
import myth, output
# Add some color 
# to the window 
sg.theme('SandyBeach')      
  
# Very basic window. 
# Return values using 
# automatic-numbered keys 
layout = [ 
    [sg.Text('Please enter the data you wish to compile.')], 
    [sg.Text('Input file', size =(15, 1)), sg.InputText()], 
    [sg.Text('Output file', size =(15, 1)), sg.InputText()], 
    [sg.Text('Any other options', size =(15, 1)), sg.InputText()], 
    [sg.Submit(), sg.Cancel()] 
] 
  
window = sg.Window('Myth', layout) 
event, values = window.read() 
window.close() 
  
# The input data looks like a simple list  
# when automatic numbered 
print(event, values[0], values[1], values[2])    
myth.compile(values[0], values[1], myth.debug, output.py)