#16 pages per EVS Tech document | 14 pages per custodian | "X" pages per HS student

number = int(input("Number:"))

#logic for 
if number % 16 == 0:
    print("EVS Tech document(s)")
elif number % 14 == 0:  
    print("Custodian document(s)")
elif number % 12 == 0:
    print("HS document(s)")
else:
    print("Please check to make sure you included all of the pages for the documents")




#print ("Your number was:", number)