#!/usr/bin/env python3

import sys

class Player():
	def __init__(self, discStyle) -> None:
		self.__discStyle = discStyle
		self.__name = ""

	@property
	def name(self):
		return self.__name

	@property
	def discStyle(self):
		return self.__discStyle

	@name.setter
	def name(self, value):
		self.__name = value

