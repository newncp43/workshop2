# Ex 1
thisset  =  {"apple",  "banana",  "cherry"}
thisset.remove("banana")
print(thisset) # Output: {'apple', 'cherry'}

# Ex 2
thisset  =  {"apple",  "banana",  "cherry"}
thisset.discard("banana")
print(thisset) # Output: {'cherry', 'apple'}

# Ex 3
thisset  =  {"apple",  "banana",  "cherry"}
x = thisset.pop()
print(thisset) # Output: {'apple', 'banana'}

# Ex 4
thisset  =  {"apple",  "banana",  "cherry"}
thisset.clear()
print(thisset) # Output: set()
