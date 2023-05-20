# Na początku zapytamy o imię użytkownika tak aby bardziej spersonalizować program

dict_book={ 'Szajna Żaneta':['789123456',"sz@gmail.com"],
             'Kowalski Adam':['564789123', "kowalski.adam@wp.pl"],
             'Nowicki Jan': ['123456789', 'nowicki.jan@onet.pl'],
             'Nowak Andrzej': ["456987321", "anowak.interia.pl"],
             'Miłowicz Magda':["123987654", "magdam@kancelaria.pl"],
             'Korzecki Piotr':["654312978", 'korzeckip@wp.pl'],
             'Płaska Wojciech':["369852147", 'plaskaw@gmail.com']
}



user_name = input(" Please enter your name --> ")
print(" ")

print(f"Welcome {user_name}")
print("If you want to display the address book, select display")
print("If you want to add a new entry to the address book select add")
print("If you want to delete an entry from the address book select delete ")
print("If you are finishing for today select end")

print("")
user_choose=input(f" So {user_name}, what we do ? --> ")
user_choose.lower()

if user_choose.lower() == 'display':
   print("Here is your address book ")

   #wyświetlanie słownika
   for key in dict_book:
       print(key, dict_book[key])
   print(" ")
   print(" What now ? ")
   print("If you want to go back to the main menu, select menu and if you want to end today, select end ")
   next_choose=input()
   if next_choose.lower() == "menu":
       print(f"Welcome {user_name}")
       print("If you want to display the address book, select display")
       print("If you want to add a new entry to the address book select add")
       print("If you want to delete an entry from the address book select delete ")
       print("If you are finishing for today select end")
       print("")
       user_choose = input(f" So {user_name}, what we do ? --> ")
   elif next_choose.lower() == "end":
       print(f" We conclude for today. See you in a short time {user_name}")
elif user_choose.lower() == "add":
    lenght_dict=len(dict_book)
    name=input("Enter surname and name --> ").title()
    phone_number=input("Enter phone number ( nine number xxxxxxxxx)--> ")
    if phone_number.isdigit() == False:
        print("the number you have given does not consist only of digits")
        phone_number = input("Enter phone number ( nine number xxxxxxxxx")
    email=input("Enter emial --> ")
    dict_book[name]=[phone_number, name]
    for key in dict_book:
        print(key, dict_book[key])

elif user_choose.lower() == "delete":
    print("Which element do you want delete ? --> ")
    delete_element= input("Enter surname and name ")
    del dict_book[str(delete_element)]
    for key in dict_book:
        print(key, dict_book[key])
elif user_choose.lower()=="end":
    print(f"Goodbay We conclude for today. See you in a short time {user_name}")
