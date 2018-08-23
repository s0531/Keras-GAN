#!/usr/bin/python3
# coding: utf-8

class Gan():
	def __init__(self):
		self.height = 28
		self.width = 19
		self.a = 2

	def getHeight(self):
		print('height: %d' % self.height)

	
	def getWidth(self):
		print('width: %d' % self.width)

if __name__ == '__main__':
	gan = Gan()
	gan.getWidth()
	gan.getHeight()

