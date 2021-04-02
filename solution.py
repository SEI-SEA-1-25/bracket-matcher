
open_br= ["[","{","("]
close_br = ["]","}",")"]

def bracket_matcher(input):
  bracket_match = []
  for bracket in input:
    if bracket in open_br :
      bracket_match.append(bracket)
    elif bracket in close_br :
      bracket_match.pop(bracket)
    else:
      return False


string = "abc(123)"
print(string,"-", bracket_matcher(string))

string = "a[b]c(123"
print(string,"-", bracket_matcher(string))

string = "a{b}{c(1[2]3)}"
print(string,"-",bracket_matcher(string))