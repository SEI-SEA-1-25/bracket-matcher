def bracket_matcher(input):
    stack = []
    for ch in input: # 'abc(123)', '()) ()() ([ ])  []
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        elif ch == ")" or ch == "]" or ch == "}":
            if stack == []:
                return False
            last_ch = stack.pop() # -> stack =[]  /  last_ch = "("
            if last_ch != "(":
                return False
    return True

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
# returns false - no opening print(bracket to correspond with last character)

print(bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched