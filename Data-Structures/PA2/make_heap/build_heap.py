# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    # for i in range(len(self._data)):
    # for j in range(i + 1, len(self._data)):
    #   if self._data[i] > self._data[j]:
    #     self._swaps.append((i, j))
    #     self._data[i], self._data[j] = self._data[j], self._data[i]
    # TODO: replace by a more efficient implementation
    length  = len(self._data)-1
    i = length//2
    for i in range(i,-1,-1):
      self.convert(i,length)
 
  def convert(self,i,length):
    biggest = (i*2)+1
    while length>=biggest:
      if biggest<length and self._data[biggest]>self._data[biggest+1]:
        biggest+=1
      if self._data[i]>self._data[biggest]:
        self._swaps.append([i,biggest])
        self._data[i],self._data[biggest]=self._data[biggest],self._data[i]
        i = biggest
        biggest = (i*2)+1
      else:
        break   

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
