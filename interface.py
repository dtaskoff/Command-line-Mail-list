import maillist
import glob
import person


class Interface():
    def __init__(self):
        self.mail_lists = []
        self._load()

    def menu(self):
        menu = [
            "Hello Stranger! This is a cutting-edge, console-based mail-list!",
            "Type help, to see a list of commands."]

        return "\n".join(menu)

    def help(self):
        menu = [
            "Here is a full list of commands:",
            "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
            "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
            "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
            "* update_subscriber <unique_list_identifier> <unique_name_identifier> - Updates the information for the given subscriber in the given list",
            "* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list",
            "* create <list_name> - Creates a new empty list, with the given name.",
            "* delete <list_identifier> - Deletes the list with the given identigier. Use with care!",
            "* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.",
            "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
            "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - Merges list1 and list2 into a new list, with the given name.",
            "* export <unique_list_identifier> - Exports the given list into a JSON file, named just like the list. All white spaces are replaced by underscores.",
            "* import <json_file_name> - Imports the given JSON file into a list, named just like the JSON file(without the .json extension).",
            "* exit - this will quit the program"]

        return "\n".join(menu)

    def error(self):
        return "Unknown command! Enter 'help' for more information."

    def _load(self):
        files = glob.glob("./lists/*")

        for filename in files:
            maillist_ = maillist.MailList(filename[8:])
            file_ = open(filename, "r")
            contents = file_.read()
            file_.close()
            contents = contents.splitlines()

            for line in contents:
                maillist_.add_person(person.Person(line.split(":")[0], line.split(":")[1]))
            self.mail_lists.append(maillist_)


    def show_lists(self):
        list_ = ["[{0}] {1}".format(identifier + 1, self.mail_lists[identifier].list_name)\
            for identifier in range(0, len(self.mail_lists))]

        return "\n".join(list_)
     
    def show_list(self, unique_list_identifier):
        index = int(unique_list_identifier) - 1
        if index >= len(self.mail_lists):
            return "A list with such an index doesn't exist"
        return str(self.mail_lists[index])

    def add(self, unique_list_identifier):
        index = int(unique_list_identifier) - 1
        if index >= len(self.mail_lists):
            return "A list with such an index doesn't exist"

        name = input("name>")
        email = input("email>")
        new_person = person.Person(name, email)
        if not self.mail_lists[index].has_person_with_email(email):
            self.mail_lists[index].add_person(new_person)
            return "{0} was added to the list".format(str(new_person))

        return "A person with the given email <{0}> already exists!".format(email)


    def update_subscriber(self, unique_list_identifier, unique_name_identifier):
        list_index = int(unique_list_identifier) - 1
        subscriber_index = int(unique_name_identifier) - 1

        if list_index >= len(self.mail_lists):
            return "A list with such an index doesn't exist"

        if subscriber_index >= len(self.mail_lists[list_index].people):
            return "A subscriber with such an index doesn't exist"

        subscriber = self.mail_lists[list_index].people[subscriber_index]

        print("Updating: {0}".format(subscriber))
        print("Press enter if you don't want to change the field")

        name = input("new name>")
        email = input("new email>")

        if len(name) > 0:
            subscriber.name = name
        if len(email) > 0:
            subscriber.email = email

        return "Subscriber update: {0}".format(subscriber)

    def remove_subscriber(self, unique_list_identifier, unique_name_identifier):
        list_index = int(unique_list_identifier) - 1
        subscriber_index = int(unique_name_identifier) - 1

        if list_index >= len(self.mail_lists):
            return "A list with such an index doesn't exist"

        if subscriber_index >= len(self.mail_lists[list_index]):
            return "A subscriber with such an index doesn't exist"

        self.mail_lists[list_index].remove_person(subscriber_index + 1)
        print("Subscriber deleted")

    def create(self, list_name):
        self.mail_lists.append(maillist.MailList(list_name))
        return "New list <{0}> was created!".format(list_name)

    def update(self, list_identifier, new_name):
        index = int(list_identifier) - 1
        if index >= len(self.mail_lists):
            return "A list with such an index doesn't exist"

        old_name = self.mail_lists[index].list_name
        self.mail_lists[index].list_name = new_name
        return "The list {0} was renamed to {1}".format(old_name, new_name)

    def delete(self, list_identifier):
        index = int(list_identifier) - 1
        name = self.mail_lists[index].list_name
        del self.mail_lists[index]
        return "The list <{0}> was deleted!".format(name)

    def search_email(self, email):
        result = [list_ for list_ in self.mail_lists if list_.has_person_with_email(email)]
        if len(result) == 0:
            return "{0} was not found in the current mailing lists.".format(email)
            
        result, self.mail_lists = self.mail_lists, result
        string_ =  "<{0}> was found in \n{1}".format(email, self.show_lists())
        result, self.mail_lists = self.mail_lists, result
        return string_

    def merge_lists(self, list_identifier_1, list_identifier_2, list_name):
        index1 = int(list_identifier_1) - 1
        index2 = int(list_identifier_2) - 1
        new_maillist = maillist.MailList(list_name)
        new_maillist.merge_with(self.mail_lists[index1])
        new_maillist.merge_with(self.mail_lists[index2])
        self.mail_lists.append(new_maillist)

        return "New list <{0}> was created!".format(list_name)

    def export(self, list_identifier):
        list_ = self.mail_lists[int(list_identifier) - 1]
        list_name = list_.list_name
        file_ = open("{0}.json".format(list_name), "w")
        file_.write(list_.export_to_json())
        file_.close()
        return "The list <{0}> was exported to json format".format(list_name)

    def import_(self, json_file_name):
        maillist_ = maillist.MailList(json_file_name[:len(json_file_name) - 5])
        file_ = open(json_file_name, "r")
        contents = file_.read()
        file_.close()
        maillist_.import_from_json(contents)
        self.mail_lists.append(maillist_)
        return "The list <{0}> was created from {1}".format(maillist_.list_name, json_file_name)

    def exit(self):
        exit(0)