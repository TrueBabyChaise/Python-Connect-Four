#!/usr/bin/env python3

from src.player import Player
from src.connectFour import ConnectFour
from src.color import Color_Off

class Table():

	def __init__(self, nbPlayer = 2, nbRow = 6, nbColumn = 7, lineLenToWin = 4) -> None:
		self.__nbPlayer = 2
		self.__nbRow = 6
		self.__nbColumn = 7
		self.__lineLenToWin = 4
		self.__connectFour = None
		self.__players = []
		self.boardInit()
		self.playerInit()

	def __repr__(self) -> str:
		return "Table you play on :3"

	def __str__(self) -> str:
		string = ""
		tmpTab = [[" " for i in range(self.__nbColumn * 4)] for y in range(self.__nbRow * 4)]
		for row in range(len(self.__connectFour._board)):
			for column in range(len(self.__connectFour._board[row])):
				### TMP
				tmpTab[row * 4][column  * 4] = "#"
				tmpTab[row * 4][column * 4 + 1] = "#"
				tmpTab[row * 4][column * 4 + 2] = "#"
				tmpTab[row * 4][column * 4 + 3] = "#"
				tmpTab[row * 4 + 1][column * 4] = "#"
				tmpTab[row * 4 + 1][column * 4 + 1] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 1][column * 4 + 2] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 1][column * 4 + 3] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 2][column * 4] = "#"
				tmpTab[row * 4 + 2][column * 4 + 1] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 2][column * 4 + 2] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 2][column * 4 + 3] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 3][column * 4] = "#"
				tmpTab[row * 4 + 3][column * 4 + 1] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 3][column * 4 + 2] = self.getCaseFormat(self.__connectFour._board[row][column])
				tmpTab[row * 4 + 3][column * 4 + 3] = self.getCaseFormat(self.__connectFour._board[row][column])
				###

		for line in tmpTab:
			for letter in line:
				string += letter
			string += "#\n"
		string += "#" * self.__nbColumn * 4 + "#\n"
		return string
	
	def getPlayerId(self, discStyle) -> int:
		for player in self.__players:
			if player.discStyle == discStyle:
				return self.__players.index(player)

	def getCaseFormat(self, discStyle) -> str:
		if discStyle == '0':
			return " "
		playerId = self.getPlayerId(discStyle)
		return f"{self.__players[playerId].color}{self.__players[playerId].discStyle}{Color_Off}"

	def boardInit(self) -> None:
		#print("Board Init...")
		self.__connectFour = ConnectFour(self.__nbRow, self.__nbColumn, self.__lineLenToWin)
		#print(self.__connectFour)

	def playerInit(self) -> None:
		#print("Players Init...")
		discStyle = ['#', '%', '&', 'X', 'O'] #TMP
		for i in range(self.__nbPlayer):
			self.__players.append(Player(discStyle[i % len(discStyle)]))
			self.__players[i].askName()
			self.__players[i].askColor()
			print(self.__players[i])

	def getAllDiscStyle(self) -> list[str]:
		return [player.discStyle for player in self.__players]

	def run(self) -> None:
		playerTurn = 0

		while not self.__connectFour.haveDiscWinned(self.getAllDiscStyle()):
			correctColumnChoose = False
			while not correctColumnChoose:
				correctColumnChoose = self.__connectFour.addDisc(self.__players[playerTurn].askColumn(), self.__players[playerTurn].discStyle)
			print(self)
			playerTurn = (playerTurn + 1) % self.__nbPlayer

		print(self.__players[playerTurn - 1].name + " win the game !")