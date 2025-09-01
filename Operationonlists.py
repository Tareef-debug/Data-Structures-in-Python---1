lft=["apple","banana","orange","watermelon","kiwi"]
print("lenght of the list",len(lft))
      #print elements
print("first element of the list", lft[0])
print("last element of the list", lft[4])

lft.append("grape")
print("updated list", lft)

lft.remove("apple")
print(" again updated list", lft)

lft.sort()
print("sorted list", lft)

lft.pop(1)
print(" again again updated list", lft)

print(lft*2)


lft.reverse()
print("reversed list", lft)

x = lft[2];4
print("sliced list", x)