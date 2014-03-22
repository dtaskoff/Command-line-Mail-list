class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "{0} - {1}".format(self.name, self.email)

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email