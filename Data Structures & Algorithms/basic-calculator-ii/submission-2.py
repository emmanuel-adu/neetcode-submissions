import re

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        tokens = re.findall(r"\d+|[+\-*/]", s)
        print(tokens)

        for token in tokens:
            if token.isdigit():
                num = int(token)

                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    a = stack.pop()
                    stack.append(a * num)
                elif op == "/":
                    a = stack.pop()
                    stack.append(int(a / num))
            else:
                op = token


        print(stack)
        return sum(stack)

                
        