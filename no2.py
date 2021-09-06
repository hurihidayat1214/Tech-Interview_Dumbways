def bubbleSort(array):

  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:  

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    if not swapped:
      break

data = [2, 24, 32, 22, 31, 100, 56, 21, 99, 7, 5, 37, 97, 25, 13, 11]


bubbleSort(data)
print(data)

array = [2, 24, 32, 22, 31, 100, 56, 21, 99, 7, 5, 37, 97, 25, 13, 11]

for nilai in array:
    if nilai %  2 == 0:
        print(nilai, " bilangan  genap")
       
    else:
       
        print(nilai, "bilangan ganjil")