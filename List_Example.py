# Append Items
A_list = ["Apple", "banana", "chery"]
B_list = ["mango", "papaya", "pineapple"]
B_tuple = ("mango", "papaya")
C_list = ["Apple", "banana", "papaya"]
print("Current List :", A_list)
# Add items to the end of list, use append()
A_list.append("orange")
print("A_List after change", A_list)
# To insert a list item at a specified index, use the insert()
A_list.insert(1, 'lemon')
print("A_list after insert: ", A_list)
# To append elements from another list to the current list, use the extend()
A_list.extend(B_list)
print(" list affter extend: ", A_list)
A_list.extend(B_tuple)
print(" list affter extend to tuple: ", A_list)
# The remove() method removes the specified item
C_list.remove("Apple")
print(" C_list affter Remove : ", C_list)
# The pop() method removes the specified index
C_list.pop(1)
print(" C_list affter Remove by pop : ", C_list)
B_list.pop()
print(" B_list affter Remove by pop : ", B_list)
