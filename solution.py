
class Stack:
  def __init__(self):
      self.data = []

  def isEmpty(self):
      """Returns True if Stack is empty, False otherwise"""
      return self.data == []

  def push(self, item):
      """Adds an item to the top of stack"""
      return self.data.append(item)

  def pop(self):
      """Removes the item from the top of stack. Returns the removed item"""
      if len(self.data) > 0:
        return self.data.pop()
      else:
        return None

  def peek(self):
      """Returns the top item in the stack, but doesn't remove it"""
      if len(self.data) > 0:
        return self.data[len(self.data)-1]
      else:
        return None

  def size(self):
      """Returns the (int) size of the stack"""
      return len(self.data)

  def __str__(self):
      """Returns a string representation of all items in stack"""
      string = self.data.copy()
      return str(string)

my_stack = Stack()

def bracket_matcher(input):
  global my_stack
  listed_string = list(input)
  # bracket_list = []
  for letters in listed_string:
    if(letters == '(' or letters == '[' or letters == '{'):
      my_stack.push(letters)
      # print(my_stack.peek())
    if(letters == ']' and my_stack.peek() == '['):
      print('This Code Works')
      return True
    # else:
    #   print('Missing or misplaced brackets')
    #   return False
    if(letters == '}' and my_stack.peek() == '{'):
      print('This Code Works')
      return True
    # else:
    #   print('Missing or misplaced brackets')
    #   return False
    if(letters == ')' and my_stack.peek() == '('):
      print('This Code Works')
      return True
    # else:
    #   print('Missing or misplaced brackets')
    #   return False
    
 
bracket_matcher('a[b]c(123')

# print(my_stack.peek())
print(my_stack.peek() + " this is the bottom peek check")
print(my_stack.__str__)