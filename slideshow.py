#!/usr/bin/env python3
import os
import sys
from os import listdir
from PIL import Image
import datetime
import argparse
#Проверяем количество ключей и задаем глобальные переменные
def parsing_arguments():
	parser = argparse.ArgumentParser(description='This script make xml wallpaper.',prog='slideshow')
	parser.add_argument('-p',type=str,help='path to catalog with images',
	metavar='/path/to/dir')
	parser.add_argument('-o',type=str,metavar='/path/to/file.xml',help='path to output xml files')
	parser.add_argument('-d',type=int,metavar='N',help='time display wallpaper')
	#parser.add_argument('-t',type=int, metavar='N',
	#help='time to transition from current to next wallpaper, default is off, 1 - on')
	args=parser.parse_args()
	return args
def dir_exist(path):
	if os.path.exists(path) and os.path.isdir(path):
		return True
	else:
		return False
def is_xml(path):
	if os.path.exists(os.path.dirname(path)) or os.path.splitext(path)[1]=='.xml':
		return True
	else:
		return False
def xml_file():
	if is_xml(parsing_arguments().o):
		return os.path.abspath(parsing_arguments().o)
	else:
		print('We don\'t write the output file or this incorrect.')
		sys.exit()
def watching_directory():
	if dir_exist(parsing_arguments().p):
		return os.path.abspath(parsing_arguments().p)
	else:
		print('Sorry unvalid path.')
		sys.exit()
def duration():
	if parsing_arguments().d!=None or parsing_arguments<24*60*60:
		return str(parsing_arguments().d)
	else:
		print('We don\'t write the duration or duration is very big(more 24hours)')
		sys.exit()
def list_of_images():
	images=[]
	tree=os.walk(watching_directory())
	for i in tree:
		for j in i[2]:
			path=os.path.join(i[0],j)
			im=Image.open(path)
			(width,height)=im.size
			if (width/height==16/9 and width>=1280 and height>=720):
				images.append(path)
	if images!='':
		return images
	else:
		return 'None'
def create_section(path):
	section='\t<static>\n\t\t<duration>'+duration()+'</duration>\n\t\t'+'<file>'+path+'</file>\n\t</static>\n'
	return section
def create_hat():
	date=datetime.date.today()
	if date.month%10==date.month:
		month='0'+str(date.month)
	else:
		month=str(date.month)
	if date.day%10==date.day:
		day='0'+str(date.day)
	else:
		day=str(date.day)
	year=str(date.year)
	hat='<background>\n\t<startime>\n\t\t<year>'+year+'</year>\n\t\t<month>'+month+'</month>\n\t\t<day>'+day+'</day>\n\t\t<hour>0</hour>\n\t\t<minute>00</minute>\n\t\t<second>00</second>\n\t</startime>\n'
	return hat
def create_end_xml_file():
	return '</background>'
xml_content=[]
xml_content.append(create_hat())
if list_of_images()!='None':
	for i in list_of_images():
		xml_content.append(create_section(i))
xml_content.append(create_end_xml_file())
xml=open(xml_file(),'w')
for i in xml_content:
	xml.write(i)
xml.close
