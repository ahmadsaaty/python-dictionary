name= input("enter name: ")
dictionaries = []
while name != "stop" :
    
    date= input("enter date: ")
    item= input("enter item: ")
    
    items =[]
    total =0
    while item != "stop":
        price = float(input(f"enter price for {item}: "))
        items.append(item)
        item= input("enter item: ")
        total += price
    print (items)
    
    dictionary1= {
        "name" : name,
        "date" : date,
        "items": items,
        "total": total,
    }

    print(dictionary1)

    name= input("enter new name: ")
    dictionaries.append(dictionary1)

print(dictionaries)


        

    
