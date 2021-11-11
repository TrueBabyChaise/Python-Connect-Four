#!/usr/bin/env python3

import sys

class Player():
	def __init__(self, discStyle) -> None:
		self.__discStyle = discStyle
		self.__name = ""

	def __repr__(self) -> str:
		return "Player : " + self.__name + ", Disc : " + self.__discStyle

	def __str__(self) -> str:
		return "Player : " + self.__name + ", Disc : " + self.__discStyle

	@property
	def name(self) -> str:
		return self.__name

	@property
	def discStyle(self) -> str:
		return self.__discStyle

	@name.setter
	def name(self, value):
		self.__name = value

	def askColumn(self) -> int:
		tmp = "a"
		while not tmp.isdigit():
			tmp = input("Which column do you wanna play on " + self.__name + " ?\n -> ")
		return int(tmp)
