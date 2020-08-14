import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#idea: convert name to number, add them to a binary search tree one by one (for one array), use BST method to find the name you're looking for and then append that to the duplicates list

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree ----- what about accounting for dupes?
    def insert(self, value):
        #check if value is less than this node's value
        if value < self.value:
            #does current node have a left child? If so, try the same method on it instead
            if self.left != None:
                self.left.insert(value)
            #otherwise (if there is space there), set self.left to the new node
            else:
                self.left = BSTNode(value)
        #now, since the value is greater than or equal to the current node's we'll look to the right
        else:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Does the current node == target?
        if target == self.value:
            return True
        #else, check if target is greater or less than the target and use recurrsion appropriately
        elif target > self.value and self.right != None:
            return self.right.contains(target)
        elif target < self.value and self.left != None:
            return self.left.contains(target)
        #else, it's not here buddy
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right != None:
            self.right.for_each(fn)
        if self.left != None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left != None:
            self.left.in_order_print()
        print(self.value)
        if self.right != None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):

        from collections import deque

        q = deque()
        q.append(self)
        
        while len(q) > 0:
            current_node = q.popleft()

            #check if node has children
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        if self.left != None:
            self.left.dft_print()
        if self.right != None:
            self.right.dft_print()

#New code ---

def textToNum(text):
    nums = [ord(letter) for letter in text]
    newString = ''.join(str(n) for n in nums)
    newNum = int(newString)
    return newNum

startVal = textToNum('root')

bst = BSTNode(startVal)

for name in names_1:
    numVal = textToNum(name)
    bst.insert(numVal)

#^Now the tree exists with names_1 contents, run a loop through names_2 and use the contains method to see if it exists. if it does, append to duplicates

for name in names_2:
    numVal = textToNum(name)
    if bst.contains(numVal) == True:
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicates = set(names_1).intersection(names_2)

print(f'Sprint duplicates: {len(duplicates)}')