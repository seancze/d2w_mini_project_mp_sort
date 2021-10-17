

def mergesort(array, byfunc=None):
  
  if len(array) > 1:
    start, end = 0, len(array)
    mid = len(array) // 2
    left = array[start:mid]
    right = array[mid:end]

    i, j, k = 0, 0, 0

    # Sort recursively (I.e. Starting from 2 elements)
    mergesort(left, byfunc=byfunc)

    mergesort(right, byfunc=byfunc)

    # Add to array in-place
    while i < len(left) and j < len(right):
      if byfunc(left[i]) <= byfunc(right[j]):
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      
      k += 1
    
    # Remaining elements
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
    
class Stack:
  def __init__(self):
    self._items = []

  def push(self, item):
    self._items.append(item)

  def pop(self):
    if len(self._items):
      return self._items.pop()

  def peek(self):
    if len(self._items):
      return self._items[-1]
  
  @property
  def is_empty(self):
    return len(self._items) == 0

  @property
  def size(self):
    return len(self._items)

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    valid_num = '0123456789'
    valid_operator = '+-*/()'
    
    def __init__(self, string=""):
        self.expr = string

    @property
    def expression(self):
        return self.expr

    @expression.setter
    def expression(self, new_expr):
        for char in new_expr:
            if char not in EvaluateExpression.valid_char:
                self.expr = ""
                return
        
        self.expr = new_expr

    def insert_space(self):
        s = ""
        for char in self.expr:
            if char in EvaluateExpression.valid_operator:
                s += f" {char} "
            else:
                s += char
        return s
    
    def process_operator(self, operand_stack, operator_stack):
        a = operand_stack.pop()
        operator = operator_stack.pop()        
        b = operand_stack.pop()
        
        if operator == "+":
            ans = b + a
        elif operator == "-":
            ans = b - a
        elif operator == "*":
            ans = b * a
        elif operator == "/":
            ans = b // a
        
        operand_stack.push(ans)

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()

        for el in tokens:
            try:
                # Note: "10.5" will NOT be able to be converted into an int
                my_int = int(el)
                operand_stack.push(my_int)
            except:
                if el == "+" or el == "-":
                    while not operator_stack.is_empty and operator_stack.peek() not in "()":
                        self.process_operator(operand_stack, operator_stack)
                    operator_stack.push(el)
                elif el == "*" or el == "/":
                    while operator_stack.peek() in "*/":
                        self.process_operator(operand_stack, operator_stack)
                    operator_stack.push(el)
                elif el == "(":
                    operator_stack.push(el)
                elif el == ")":
                    while operator_stack.peek() != "(":
                        self.process_operator(operand_stack, operator_stack)
        
        while operator_stack.size > 0:
            if operator_stack.peek() in "()":
                operator_stack.pop()
                continue
            self.process_operator(operand_stack, operator_stack)
            
        return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





