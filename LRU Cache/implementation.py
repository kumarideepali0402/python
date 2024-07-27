class LRU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.data={}
        self.keyList=DLL()
        self.keyMap={}