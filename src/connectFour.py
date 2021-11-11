#!/usr/bin/env python3

import sys

class ConnectFour():

	def __init__(self, heigth=6, width=7, lineLenToWin=4) -> None:
		self._board = []
		self._height = heigth
		self._width = width
		self._lineLenToWin = lineLenToWin
		self.__createBoard()
		pass

	def __repr__(self) -> str:
		string = ""
		for y in range(self._height):
			for x in range(self._width):
				string += self._board[y][x]
			string += "\n"
		return string
	
	def __str__(self) -> str:
		string = ""
		for y in range(self._height):
			for x in range(self._width):
				string += self._board[y][x]
			string += "\n"
		return string
	
	def resetBoard(self) -> None:
		self.__createBoard()

	def __createBoard(self) -> None:
		self._board = [['0' for i in range(self._width)] for y in range(self._height)]

	def isColumnFull(self, column) -> bool:
		if self.getDiscColumnHeight(column) <= -1:
			return True
		return False

	def addDisc(self, column, discStyle) -> bool:
		if column >= self._width:
			print("Column doesn't exist", file=sys.stderr)
			return False
		if self.isColumnFull(column):
			print("Column is full", file=sys.stderr)
			return False
		self._board[self.getDiscColumnHeight(column)][column] = discStyle
		return True

	def getDiscColumnHeight(self, column) -> int:
		heigth = 0
		for row in self._board:
			if row[column] != '0':
				return heigth - 1
			heigth += 1
		return self._height - 1