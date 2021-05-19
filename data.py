#!/usr/bin/python

from urllib.request import urlopen
import random

def aleat():
	x = random.randint(0, 3)
	if x==0:
		ran_1 = urlopen("https://pastebin.com/raw/fQbETQiq")
		for lineas in ran_1.readlines():
			print(lineas)
			ran_1.close()
	elif x==1:
		ran_2 = urlopen("https://pastebin.com/raw/3iKNEsvj")
		for lineas in ran_2.readlines():
			print(lineas)
			ran_2.close()
	elif x==2:
		ran_3 = urlopen("https://pastebin.com/raw/dZdjMp3X")
		for lineas in ran_3.readlines():
			print(lineas)
			ran_3.close()
	else:
		if x==3:
			ran_4 = urlopen("https://pastebin.com/raw/1uY8GqKC")
			for lineas in ran_4.readlines():
				print(lineas)
				ran_4.close()



def colombia():
    col = urlopen("https://pastebin.com/raw/dZdjMp3X")
    for lineas in col.readlines():
    	print(lineas)
    	col.close()

def usa():
	USA = urlopen("https://pastebin.com/raw/3iKNEsvj")
	for lineas in USA.readlines():
		print(lineas)
		USA.close()


def brasil():
	bra = urlopen("https://pastebin.com/raw/1uY8GqKC")
	for lineas in bra.readlines():
		print(lineas)
		bra.close()