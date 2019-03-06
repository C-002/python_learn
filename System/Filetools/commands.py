#!/usr/local/bin/python
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass

commands = {'*': 'Ms.', '+': 'Mr.'}

def processLine(line):
    '''
    if line[0] == '*':
        print("Ms.", line[1:], end='')
    elif line[0] == '+':
        print("Mr.", line[1:], end='')
    else:
        raise UnknownCommand(line)
    '''
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)

filename = 'data.txt'
if len(argv)==2:
    filename = argv[1]
scanner(filename, processLine)