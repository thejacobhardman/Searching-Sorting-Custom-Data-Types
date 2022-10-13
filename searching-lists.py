# Jacob Hardman
# CS 301
# Dr. Nathaniel Miller
# 3/27/2022

def search_sorted_list(sorted_list, item, start_index=0, last_index=0):
    if last_index == 0: 
        last_index = len(sorted_list) - 1
    if start_index > last_index:
        return False
    midpoint = (start_index + last_index) // 2
    if sorted_list[midpoint] == item:
        return True
    else:
        if item < sorted_list[midpoint]:
            last_index = midpoint - 1
            return search_sorted_list(sorted_list, item, start_index, last_index)
        else:
            start_index = midpoint + 1
            return search_sorted_list(sorted_list, item, start_index, last_index)

class HashList:
    # Running Time: O(1)
    def __init__(self, length):
        self.length = length
        self.data = [None] * self.length

    # Running Time: O(1)
    def hashfunction(self, item):
        return item % self.length

    # Running Time: O(1)
    def new_hash(self, old_hash):
        return (old_hash + 1) % self.length

    # Best Case Running Time: O(1)
    # Worst Case Running Time: O(N)
    def put(self, item):
        data_added = False
        hash_value = self.hashfunction(item)
        if self.data[hash_value] == None:
            self.data[hash_value] = item
            data_added = True
        else:
            next_slot = self.new_hash(hash_value)
            while data_added == False:
                if next_slot == self.length:
                    next_slot = 0
                if next_slot == hash_value:
                    break
                if self.data[next_slot] == None:
                    self.data[next_slot] = item
                    data_added = True
                next_slot = self.new_hash(next_slot)
        if data_added == False:
            print("ERROR - List is currently full.")

    # Best Case Running Time: O(1)
    # Worst Case Running Time: O(N)
    def contains(self, item):
        item_found = False
        hash_value = self.hashfunction(item)
        if self.data[hash_value] == item:
            item_found = True
        else:
            next_slot = self.new_hash(hash_value)
            while item_found == False:
                if next_slot == self.length:
                    next_slot = 0
                if next_slot == hash_value or next_slot == None:
                    break
                if self.data[next_slot] == item: 
                    item_found = True
                next_slot = self.new_hash(next_slot)
        return item_found

    # Running Time: O(1)
    def items(self):
        return self.data

# Most of the methods in the HashList have a constant run time of O(1). It doesn't take any time at all for the computer to create the HashList,
# perform the hashvalue or new_hash functions, or th return the HashList's data. In a best case scenario with no collisions, adding and searching 
# the HashList for items would also take a constant run time of O(1). This is because the HashList isn't having to iterate over anything in a best
# case scenario, it simply needs to perform simple math calculations to either place or locate data. In a worst case scenario however, because I
# am using rehashing by linear probing, the put and contains functions would approach a linear runtime of O(N) as the HashList has to iterate
# over itself to either find an open spot for an item, or an open spot meaning that the item is not present.

# In order to modify our HashList into a dictionary, we would need to create a second list of data inside of the class that would store "keys"
# for each piece of data. Then, simply calculating the hashvalue each time, we would store each piece of data's "key" value inside of that second list
# so that each piece of data would exist as a "key" "value" pair, just like a dictionary.

def test():
    #testing code goes here...
    print("testing...")

test()