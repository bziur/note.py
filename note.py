#!/usr/bin/env python

import sys
import argparse
from subprocess import call
from os.path import expanduser
from os import getenv

# adding options
parser = argparse.ArgumentParser()
notegroup = parser.add_mutually_exclusive_group();
notegroup.add_argument('-n', '--new',	action='store_true',	help='Create note.')
notegroup.add_argument('-e', '--edit',	action='store_true',	help='Edit note.')
notegroup.add_argument('-i', '--insert',action='store',		help='Input line into a note')
parser.add_argument('-p', '--pretty',	action='store_true',	help='Pretty titles.')
parser.add_argument('-l', '--ls',	action='store_true',	help='List notes.')
parser.add_argument('note',					help='Name of the note',	nargs='?',	default='todo')
parser.add_argument('-r', '--remove',	action='append',	help='Remove note(s).')

args = parser.parse_args()

# CONFIGURATION

directory = expanduser('~') + '/Documents/notes/'
ext = '.txt'

# DO COMMANDS

# if to remove, remove
if args.remove :
	for to_remove in args.rem :
		filename = directory + getname(pop(args.rem)) + ext
		if filename :
			call('rm', filename)
# if note, edit, show or do sth
else :
	filename = directory + args.note + ext
	if args.new or args.edit :
		editor = getenv('EDITOR')
		call([editor, filename])
	elif args.insert :
		call([args.insert, '>>', filename])
	else :
		if args.pretty :
			print('\033[1m' + args.note + ' content:\033[0m')
		call(['cat', filename])
# if list, list
if args.ls :
	call(['dir', '-1t', directory])

