import person
import json


class MailList():
    def __init__(self, list_name):
        self.list_name = list_name
        self.people = []

    def __str__(self):
        string = ""
        id_ = 1
        for _person in self.people:
            string += "[%d] %s\n"%(id_, str(_person))
            id_ += 1
        return string

    def add_person(self, person_):
        if person_ not in self.people:
            self.people.append(person_)

    def has_person_with_mail(self, email):
        for person_ in self.people:
            if person_.email == email:
                return True
        return False

    def remove_person(self, index_of_person):
        del self.people[index_of_person - 1]

    def merge_with(self, other_list):
        self.people +=\
            [person_ for person_ in other_list.people if person_ not in self.people]

    def export_to_json(self):
        json_dump_list = []

        for person_ in self.people:
            json_dump_list.append({"name" : person_.get_name(),
                                    "email" : person_.get_email()})
        
        return json.dumps(json_dump_list, indent = 4)