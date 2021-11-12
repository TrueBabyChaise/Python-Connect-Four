#!/usr/bin/env python3

import sys
import src.color as clr

class Player():

	def __init__(self, discStyle) -> None:
		self.__discStyle = discStyle
		self.__color = None
		self.__name = ""

	def __repr__(self) -> str:
		return f"Name : {self.__name}, Disc : {self.__discStyle}, Color : {self.__color}Color{clr.Color_Off}"

	def __str__(self) -> str:
		return f"Name : {self.__name}, Disc : {self.__discStyle}, Color : {self.__color}Color{clr.Color_Off}"

	@property
	def name(self) -> str:
		return self.__name

	@property
	def discStyle(self) -> str:
		return self.__discStyle

	@property
	def color(self) -> str:
		return self.__color
	
	@name.setter
	def name(self, value):
		self.__name = value

	def askName(self) -> str:
		tmp = "a"
		accept = "a"		
		while accept != "yes" and accept != "y":
			tmp = input("Which name do you want to use ?\n -> ")
			accept = input("Are you sure (y/n) ?\n -> ").lower()
		self.__name = tmp
		return tmp

	def askColor(self) -> str:
		colorTabValue = [clr.Red, clr.Black, clr.Blue, clr.White, clr.Yellow]
		colorTab = ["red", "black","blue", "white", "yellow"]
		tmp = "a"
		while not tmp in colorTab:
			tmp = input("Which color do you wanna play with " + self.__name + " ?\n[red, black, blue, white, yellow]\n -> ")
		self.__color = colorTabValue[colorTab.index(tmp)]
		return colorTabValue[colorTab.index(tmp)]

	def askColumn(self) -> int:
		tmp = "a"
		while not tmp.isdigit():
			tmp = input("Which column do you wanna play on " + self.__name + " ?\n -> ")
		return int(tmp)
