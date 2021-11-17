from typing import overload
from src.player import Player
from src.connectFour import ConnectFour as cr
import random

def override(func):
	"""
	Simple decorator to know if I'm overwriting a function from the parent
	"""
	return func

class IA(Player):

	def __init__(self, discStyle) -> None:
		super().__init__(discStyle)
		self._name = ""
		self._color = None

	def __repr__(self) -> str:
		return super().__repr__()

	def __str__(self) -> str:
		return super().__str__()

	@property
	def name(self) -> str:
		return self._name

	@property
	def discStyle(self) -> str:
		return super().discStyle

	@property
	def color(self) -> str:
		return self._color

	@color.setter
	def color(self, value):
		self._color = value

	@name.setter
	def name(self, value):
		self._name = value

	@override
	def askColor(self) -> str:
		return super().askColor()
	
	@override
	def askName(self) -> str:
		return super().askName()

	def getBestMove(self, connectFour) -> int:

		def getDownAlignedCaseCount(row, column, board):
			if len(board) <= row:
				print("Down Skipped", end=" ")
				return 0
			cnt = 0
			for newRow in board[row:]:
				if newRow[column] != self.discStyle:
					break
				cnt += 1
			print(cnt, "Down", end=" ")
			return cnt
		
		def getRightAlignedCaseCount(row, column, board):
			cnt = 0
			for case in board[row][column:]:
				if case != self.discStyle:
					break
				cnt += 1
			print(cnt, "Right", end=" ")
			return cnt
		
		def getLeftAlignedCaseCount(row, column, board):
			cnt = 0
			if len(board[row][:column]) == 0:
				return 0
			tmp = board[row][:column].copy()
			tmp.reverse()
			for case in tmp:
				if case != self.discStyle:
					break
				cnt += 1
			print(cnt, "Left", end=" ")
			return cnt
		
		def getLeftDownAlignedCaseCount(row, column, board):
			if len(board) <= row:
				print('LeftDown Skipped', end=" ")
				return 0
			cnt = 0
			for newRow in range(row, len(board[row:])):
				for newColumn in range(len(board[newRow][:column]), -1, -1):
					if board[newRow][newColumn] != self.discStyle:
						print(cnt, "LeftDown", end=" ")
						return cnt
					cnt += 1
			print(cnt, "LeftDown", end=" ")
			return cnt

		def getRightDownAlignedCaseCount(row, column, board):
			if len(board) <= row:
				print('RightDown Skipped', end=" ")
				return 0
			cnt = 0
			for newRow in range(row, len(board[row:])):
				for newColumn in range(column, len(board[newRow][column:])):
					if board[newRow][newColumn] != self.discStyle:
						print(cnt, "RightDown", end=" ")
						return cnt
					cnt += 1
			print(cnt, "RightDown", end=" ")
			return cnt

		def getMaxAlignedCase(row, column, board):
			max = getDownAlignedCaseCount(row + 1, column, board)
			tmp = getLeftAlignedCaseCount(row, column, board)
			tmp += getRightAlignedCaseCount(row, column + 1, board)
			if tmp > max:
				max = tmp
			tmp = getLeftDownAlignedCaseCount(row + 1, column, board)
			if tmp > max:
				max = tmp
			tmp = getRightDownAlignedCaseCount(row + 1, column, board)
			if tmp > max:
				max = tmp
			return max

		max = 0
		posColumn = random.randint(0, connectFour._nbColumn)
		for column in range(connectFour._nbColumn):
			print("Column :", column)
			tmp = getMaxAlignedCase(connectFour.getDiscColumnRow(column), column, connectFour._board)
			if tmp > max:
				max = tmp
				posColumn = column
			print()
		return posColumn

	@override
	def askColumn(self, connectFour) -> int:
		return self.getBestMove(connectFour)