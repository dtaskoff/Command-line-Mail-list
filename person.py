class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_mail(self):
        return self.email

    def __str__(self):
        return "{0} - {1}".format(self.name, self.email)