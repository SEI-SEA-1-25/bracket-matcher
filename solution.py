# Ian's homework
# Bracket matcher

open_brackets = ["[","{","("]
closed_brackets = ["]","}",")"]
  

def bracket_matcher(input_str):
    stack = []
    for i in input_str:
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            pos = closed_brackets.index(i)
            if ((len(stack) > 0) and
                (open_brackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "bad code"
    if len(stack) == 0:
        return "Nice code!"
    else:
        return "bad code"
  
  
print(bracket_matcher('a[b]c(123'))

print(bracket_matcher('a[bc(123)]'))
# # returns true
#
print(bracket_matcher('a[bc(12]3)'))
# # returns false -- improperly nested

print(bracket_matcher(''))
# # returns true

print(bracket_matcher('a{b}{c(1}[2]3)'))
# # returns false -- improperly nested




# string = "abc(123)"
# print(string,"-", bracket_matcher(string))
  
# string = "a[b]c(123"
# print(string,"-", bracket_matcher(string))
  
# string = "a{b}{c(1[2]3)}"
# print(string,"-",bracket_matcher(string))