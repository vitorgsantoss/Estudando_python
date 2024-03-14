from _collections_abc import Sequence

class My_list(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self,value):
        self._data[self._index]=value
        self._index+=1

    def __getitem__(self, value):
        return self[value]
    
    def __next__(self):
     
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value =  self._data[self._next_index]
        self._next_index+=1
        return value
    
    def __len__(self):
        return self._index
    
    def __iter__(self):
        return self
    


    
lista = My_list()
lista.append('Vítor')
lista.append('Gabriel')
lista.append('Santos')
# print(lista._data[0])
# print(len(lista))
for item in lista:
    print(item)
