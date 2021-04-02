class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        """Returns True if Stack is empty, False otherwise"""
        return len(self.data) == 0

    def push(self, item):
        """Adds an item to the top of stack"""
        self.data.append(item)

    def pop(self):
        """Removes the item from the top of stack. Returns the removed item"""
        popped_item = self.data.pop()
        return popped_item

    def peek(self):
        """Returns the top item in the stack, but doesn't remove it"""
        return self.data[-1]

    def size(self):
        """Returns the (int) size of the stack"""
        return len(self.data)

    def __str__(self):
        """Returns a string representation of all items in stack"""
        data_string = ' '.join(self.data)
        return f'{data_string}'


def bracket_matcher(user_input):
  # bracket_stack = Stack()
  bracket_stack = []
  for bracket in user_input:
    if bracket in '({[':
      bracket_stack.push(bracket)
    elif bracket in ')}]':
      if bracket == bracket_stack[0]:
        bracket_stack.pop(bracket)
      else:
        return False
    else:
      return True


# loop over the input, look for brackets
# if it's an open bracket, we push it onto the stack
# if it's a closed bracket, we match it against the first stack item
# if false, return false
# if it matches, pop it out of stack/list/array



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