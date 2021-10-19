class findvalue:
      def __init__(self,array,element):
            self.array = array
            self.element = element
            self.start = 0
            self.end = len(array)
      def search(self):
            step = 0
            while(self.start <= self.end):
               print("Sub array in step {}: {}".format(step, str(self.array[self.start:self.end+1])))
               step = step + 1
               mid = (self.start + self.end)//2

               if self.array[mid] == self.element:
                   return mid

               if self.element < self.array[mid]:
                   self.end = mid - 1

               else:
                   self.start = mid + 1
            return -1        

array = [1,4,5,9,10,20,10,42,44,55,100]
find = 100
search = findvalue(array,find)
  
print('Search array : {} in Array : {}'.format(array,search.element))
print("Index of {}".format(search.search()))