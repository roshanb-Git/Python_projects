class Member:
    def __init__(self, name, member_id, active =True):
        self.name = name
        self.id = member_id
        self.active =active


def display_info(Member):
    print(f"Name: {Member.name} \nID: {Member.id} ")


# check status of member
def check_status(member):
        if member.active:
            print(f'{member.name} is an active user')
        else:
            print(f'{member.name} is currently suspended')


#update status of member
def update_status(member,status):
       member.active =status
       if status:
           print(f'{member.name} is an active user now ')
       else:
           print(f'{member.name} has been suspended')

    