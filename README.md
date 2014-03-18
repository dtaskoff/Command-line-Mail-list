Command line mail list
======================

Our repo for the Hack Bulgaria's project

class person:
- name
- identifier

- constructor (__init__)
- to string method (__str__)

class mail list:
- people (and array of persons)
- constructor (__init__)
- to string method (__str__)
- search by mail
- add person
- merge with another list
- export to JSON

class mail interface:
- runs a cycle 'till command 'exit' is entered
- works with files saved on the harddisk
- show lists
- show list by identifier
 
 class person -> class mail list -> class interface

* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier
* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>
* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.
* create <list_name> - Creates a new empty list, with the given name.
* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.
* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.
* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.
* exit - this will quit the program