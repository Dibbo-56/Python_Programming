class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


obj1 = Friend("John", "@1", "1234")
obj2 = Friend("Johny", "@2", "1324")
obj3 = Friend("John3", "@3", "1243")

for i in Contact.all_contacts:
    print(i.name, i.email, i.phone)
