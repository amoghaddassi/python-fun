"""Converts prefix notation to postfix notation for arithmetic expressions."""
class Stack:
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()

def pre_to_post(pre):
	stk = Stack()
	operators = ['+', '-', '*', '/']
	for char in pre[::-1]:
		if char in operators:
			op1 = stk.pop()
			op2 = stk.pop()
			stk.push(str(op2) + str(op1) + char)
		else:
			stk.push(char)
	return stk.pop()	
