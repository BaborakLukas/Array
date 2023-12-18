x = [85859,64230,56940,80691,70077,13959,23673,80213,4184,25484]

def bubbleSort(array):
    
  
  for i in range(len(array)):

    
    for j in range(0, len(array) - i - 1):

      
      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
data = x

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)