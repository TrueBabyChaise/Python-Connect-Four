#!/usr/bin/env python3

from src.connectFour import ConnectFour

def main():
	cF = ConnectFour()
	print(cF)
	while cF.addDisc(4):
		print(cF)
	print(cF)

if __name__ == '__main__':
	main()