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