class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class SuperClass(Queue):
    def isempty(self):
        return len(self.queue) == 0

q = SuperClass()

try:
    for i in range(10):
        q.put(i)

    for i in range(11):
        if not q.isempty():
            print(q.get())
        else:
            print('Empty queue')
except:
    print('U fucked it up')
