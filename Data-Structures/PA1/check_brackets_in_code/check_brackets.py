# python3

import sys

# class Bracket:
#     def __init__(self, bracket_type, position):
#         self.bracket_type = bracket_type
#         self.position = position

#     def Match(self, c):
#         if self.bracket_type == '[' and c == ']':
#             return True
#         if self.bracket_type == '{' and c == '}':
#             return True
#         if self.bracket_type == '(' and c == ')':
#             return True
#         return False

def Match(a, b):
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    if a == '(' and b == ')':
        return True
    return False

if __name__ == "__main__":
    text = sys.stdin.read()
    index = 0
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i,next))
            
        if next == ')' or next == ']' or next == '}':
        # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or not Match(opening_brackets_stack.pop()[1],next):
                index =(i+1)
                print (index) 
                break

    # Printing answer, write your code here
    if len(opening_brackets_stack) == 0 and index==0:
        print('Success')
    elif len(opening_brackets_stack) != 0 and index==0:
        print(opening_brackets_stack.pop()[0]+1)