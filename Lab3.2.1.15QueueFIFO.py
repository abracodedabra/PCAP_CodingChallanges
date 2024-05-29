class QueueError(Exception):  # Choose base class for the new exception.
     def __init__(self):
        pass



class Queue:
    def __init__(self):
        self.__queListe = []

    def put(self, elem):
        self.__queListe.insert(0, elem)


    def get(self):
        if len(self.__queListe) < 1:
            raise QueueError
        tmp = self.__queListe[-1]
        del self.__queListe[-1]
        return tmp


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
