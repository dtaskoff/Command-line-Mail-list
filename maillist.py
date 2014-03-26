import person
import json

# a class implementing a single maillist file
class MailList():
    # a simple constructor
    def __init__(self, list_name):
        self.list_name = list_name
        self.people = []

    # the to-string method for easier viewing
    def __str__(self):
        list_ = ("[{0}] {1}".format(identifier + 1, str(self.people[identifier]))\
            for identifier in range(0, len(self.people)))

        return "\n".join(list_)

    # adds a person object to the current maillist
    def add_person(self, person_):
        if person_ not in self.people:
            self.people.append(person_)
            return True
        return False

    # removes a person by his index in the list
    def remove_person(self, index_of_person):
        del self.people[index_of_person - 1]

    # return true if there is a person with this 'email'
    # in the current maillist
    def has_person_with_email(self, email):
        for person_ in self.people:
            if person_.get_email() == email:
                return True
        return False

    # merges the current maillist with some other maillist
    def merge_with(self, other_list):
        self.people +=\
            [person_ for person_ in other_list.people if person_ not in self.people]

    # exports the maillist into a json file named
    # upon the list
    def export_to_json(self):
        json_dump_list = []

        for person_ in self.people:
            json_dump_list.append({"name" : person_.get_name(),
                                    "email" : person_.get_email()})
        
        return json.dumps(json_dump_list, indent = 4)

    # imports a json file to the current list
    # it keeps already entered data!
    def import_from_json(self, json_object):
        loaded_json = json.loads(json_object)

        for data in loaded_json:
            person_ = person.Person(data['name'], data['email'])
            self.people.append(person_)