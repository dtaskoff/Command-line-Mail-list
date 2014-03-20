from maillist import MailList
import glob
import person


class Interface:
    def __init__(self):
        self.mail_lists = []
        self._load(self.mail_lists)

    def menu(self):
        menu = [
            "Hello Stranger! This is a cutting-edge, console-based mail-list!",
            "Type help, to see a list of commands."]

        return "\n".join(menu)

    def help(self):
        menu = ["Here is a full list of commands:",
                "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
                "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
                "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
                "* create <list_name> - Creates a new empty list, with the given name.",
                "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
                "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
                "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
                "* exit - this will quit the program"]

        return "\n".join(menu)

    def error(self):
        return "Unknown command! Please try again!"

    # all lists will be held in a directory called ./lists
    # example: Hack Bulgaria will be stored as ./lists/Hack%20Bulgaria

    def _load(self, mail_lists):
        files = glob.glob("./lists/*")

        for filename in files:
            maillist = MailList(filename)
            file_ = open(filename, "r")
            contents = file_.read()
            file_.close()
            contents = contents.splitlines()
            for line in contents:
                maillist.add_person(person.Person(line[1], line[3]))
            mail_lists.append(maillist)
     
    def show_list(self, unique_list_identifier):
        return str(self.mail_lists[int(unique_list_identifier) - 1])

    def show_lists(self):
        string = ""
        for index in range(len(self.mail_lists)):
            string += "[%d] %s"%(index + 1, self.mail_lists[index].list_name)

        return string

    def add(self, unique_list_identifier):
        name = input("name>")
        email = input("email>")
        new_person = person.Person(name, email)
        if not self.mail_lists[int(unique_list_identifier) - 1].\
                has_person_with_mail(email):
            self.mail_lists[int(unique_list_identifier) - 1].add_person(new_person)
            return "%s was added to the list" % str(new_person) 
        return "A person with the given mail already exists!"

    def create(self, list_name):
        pass

    def search_email(self, email):
        pass

    def merge_lists(self, list_identifier1, list_identifier2, list_name):
        new_maillist = maillist.MailList(list_name)
        new_maillist.merge_with(self.mail_lists[int(list_identifier1)])
        new_maillist.merge_with(self.mail_lists[int(list_indentifier2)])
        self.mail_lists.append(new_maillist)

    def export(self, list_identifier):
        list_ = self.mail_lists[int(list_identifier)]
        list_name = list_.list_name
        file_ = open("%s.json" % list_name)
        file_.write(list_.export_to_json())
        file_.close()


    def delete(self, list_id):
        pass

    def remove_subscriber(self, list_identifier, subscriber_identifier):
        self.mail_lists[int(list_identifier) - 1].\
            remove_person(int(subscriber_identifier)

    def update(self, list_id, new_name):
        pass

    #def update_subscriber(self, list_id, subscriber): # update name and email
    #    pass

    #def import_json(self, filename):
    #    pass

    def exit(self):
        exit(0)
