class stack:
    def __init__(self):
        self.stack = list()
        self.min = None

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        if self.isEmpty():
            self.min = item
        else:
            if item < self.min:
                self.min = item

        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

    def my_min(self):
        return self.min


if __name__ == '__main__':
    s = stack()
    s.push(5)
    s.push(2)
    s.push(3)
    s.push(1)
    s.push(4)
    print(s.stack)
    # print(s.pop())
    print(f'min: {s.my_min()}')
    # print(s.size())
