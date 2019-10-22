def binary_search(input_array, left_side, right_side, value):
  
    if right_side >= left_side:
      middle = int(left_side + (right_side - left_side) / 2)

      if input_array[middle] == value:
        return middle
      elif input_array[middle] > value:
        return binary_search(input_array, left_side, middle - 1, value)
      else:
        return binary_search(input_array, middle + 1, right_side, value)

    else:
      return -1



test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, 0, len(test_list) - 1 ,test_val1))
print(binary_search(test_list, 0, len(test_list) - 1, test_val2))