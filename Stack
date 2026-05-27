#stack = last in first out (LIFO)

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()#deque is a double-ended queue that allows for efficient appending and popping from both ends. It is used here to implement the stack data structure, providing O(1) time complexity for push and pop operations.

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage1:
# def reverse_string(text):
#     stack = Stack()
#     for char in text:
#         stack.push(char)
            
#     reversed_text = ""
#     while not stack.is_empty():
#             reversed_text = reversed_text + stack.pop()
#     return reversed_text
        

# s = Stack()
# s.push("We ")
# s.push("will")
# s.push("conquere")
# s.push("COVID-19")

# print(reverse_string("We will conquere COVID-19"))


# Example usage2:

# def is_balanced (text):
#     stack = Stack()
#     pairs = { ')': '(', '}': '{', ']': '[' }    
    
#     for char in text:
#         if char in pairs.values():
#             stack.push(char)
            
#         elif char in pairs.keys():
#             if stack.is_empty() or stack.pop() != pairs[char]:
#                 return False
#     return stack.is_empty()

# print(is_balanced("({a+b})"))     
# print(is_balanced("))((a+b}{"))   
# print(is_balanced("((a+b))"))     
# print(is_balanced("))"))        
# print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) 

