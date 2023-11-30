class Solution:
    def interpret(self, command: str) -> str:
        val = ""
        char = 0
        while char < len(command):
            if command[char] == "G":
                val += command[char]
                char += 1
            elif command[char: char + 2] == "()":
                val += "o"
                char += 2
            elif command[char: char + 4] == "(al)":
                val += "al"
                char += 4
        return val