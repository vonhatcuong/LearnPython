# import 'array' for array operations
import array
#create array
arr= array.array('i',[-10,1,2,3,4,5,8])
arr1= array.array('i',[1, 2, 3, 1, 2, 5])
# printing original array
print("The new created array is : " , end=" ")
for i in range (0,7):
    print (arr[i], end=" ")

print("\r")

# using append() to insert new value at end
arr.append(9)

# printing appended array
print("The appended array is :",end=" ")
for i in range(0,8):
    print(arr[i],end=" ")

# Using insert() to insert value at specific position
# Insert 5 at 2nd position'
arr.insert(6,6 )
print("\r")

# Printing array after insertion
print ("The array after insertion is : ", end="")
for i in range(0,9):
    print(arr[i], end=" ")
print("\r")

# pop():- This function removes the element at the position
#          mentioned in its argument and returns it.

print("The popped element is: ",end=" ")
print(arr.pop(5))

# printing array after popping
print ("The array after popping is : ",end="")
for i in range (0,8):
    print (arr[i],end=" ")
 
print("\r")
 
# using remove() to remove 1st occurrence of 1
arr.remove(8)
# printing array after removing
print ("The array after removing  is : ",end="")
for i in range (0,7):
    print (arr[i],end=" ")

print("\r")
# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2  is : ",end="")
print (arr1.index(2))
 
#using reverse() to reverse the array
arr.reverse()
 
# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range (0,7):
    print (arr[i],end=" ")
print("\r")

# Return the number of occurrences of x in the array
print("Return count of number 1 in the array",end=" ")
print(arr1.count(1),"\r")
