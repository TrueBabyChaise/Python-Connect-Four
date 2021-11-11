#!/usr/bin/env python3

from src.player import Player
from src.connectFour import ConnectFour

class Table():

	def __init__(self) -> None:
		self.__nbPlayer = 2
		self.__nbRow = 6
		self.__nbColumn = 7
		self.__lineLenToWin = 4
		self.__connectFour = None
		self.__players = []
		self.boardInit()
		self.playerInit()

	def boardInit(self):
		print("Board Init...")
		self.__connectFour = ConnectFour()
		print(self.__connectFour)

	def playerInit(self):
		print("Players Init...")
		discStyle = ['#', '%', '&', 'X', 'O'] #TMP
		names  = ["Rose", "Violette", "Jonquille", "Pétunia", "Tulipe"] #TMP
		for i in range(self.__nbPlayer):
			self.__players.append(Player(discStyle[i]))
			self.__players[i].name = names[i]
			print(self.__players[i])

	def getAllDiscStyle(self):
		return [player.discStyle for player in self.__players]

	def run(self):
		playerTurn = 0

		while not self.__connectFour.haveDiscWinned(self.getAllDiscStyle()):
			correctColumnChoose = False
			while not correctColumnChoose:
				correctColumnChoose = self.__connectFour.addDisc(self.__players[playerTurn].askColumn(), self.__players[playerTurn].discStyle)
			print(self.__connectFour)
			playerTurn = (playerTurn + 1) % self.__nbPlayer
		print("End")