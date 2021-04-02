left = ["[", "{", "(" ]
right = ["]", "}", ")" ]

def bracket_matcher(input):
    stack =[]

    for i in input:
        if i in left:
            stack.append(i)
        elif i in right:
            position = right.index(i)

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
# returns true

print(bracket_matcher('a[b]c(123'))
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