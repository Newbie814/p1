# SET data type  --  unordered collection of unique elements non-indexed

set = {'Matt', 'Joe', 'John'}
print(set) # {'Matt', 'Joe', 'John'}   does not include duplicates

# SET add method
set.add('Sam')
print(set) # {'Matt', 'Sam', 'Joe', 'John'}

# SET clear method   -- empties the set
set2 = {'Matt', 'Joe', 'John'}
set2.clear()
print(set2) # {}

# SET copy method
set3 = {'Matt', 'Joe', 'John'}
set4 = set3.copy()
print(set4) # {'Matt', 'Joe', 'John'}

# SET difference method    --  returns a new set with elements in the first set but not in the second
set5 = {'Matt', 'Joe', 'John'}
set6 = {'Matt', 'Joe'}
set7 = set5.difference(set6)
print(set7) # {'John'}

# SET difference_update method    --  removes elements from the set
set8 = {"New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", }
set9 = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix",}
set8.difference_update(set9)
print(set8) # {'John'}


###############  difference creates a new set, whereas difference_update modifies the set in place(removes the shared elements)

# SET discard method   --  removes the specified element from the set
set10 = {'Matt', 'Joe', 'John'}
set10.discard('Matt')
print(set10) # {'Joe', 'John'}

# SET intersection method    --  returns a new set with elements common to the two sets
set11 = {'Matt', 'Joe', 'John'}
set12 = {'Matt', 'Joe'}
set13 = set11.intersection(set12)
print(set13) # {'Matt', 'Joe'}

# SET intersection_update method    --  removes jon-shared elements from the set
set14 = {"New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", }
set15 = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix",}
set14.intersection_update(set15)
print(set14) # {'New York', 'Los Angeles', 'Chicago', 'Houston'}


# SET isdisjoint method    --  returns True if the two sets have a null intersection(no elements in common)
#returns false if there is an intersection(common elements)

set16 = {'Matt', 'Joe'}
set17 = {'Sandra', 'John'}
set18 = set16.isdisjoint(set17)
print(set18) # True

# SET issubset method    --  returns True if all the elements of the first set are contained in the second
set19 = {'Matt', 'Joe'}
set20 = {'Matt', 'Joe', 'John'}
set21 = set19.issubset(set20)
print(set21) # True

# SET issuperset method    --  returns True if all the elements of the second set are contained in the first
set22 = set20.issuperset(set19)
print(set22) # True

# SET pop method    --  removes and returns an arbitrary element from the set
set23 = {'Matt', 'Joe', 'John'}
set24 = set23.pop()
print(set24) # John       element popped is random

# SET remove method    --  removes the specified element from the set

set25 = {'Matt', 'Joe', 'John'}
set25.remove('Matt')
print(set25) # {'Joe', 'John'}

# SET symmetric_difference method    --  returns a new set with the non-shared elements of the two sets

set26 = {'Apple', 'Banana', 'Cherry'}
set27 = {'Apple', 'Cherry', 'Durian'}
set28 = set26.symmetric_difference(set27)
print(set28) # {'Banana', 'Durian'}

# SET symmetric_difference_update method    --  removes the shared elements from the set  - mutates the set
set29 = {"New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", }
set30 = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix",}
set29.symmetric_difference_update(set30)
print(set29) # {'Phoenix'}

# SET union method    --  returns a new set with the 2 set concatenated, with no duplicates
set31 = {'Matt', 'Joe', 'John'}
set32 = {'liam', 'sandra', 'connor', 'Matt'}
set33 = set31.union(set32)
print(set33) # {'Joe', 'connor', 'John', 'liam', 'Matt', 'sandra'}

# SET update method    --  adds the elements of the second set to the first set - mutates the set - no new set
set34 = {'Matt', 'Joe', 'John'}
set35 = {'liam', 'sandra', 'connor', 'Matt'}
set34.update(set35)
print(set34) # {'Joe', 'John', 'liam', 'sandra', 'connor', 'Matt'}