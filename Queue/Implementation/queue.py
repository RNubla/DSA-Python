class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue('dog')
q.enqueue(True)
q.enqueue('car')
q.enqueue('sims')
print(q.queue)
print(q.peek())
q.dequeue()
print(q.queue)
