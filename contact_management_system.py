  def show_all_contacts(cls):
        if len(cls.phone_dict) <= 0:
            print("No contacts Found")
        else:
            for contact in cls.phone_dict:
                print(contact.show_contact())

    @classmethod
    def search(cls,search_name):
        for i in cls.phone_dict:
            if i.name == search_name:
                return i.number


    @staticmethod
    def phone_valid(number):

        if len(number)  >= 10:
            return number

        else:
            print("not a valid number")





n= int(input("How many number do u want to add: "))
for i in range(n):
    name= input("Enter the contact name: ")
    number = (input("Enter the number: "))
    if contacts.phone_valid(number):
        contacts(name,number)



contacts.show_all_contacts()
