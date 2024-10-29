class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        while len(self.st1) > 1:
            self.st2.append(self.st1.pop())
        val = self.st1.pop()
        while self.st2:
            self.st1.append(self.st2.pop())
        return val
        

    def peek(self):
        """
        :rtype: int
        """
        while len(self.st1) > 1:
            self.st2.append(self.st1.pop())
        val = self.st1[-1]
        while self.st2:
            self.st1.append(self.st2.pop())
        return val
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.st1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()