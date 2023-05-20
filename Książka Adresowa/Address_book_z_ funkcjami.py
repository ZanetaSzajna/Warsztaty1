#Tworzymy  słownik z  danymi

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

# definiowanie funkcji
def menu():

    print(f"Welcome {user_name}")
    print("If you want to display the address book, select display")
    print("If you want to add a new entry to the address book select add")
    print("If you want to delete an entry from the address book select delete ")
    print("If you are finishing for today select end")




def print_dict():
    print("It is your Adress book --> ")
    for key in dict_book:
       print(key, dict_book[key])
def add_dict():
    name = input("Enter surname and name --> ").title()
    phone_number = input("Enter phone number ( nine number xxxxxxxxx)--> ")
    if phone_number.isdigit() == False:
        print("the number you have given does not consist only of digits")
        phone_number = input("Enter phone number ( nine number xxxxxxxxx")
    email = input("Enter emial --> ")
    dict_book[name] = [phone_number, email]
    print(f"We add a new contact {name} to your Adress book")
    for key in dict_book:
        print(key, dict_book[key])
def delete_dict():
    print("Which element do you want delete ? --> ")
    delete_element = input("Enter surname and name ")
    del dict_book[str(delete_element)]
    print(f"We delete contact {delete_element} to your Adress book")
    for key in dict_book:
        print(key, dict_book[key])
def end_dict():
    print(f"Goodbay We conclude for today. See you in a short time {user_name}")

# Częśś główna

menu()
user_choose=input(f" So {user_name.title()}, what we do ? --> ")
user_choose.lower()

def choose(user_choose):
    if user_choose.lower() =="display":
        print_dict()
    elif user_choose.lower() == "add":
        add_dict()
    elif user_choose.lower() =="delete":
        delete_dict()
    elif user_choose.lower()=="end":
        end_dict()
choose(user_choose)
