def selectionSort(lst):
  if len(lst)== 1:
    return lst
  else:
    x1 = lst[0]
    x = 0
    for i in range(len(lst)):
      if x1>lst[i]:
        x1=lst[i]
        x = i
    del lst[x]
    return [x1] + selectionSort(lst)

print(selectionSort([4,3,1,2,-1,-4,5,7,8]))

