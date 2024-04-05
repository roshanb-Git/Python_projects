class Member:
    def __init__(self, name, member_id, address, phone, email):
        self.name = name
        self.id = member_id
        self.address = address
        self.phone = phone
        self.email = email


def display_info(Member):
    print(f"Name: {Member.name} \nID: {Member.id} \nAddress: {Member.address} \nPhone: {Member.phone} \nEmail: {Member.email}")