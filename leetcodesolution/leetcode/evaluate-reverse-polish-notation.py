class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif char == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            
            elif char == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)

            elif char == "/":
                num1 = stack.pop()
                num2 = stack.pop()

                if num1 > 0 and num2 < 0 and num2 % num1 != 0:
                    stack.append(num2 // num1 + 1)
                elif num1 < 0 and num2 > 0 and num2 % num1 != 0:
                    stack.append(num2 // num1 + 1)
                else:
                    stack.append(num2 // num1)
            else:
                stack.append(int(char))
        
        return stack[-1]
            
        

        