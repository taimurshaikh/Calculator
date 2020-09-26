# List of priorities of each operation (except closing bracket) to dicate order of precedence
priorities = {"(": 0, "/": 2, "*": 2, "+": 1, "-": 1}

class Calculator:

    def isOperand(self, op):
    """ Checks whether element is operand """
        try:
            op = int(op)
        except ValueError:
            return False
        return True

    def convert(self, string):
    """ Convert the standard (infix) expression to Reverse Polish (postfix) notation"""

        # This array will implement a stack data structure
        stack = []

        # Postfix output
        postfix = ""

        for obj in string.split(" "):

            # If it's a number, directly add to output
            if self.isOperand(obj):
                postfix += obj

            else:
                # We can directly push an opening bracket to the stack
                if not stack or obj ==  "(":
                    stack.append(obj)

                # For closing bracket, pop everything that comes after the preceding opening bracket and add it to the output
                elif obj == ")":

                    while stack[-1] != "(":
                        postfix += stack.pop()

                    # Discard opening bracket
                    stack.pop()

                else:
                    # For any other incoming operator, keep checking if stack is empty and priority of incoming operator is
                    # less than or equal to priority of operator at top of stack

                    while stack and priorities[obj] <= priorities[stack[-1]]:
                        # Add all the higher priority operators to the output
                        postfix += stack.pop()

                    # Only after incoming operator has higher priority can we push it to the stack
                    stack.append(obj)

        # Add the last operator to the output
        if stack:
            postfix += stack.pop()
        return postfix

    def evaluate(self, string):
        """ Evaluates postfix expression """
        expression = self.convert(string)
        stack = []

        for op in expression:
            # Directly push any operands onto stack
            if self.isOperand(op):
                stack.append(op)

            else:
                # Push two operands from stack
                op1 = stack.pop()
                op2 = stack.pop()

                # Depending on which operator the current object in the expression is, perform that operation on the 2 popped operands and push the result
                if op == "+":
                    stack.append(int(op2) + int(op1))
                elif op == "-":
                    stack.append(int(op2) - int(op1))
                elif op == "*":
                    stack.append(int(op2) * int(op1))
                elif op == "/":
                    stack.append(int(op2) / int(op1))

        # The only item left in the stack is the result of the expression
        return stack[0]

calc = Calculator()
res = calc.evaluate("( 4 * ( 3 - ( 5 * 2 ) ) )")
print(res) # ==> -28
