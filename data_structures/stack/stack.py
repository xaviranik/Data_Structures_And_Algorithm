class Stack:
    def __init__(self):
        self.item = []

    def __len__(self):
        return len(self.item)

    def top(self):
        if len(self.item) >= 1:
            print(self.item[len(self.item) - 1])
        else:
            print("Empty Stack")

    def pop(self):
        if len(self.item) >= 1:
            self.item.pop()
        else:
            raise IndexError

    def push(self, item):
        self.item.append(item)
        print(self.item)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.push(4)
