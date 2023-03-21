# create an empty set
s = set()

# add elements to the set 
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # sets can only have unique values, so adding another 3 does nothing

s.remove(2)

print(s)

print(f"The set has {len(s)} elements")