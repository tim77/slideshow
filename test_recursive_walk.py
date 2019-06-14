#!/usr/bin/env python3
import os
import sys
from os import listdir
from PIL import Image
import datetime
import argparse
#Объявим глобальные переменные
global xml_file_folder
global xml_file
global watching_directory
#Проверяем количество ключей и задаем глобальные переменные
def parsing_arguments():
	parser = argparse.ArgumentParser(description='This script make xml wallpaper.',prog='slideshow')
	parser.add_argument('-p',type=str,help='path to catalog with images',
	metavar='/path/to/dir')
	parser.add_argument('-o',type=str,metavar='/path/to/file.xml',help='path to output xml files')
	parser.add_argument('-d',type=int,metavar='N',help='time display wallpaper')
	parser.add_argument('-t',type=int,metavar='N',help='time to transition from current to next wallpaper')
	args=parser.parse_args()
	return args
def dir_exist(path):
	if os.path.exists(path) and os.path.isdir(path):
		return True
	else:
		return False
def is_xml(path):
	if os.path.exists(os.path.dirname(path)) and os.path.splitext(path)[1]=='.xml':
		return True
	else:
		return False
def xml_folder(path):
	if path.rfind('/')>-1:
		pat=path[0:path.rfind('/')]
	else:
		pat=os.getcwd()
	return pat
print (parsing_arguments())
print(is_xml(parsing_arguments().o))
