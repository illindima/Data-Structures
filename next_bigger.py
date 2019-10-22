def nextBigger(n):
    splitted = [int(i) for i in str(n)]
    
    index_of_replaced_num = -1
    i = len(splitted) - 1

    while i > 0:
      if splitted[i] > splitted[i - 1]:
        index_of_replaced_num = i - 1
        break
      i -= 1
    
    if index_of_replaced_num == -1:
      return -1
    else:
     
      left = splitted[:index_of_replaced_num]
      pivot = splitted[index_of_replaced_num]
      right = splitted[index_of_replaced_num + 1:]
      
      tempSortRight = sorted(right)
      for j in tempSortRight:
        if j > pivot:
          minV = j

      right.remove(minV)
      right.append(pivot)
      right.sort()

      return transform_to_num(left + [minV] + right)

      

def transform_to_num(num_list):
  return int(''.join(map(str,num_list)))
    
    
#Test cases

print(nextBigger(112342))