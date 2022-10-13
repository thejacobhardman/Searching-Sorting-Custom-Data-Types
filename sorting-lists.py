# Jacob Hardman
# CS 301
# Dr. Nathaniel Miller
# 3/30/22

# Insertion Sort 
# Worst Cast Runtime: O(n^2) due to while loop nested inside of for loop.
def insertion_sort(unsorted_list):
    sorted_list = []

    for item in unsorted_list:
        i = 0
        item_placed = False
        while i <= len(sorted_list) and item_placed == False:
            if len(sorted_list) == 0:
                sorted_list.append(item)
                item_placed = True
            if i == len(sorted_list):
                sorted_list.append(item)
                item_placed = True
            if item < sorted_list[i]:
                sorted_list.insert(i, item)
                item_placed = True
            i += 1

    return sorted_list

# Bubble Sort 
# Worst Cast Runtime: O(n^2) due to nested while loops.
def bubble_sort(list_to_sort):
    list_sorted = False
    while not list_sorted:
        list_altered = False
        i = 0
        while i <= len(list_to_sort):
            if i == len(list_to_sort)-1:
                break
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
                list_altered = True
            i += 1
        if list_altered == False:
            list_sorted = True
    
    return list_to_sort

# Selection Sort
# Worst Case Runtime: O(n^2) due to nested while loops
def selection_sort(list_to_sort):
    i = len(list_to_sort)-1
    while i >= 0:
        j = 0
        max_value = 0
        max_value_index = 0
        while j <= i:
            if list_to_sort[j] > max_value:
                max_value = list_to_sort[j]
                max_value_index = j
            j += 1
        if list_to_sort[i] != max_value:
            list_to_sort[i], list_to_sort[max_value_index] = list_to_sort[max_value_index], list_to_sort[i]
        i -= 1

    return list_to_sort

# Merge Sort - Total Worst Cast Runtime: O(nk)
# Worst Case Runtime: O(n) due to while loop
def merge(list1, list2):
    merged_list = []

    index1 = 0
    index2 = 0
    total_length = len(list1) + len(list2)

    while len(merged_list) != total_length: 
        if index1 >= len(list1):
            merged_list.append(list2[index2])
            index2 += 1
        elif index2 >= len(list2):
            merged_list.append(list1[index1])
            index1 += 1
        elif list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

    return merged_list

# Worst Case Runtime: O(k) due to list slicing
def merge_sort(list_to_sort):
    if len(list_to_sort) == 1:
        return list_to_sort

    midpoint = len(list_to_sort)//2
    list1 = list_to_sort[:midpoint]
    list2 = list_to_sort[midpoint:]

    list1 = merge_sort(list1)
    list2 = merge_sort(list2)

    return merge(list1, list2)

# Testing Code
list_to_sort = [5, 8, 3, 4, 9, 10, 2, 1, 7, 6]

print("Testing functions with: " + str(list_to_sort))

print("\nInsertion Sort: " + str(insertion_sort(list_to_sort)))
print("\nBubble Sort: " + str(bubble_sort(list_to_sort)))
print("\nSelection Sort: " + str(selection_sort(list_to_sort)))
print("\nMerge Sort: " + str(merge_sort(list_to_sort)))
