#  Ex  1
thisset  =  {"apple",  "banana",  "cherry"}
thisset .add("orenge")
print(thisset)
#  Output: {'orenge', 'cherry', 'apple', 'banana'}

#  Ex  2
thisset  =  {"apple",  "banana",  "cherry"}
tropical  =  {"pineapple",  "mango",  "papaya"}
thisset.update(tropical)
print(thisset)
# Output : {'pineapple', 'cherry', 'apple', 'mango', 'papaya', 'banana'}