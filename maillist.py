import person


class MailList():
    def __init__(self, list_name):
        self.list_name = list_name
        self.people = []

    def __str__(self):
        string = ""
        id_ = 1
        for _person in self.people:
            string += "[%d] %s\n"%(id_, str(_person))
        return string

    def add_person(self, person_):
        if person_ not in self.people:
            self.people.append(person_)

    def has_person_with_mail(self, email):
        for person_ in self.people:
            if person_.email == email:
                return True
        return False

    def merge_with(self, other_list):
        self.people +=\
            [person_ for person_ in other_list.people if person_ not in self.people]

    def export_to_json(self):
        file_ = open(self.list_name, "w")
        file_.write("[\n")

        for person_ in self.people:
            file_.write("\t{\n\t\t\"name\" : \"%s\",\n"%person_.get_name)
            file_.write("\t\t\"email\" : \"%s\""%person_.get_email)
            file_.write("\t},\n")

        file_.write("]")
        file_.close()