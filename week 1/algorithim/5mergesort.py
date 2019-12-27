import sys
sys.path.append('/home/user/Desktop/task/week 1/utility')

from utility import Merge_Sort
llist = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(llist)  # here unsorted list is printed
Merge_Sort(llist)  # her list is sorted using merge sort
print(llist)  # now sorted list is printed