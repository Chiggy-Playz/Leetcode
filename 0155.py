class MinStack:

    def __init__(self):
        self.l = []
        self.min = []

    def push(self, val: int) -> None:
        self.l.append(val)
        self.min_add(val)
        print(self.min)
    
    def min_add(self, val):
        if not self.min:
            self.min = [val]
            return
        
        high = len(self.min) - 1
        low = 0
        mid = (high + low) // 2
        while low < high:
            if val < self.min[mid]:
                high = mid
                mid = (high + low) // 2
            elif self.min[mid] < val:
                low = mid + 1
                mid = (high + low) // 2
            elif self.min[mid] == val:
                break
        
        self.min.insert(mid + int(self.min[mid] < val), val)

    def pop(self) -> None:
        self.min.remove(self.l[-1])
        self.l.pop()

    def top(self) -> int:
        return self.l[-1] 

    def getMin(self) -> int:
        return self.min[0]


obj = MinStack()
obj.push(-2)
obj.push(-5)
obj.push(-6)
obj.push(2)
obj.push(1)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
