import math
import random
import threading
import queue

class QuickSorter():

    tasks = queue.Queue()
    data = []
    key = None

    def sort(self, data, key=None):

        self.data = data
        self.key = key

        self.__quicksort()

        while self.tasks.empty() is False:
            t = self.tasks.get()
            t.run()
            self.tasks.task_done()

        return data

    def __get_value(self, item, key):
        return item if key is None else getattr(item, key)

    def __quicksort(self, lo=0, hi=None):

        if hi is None:
            hi = len(self.data) - 1

        if lo < hi:

            pivot_pos = self.__partition(lo, hi)

            t1 = threading.Thread(target=self.__quicksort, args=[lo, pivot_pos-1])
            t2 = threading.Thread(target=self.__quicksort, args=[pivot_pos+1, hi])

            self.tasks.put(t1)
            self.tasks.put(t2)
            
    def __partition(self, lo, hi):
        
        pivot_index =  math.floor((lo + hi)/2)

        self.data[hi], self.data[pivot_index] = self.data[pivot_index], self.data[hi]
        pivot = self.data[hi]
        j = i = lo
        
        for j in range(hi - 1, lo - 1, -1):
            
            if self.__get_value(self.data[j], self.key) < self.__get_value(pivot, self.key):

                while self.__get_value(self.data[i], self.key) < self.__get_value(pivot, self.key):
                    if i > j:
                        break

                    i += 1

                if i < j:
                    self.data[i], self.data[j] = self.data[j], self.data[i]

        
        self.data[i], self.data[hi] = self.data[hi], self.data[i]
        return i
