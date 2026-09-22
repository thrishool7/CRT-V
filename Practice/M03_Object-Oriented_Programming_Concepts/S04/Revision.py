class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, first_name, age):
        member = {'first_name': first_name, 'age': age}
        self.members.append(member)

    def get_members(self):
        return self.members

    def get_last_name(self):
        return self.last_name