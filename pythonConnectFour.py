#!/usr/bin/env python3

from src.table import Table
import signal

def signal_handler(sig, frame):
	print("Ctrl-C")
	exit(0)

def main():
	signal.signal(signal.SIGINT, signal_handler)
	table = Table()
	table.run()

if __name__ == '__main__':
	main()