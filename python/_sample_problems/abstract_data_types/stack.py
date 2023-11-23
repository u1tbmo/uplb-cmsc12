class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)


function_stack = Stack()
function_stack.push("main")
function_stack.push("add")
function_stack.push("subtract")
function_stack.push("multiply")
function_stack.push("divide")
function_stack.push("square")

print(function_stack.items)
print(function_stack.pop())

print(function_stack.items)
print(function_stack.pop())

print(function_stack.items)
print(function_stack.pop())
