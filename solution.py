maxDepth = 12 ## no more than 12 recursions, ok!
def bracket_matcher(inputString, currentDepth = 1):
    global maxDepth
    #strip input of non-paren/curly/bracket characters
    if(currentDepth ==maxDepth):
        raise Exception("Max depth exceeded!!!!!!")
    if(currentDepth == 1):
        print(f'Initial String is {inputString}')
    processedString = ""
    for character in inputString:
        if(character in '{}[]()'):
            processedString += character

    # base case -- if empty, True!
    if(len(processedString)==0):
        return True
    firstChar=processedString[0]
    # False if begins with closing bracket
    if(firstChar in '}])'):
        print(f"{firstChar} is not matched")

        return False
    
    ## Now we split the string into substrings to perform recursion
    elif(firstChar == '{'):
        endingIndex = processedString.find('}')
    elif(firstChar == '['):
        endingIndex = processedString.find(']')
    elif(firstChar == '('):
        endingIndex = processedString.find(')')
    else:
        raise Exception("This is unexpected")

    if(endingIndex == -1):

        print(f"{firstChar} is not matched")

        return False

    substring1 = processedString[1:endingIndex]
    substring2 = processedString[endingIndex+1::]

    # print(f'substring 1 found to be {substring1}')
    # print(f'substring 2 found to be {substring2}')
    return_value= bracket_matcher(substring1, currentDepth + 1) and bracket_matcher(substring2, currentDepth + 1)
    if(currentDepth == 1):
        print(return_value)
    return return_value

bracket_matcher('abc(123)')
# returns true

bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

bracket_matcher('a[bc(123)]')
# returns true

bracket_matcher('a[bc(12]3)')
# returns false -- improperly nested

bracket_matcher('a{b}{c(1[2]3)}')
# returns true

bracket_matcher('a{b}{c(1}[2]3)')
# returns false -- improperly nested

bracket_matcher('()')
# returns true

bracket_matcher('[]]')
# returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched