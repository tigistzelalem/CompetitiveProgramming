class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * (n+1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ans = []

        while self.pointer <= self.n and self.stream[self.pointer] != None:
            ans.append(self.stream[self.pointer])
            self.pointer += 1
        
        return ans
        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)