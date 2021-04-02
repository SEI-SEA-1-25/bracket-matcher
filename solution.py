left = ["[", "{", "(" ]
right = ["]", "}", ")" ]

def bracket_matcher(input):
    stack =[]

    for i in input:
        if i in left:
            stack.append(i) # runs through the loop and checks the left sides first "( { [" and if it has it, then it will add it to my empty array
        elif i in right:
            position = right.index(i) # index returns the position of specified value

            # stack should be greater than 0, so check left(2) to see if it has a matching brace, if it does pop it off
            if ((len(stack) > 0) and (left[position] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


# Testing function

print(bracket_matcher('abc(123)'))
# func will run through and check "(" to see if it has matchng ")"
# returns true

print(bracket_matcher('a[b]c(123'))
# there is no matching ")" in the string 
# returns false -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns true

print(bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print(bracket_matcher('()'))
# returns true

print(bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched