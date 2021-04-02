# class Stack:
#     def __init__(self):
#         self.data = []

#     def isEmpty(self):
#         """Returns True if Stack is empty, False otherwise"""
#         return len(self.data) == 0

#     def push(self, item):
#         """Adds an item to the top of stack"""
#         self.data.append(item)
#         print(self.data)

#     def pop(self):
#         """Removes the item from the top of stack. Returns the removed item"""
#         return self.data.pop()

#     def peek(self):
#         """Returns the top item in the stack, but doesn't remove it"""
#         return self.data[len(self.data)-1]
#         # henry's way
#         # return self.data[-1]

#     def size(self):
#         """Returns the (int) size of the stack"""
#         return len(self.data)

#     def __str__(self):
#         """Returns a string representation of all items in stack"""
        
#         # for item in self.data:
#             # print( f'{item}')
#             # print(str(item))
#         new_string = ""
#         for i in range(len(self.data)):
#             new_string += self.data[i] + " "
#         return new_string
#         # henry's way
#         # stack_string = ""
#         # for i in self.data:
#         #     stack_string += i + ""
#         # return stack_string

# # [, ], {, }, (, )

# left = ["[", "{", "(" ]
# right = ["]", "}", ")" ]

# def bracket_matcher(input):
#     student_input = Stack()
#     for item in input:
#         if item in left:
#             student_input.push(item)
#         elif item in right:
#             position = right.index(item)
#             if((student_input.size() > 0) and (left[position] == student_input[student_input.size() -1 ])):
#                 student_input.pop()
#             else: 
#                 return False
#     if student_input.size() == 0:
#         return True
#     else: 
#         return False
    

left = ["[", "{", "(" ]
right = ["]", "}", ")" ]

def bracket_matcher(input):
    student_input =[]

    for item in input:
        if item in left:
            student_input.append(item)
        elif item in right:
            position = right.index(item)

            if ((len(student_input) > 0) and (left[position] == student_input[len(student_input) - 1])):
                student_input.pop()
            else:
                return False

    if len(student_input) == 0:
        return True
    else:
        return False


string = ('abc(123)')
# returns true
print(string,"-", bracket_matcher(string))

string = ('a[b]c(123')
# returns false -- missing closing parens
print(string,"-", bracket_matcher(string))

string = ('a[bc(123)]')
# returns true
print(string,"-",bracket_matcher(string))

string = ('a[bc(12]3)')
# returns false -- improperly nested
print(string,"-",bracket_matcher(string))

string = ('a{b}{c(1[2]3)}')
# returns true
print(string,"-",bracket_matcher(string))

string = ('a{b}{c(1}[2]3)')
# returns false -- improperly nested
print(string,"-",bracket_matcher(string))

string = ('()')
# returns true
print(string,"-",bracket_matcher(string))

string = ('[]]')
# returns false - no opening bracket to correspond with last character
print(string,"-",bracket_matcher(string))

string = ('abc123yay')
# returns true -- no brackets = correctly matched
print(string,"-",bracket_matcher(string))