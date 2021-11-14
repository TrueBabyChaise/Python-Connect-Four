#!/usr/bin/env python3

import sys

class ConnectFour():

	def __init__(self, nbRow=6, nbColumn=7, lineLenToWin=4) -> None:
		self._board = []
		self._nbRow = nbRow
		self._nbColumn = nbColumn
		self._lineLenToWin = lineLenToWin
		self.__createBoard()
		pass

	def __repr__(self) -> str:
		string = ""
		for y in range(self._nbRow):
			for x in range(self._nbColumn):
				string += self._board[y][x]
			if y != len(self._nbRow):
				string += "\n"
		return string
	
	def __str__(self) -> str:
		string = ""
		for y in range(self._nbRow):
			for x in range(self._nbColumn):
				string += self._board[y][x]
			if y != self._nbRow - 1:
				string += "\n"
		return string
	
	def resetBoard(self) -> None:
		self.__createBoard()

	def __createBoard(self) -> None:
		self._board = [['0' for i in range(self._nbColumn)] for y in range(self._nbRow)]

	def isColumnFull(self, column) -> bool:
		if self.getDiscColumnRow(column) <= -1:
			return True
		return False

	def addDisc(self, column, discStyle) -> bool:
		print(column)
		if column >= self._nbColumn:
			print("Column doesn't exist", file=sys.stderr)
			return False
		if self.isColumnFull(column):
			print("Column is full", file=sys.stderr)
			return False
		self._board[self.getDiscColumnRow(column)][column] = discStyle
		return True
	
	def getNumberOfDiscInPlay(self, discStyle) -> int:
		discCnt = 0
		for row in self._board:
			discCnt += row.count(discStyle)
		return discCnt

	def areDiscAligned(self, discStyle) -> bool:

		def isAlignedDown(row, column, discStyle) -> bool:
			if row + 3 >= self._nbRow:
				return False
			return (self._board[row][column] == discStyle and
					self._board[row + 1][column] == discStyle and
					self._board[row + 2][column] == discStyle and
					self._board[row + 3][column] == discStyle)

		def isAlignedRight(row, column, discStyle) -> bool:
			if column + 3 >= self._nbColumn:
				return False
			return (self._board[row][column] == discStyle and
					self._board[row][column + 1] == discStyle and
					self._board[row][column + 2] == discStyle and
					self._board[row][column + 3] == discStyle)

		def isAlignedDownRight(row, column, discStyle) -> bool:
			if column + 3 >= self._nbColumn or row + 3 >= self._nbRow:
				return False
			return (self._board[row][column] == discStyle and
					self._board[row + 1][column + 1] == discStyle and
					self._board[row + 2][column + 2] == discStyle and
					self._board[row + 3][column + 3] == discStyle)
		
		def isAlignedUpRight(row, column, discStyle) -> bool:
			if column + 3 >= self._nbColumn or row -3 <= -1:
				return False
			return (self._board[row][column] == discStyle and
					self._board[row - 1][column + 1] == discStyle and
					self._board[row - 2][column + 2] == discStyle and
					self._board[row - 3][column + 3] == discStyle)

		for row in range(self._nbRow):
			for column in range(len(self._board[row])):
				if isAlignedDown(row, column, discStyle):
					return True
				if isAlignedRight(row, column, discStyle):
					return True
				if isAlignedDownRight(row, column, discStyle):
					return True
				if isAlignedUpRight(row, column, discStyle):
					return True
		return False
	
	def haveDiscWinned(self, discsStyle) -> bool:
		for discStyle in discsStyle:
			if self.getNumberOfDiscInPlay(discStyle) < self._lineLenToWin:
				continue
			if self.areDiscAligned(discStyle):
				return True
		return False
		
	def getDiscColumnRow(self, column) -> int:
		actualRow = 0
		for row in self._board:
			if row[column] != '0':
				return actualRow - 1
			actualRow += 1
		return self._nbRow - 1