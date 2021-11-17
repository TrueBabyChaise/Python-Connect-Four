#!/usr/bin/env python3

import src.color as clr
from src.IA import IA
from src.player import Player
from src.connectFour import ConnectFour
from src.color import Color_Off
import random

NOCOLOR = False

class Table():

	def __init__(self, nbPlayer = 2, nbRow = 6, nbColumn = 7, lineLenToWin = 4) -> None:
		self.__nbPlayer = 2
		self.__nbRow = 6
		self.__nbColumn = 7
		self.__lineLenToWin = 4
		self.__connectFour = None
		self.__players = []
		random.seed(None)
		self.boardInit()
		self.playerInit()

	def __repr__(self) -> str:
		return "Table you play on :3"

	def __str__(self) -> str:
		string = ""
		tmpTab = [[" " for i in range(self.__nbColumn * 4)] for y in range(self.__nbRow * 4)]
		print(self.__connectFour._board)
		for row in range(len(self.__connectFour._board)):
			for column in range(len(self.__connectFour._board[row])):
				for i in range(4):
					for j in range(4):
						tmpTab[row * 4 + i][column  * 4 + j] = '#' if i == 0 or j == 0 else self.getCaseFormat(self.__connectFour._board[row][column])

		for line in tmpTab:
			for letter in line:
				string += letter
			string += "#\n"
		string += "#" * self.__nbColumn * 4 + "#\n"
		for column in range(self.__connectFour._nbColumn):
			string += f"  {column + 1} "
		string +="\n"
		return string
	
	def getPlayerId(self, discStyle) -> int:
		for player in self.__players:
			if player.discStyle == discStyle:
				return self.__players.index(player)

	def getCaseFormat(self, discStyle) -> str:
		if discStyle == '0':
			return " "
		playerId = self.getPlayerId(discStyle)
		if NOCOLOR:
			return discStyle
		return f"{self.__players[playerId].color}{self.__players[playerId].discStyle}{Color_Off}"

	def boardInit(self) -> None:
		#print("Board Init...")
		self.__connectFour = ConnectFour(self.__nbRow, self.__nbColumn, self.__lineLenToWin)
		#print(self.__connectFour)

	def askPlayerNumber(self) -> None:
		tmp = "a"
		accept = "a"		
		while accept != "yes" and accept != "y" and not tmp.isdigit():
			tmp = input("How many people are gonna play ?\n -> ")
			if not tmp.isdigit():
				continue
			accept = input("Are you sure (y/n) ?\n -> ").lower()
		self.__nbPlayer = int(tmp)

	def playerInit(self) -> None:
		#print("Players Init...")
		self.askPlayerNumber()
		discStyle = ['#', '%', '&', 'X', 'O'] #TMP
		IAName = ["Mizu", "Minato"]
		IAColor = [clr.Red, clr.Blue]
		for i in range(self.__nbPlayer):
			self.__players.append(Player(discStyle[i % len(discStyle)]))
			self.__players[i].askName()
			self.__players[i].askColor()
		while len(self.__players) < 2:
			self.__players.append(IA(discStyle[len(self.__players) % len(discStyle)]))
			self.__players[-1].name = IAName[len(self.__players) - 1]
			self.__players[-1].color = IAColor[len(self.__players) - 1]
		if self.__nbPlayer < 2:
			self.__nbPlayer = 2
		print(*self.__players, sep="\n")

	def getAllDiscStyle(self):
		return [player.discStyle for player in self.__players]

	def run(self) -> None:
		playerTurn = 0

		while not self.__connectFour.haveDiscWinned(self.getAllDiscStyle()):
			correctColumnChoose = False
			if isinstance(self.__players[playerTurn], IA):
				correctColumnChoose = self.__connectFour.addDisc(self.__players[playerTurn].askColumn(self.__connectFour), self.__players[playerTurn].discStyle)
			else:
				while not correctColumnChoose:
					correctColumnChoose = self.__connectFour.addDisc(self.__players[playerTurn].askColumn(), self.__players[playerTurn].discStyle)
			print(self)
			playerTurn = (playerTurn + 1) % self.__nbPlayer

		print(self.__players[playerTurn - 1].name + " win the game !")