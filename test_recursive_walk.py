#!/usr/bin/env python3
import os
import sys
from os import listdir
from PIL import Image
import datetime
import argparse
#Объявим глобальные переменные
global xml_file_folder
global watching_directory
#Проверяем количество ключей и задаем глобальные переменные
def check_key():
	parser = argparse.ArgumentParser(description='
def help():
	print("We are input incorrect data. Please check this:\nslideshow /path/to/directory /path/to/xml/file [Optional parametrs]\nCheck the optional parameters(necessarily with value)\n\t--duration, -d seconds - time to change wallpaper\n\t--transition, -t time seconds - wallpaper change time\n\t--amount, -a - amount of wallpaper")
def dir_exist(path):
	if os.path.exists(path) and os.path.isdir(path):
		return True
	else:
		return False
def is_xml(path):
	if path.rfind('.xml')>-1 and path.rfind('.xml')+4==len(path) and dir_exist(xml_folder(path)):
		xml_file_folder=xml_folder(path)
		return True
	else:
		return False
def xml_folder(path):
	if path.rfind('/')>-1:
		pat=path[0:path.rfind('/')]
	else:
		pat=os.getcwd()
	return pat
check_key()
