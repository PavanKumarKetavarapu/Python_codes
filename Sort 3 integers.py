n1=int(input("enter the 1st integer value: "))
n2=int(input("enter the 2nd integer value: "))
n3=int(input("enter the 3rd integer value: "))
a1=min(n1,n2,n3)
a3=max(n1,n2,n3)
a2=(n1+n2+n3)-a1-a3
print("sorting order of the given 3 integrs is",a1,a2,a3)