# 1 ) ...........................................
# a="Java",'Python','SQL','C'
# print(tuple(a))

# 2) ............................................
# x=(1,)
# print(x,type(x))

# 3) ...................................
# a1=(1,2,3,4,5,6,7,8,9)
# print(a1[::-1])

# 4) ..............................................
# t1=tuple()
# n1=int(input("Enter number for tuple : "))
# for e in range(n1):
#     a=int(input("Enter %d : "%e))
#     t1=t1+(a,)
# t2=tuple()
# n2=int(input("Enter number for tuple : "))
# for e in range(n2):
#     a=int(input("Enter %d : "%e))
#     t2=t2+(a,)
# print("Before swapping tuple t1 and t2 : ",t1,t2)

# t1,t2=t2,t1

# print("After swapping tuple t1 and t2 : ",t1,t2)


# 5) ...............................................
# t3=(1,2,3,4,5,6)
# t3=(1,1,1,1,1)
# for i in range(len(t3)-1):
#     if t3[i]==t3[i+1]:
#         print("All are same")
#         break
#     else:
#         print("different")
#         break


# 6) ........................................
# tuple1=(100, 200, 300, 400)
# a,b,c,d=tuple1
# print(a,b,c,d)


# 7) ........................................
# tuple2=(1,2,3,4,5,6)
# tp=tuple()
# for e in tuple2:
#     if e==4 or e==5:
#         tp=tp+(e,)
# print(tp)


# 8) .......................................
# t4 = [('a', 21),('b', 37),('c', 11), ('d',29)]
# for i in range(0,len(t4)):
#     for j  in range(0,len(t4)-i-1):
#         if t4[j][1]>t4[j+1][1]:
#             temp=t4[j]
#             t4[j]=t4[j+1]
#             t4[j+1]=temp
# print(t4)

# 9) .........................................
# t5 = ("Python", [10, 20, 30], (2, 4, 16))
# print(t5[1][1])

# 10).....................................
t6 = (11, [22, 33], 44, 55)
t6[1][0]=222
print(t6)