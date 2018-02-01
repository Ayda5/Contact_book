#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, first_name, last_name, birth_year, address, phone_number,  email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name


def list_all_contact(contacts):
    for index, person in enumerate(contacts):
        print "ID: " + str(index)
        print person.get_full_name()
        print person.birth_year
        print person.address
        print person.phone_number
        print person.email
        print ""  # empty line

    if not contacts:
        print "The contact list is empty"


def add_new_contact(contacts):
    first_name = raw_input("Please enter contact's first name: ")
    last_name = raw_input("Please enter contact's last name: ")
    birth_year = raw_input("Please enter contact's birth year: ")
    address = raw_input("Please enter contact's address: ")
    phone = raw_input("Please enter contact's phone number: ")
    email = raw_input("Please enter contact's email: ")

    new = Contact(first_name=first_name, last_name=last_name, birth_year=birth_year, address=address,
                  phone_number=phone, email=email)
    contacts.append(new)

    print ""  # empty line
    print new.get_full_name() + "was successfully added to contact list."


def edit_contact(contacts):
    print "Select the number of the contact you'd like to edit: "

    for index, person in enumerate(contacts):
        print str(index) + ") " + person.get_full_name()

    print ""  # empty line
    selected_id = raw_input("What contact would you like to edit? (enter ID number): ")
    selected_contact = contacts[int(selected_id)]

    new_first_name = raw_input("Please enter a new first name for %s: " % selected_contact.get_full_name())
    selected_contact.first_name = new_first_name

    print ""  # empty line
    print "First name updated."

    new_last_name = raw_input("Please enter a new last name for %s: " % selected_contact.get_full_name())
    selected_contact.last_name = new_last_name

    print ""  # empty line
    print "Last name updated."

    new_birth_year = raw_input("Please enter a new birth year for %s: " % selected_contact.get_full_name())
    selected_contact.birth_year = new_birth_year

    print ""  # empty line
    print "Birth year updated."

    new_address = raw_input("Please enter a new address for %s: " % selected_contact.get_full_name())
    selected_contact.address = new_address

    print ""  # empty line
    print "Address updated."

    new_phone_number = raw_input("Please enter a new phone number for %s: " % selected_contact.get_full_name())
    selected_contact.phone_number = new_phone_number

    print ""  # empty line
    print "Phone number updated."

    new_email = raw_input("Please enter a new email for %s: " % selected_contact.get_full_name())
    selected_contact.email = new_email

    print ""  # empty line
    print "Email updated."


def delete_contact(contacts):
    print "Select the number of contact you'd like to delete: "

    for index, person in enumerate(contacts):
        print str(index) + ") " + person.get_full_name()

        print ""  # empty line
        selected_id = raw_input("What contact would you like to delete? (enter ID number): ")
        selected_contact = contacts[int(selected_id)]

        contacts.remove(selected_contact)
        print ""  # empty line
        print "Contact was successfully removed from your contact list."


def main():
    print "Welcome to your Contact List."

    eduard = Contact(first_name="Eduard", last_name="Skarje", birth_year="1975", address="Hollywood 7",
                   phone_number="053638797434", email="edo.skarje@gmail.com")
    spela = Contact(first_name="Spela", last_name="Marela", birth_year="1982", address="Horjul 12",
                   phone_number="054452487287", email="spela.marela@gmail.com")
    anja = Contact(first_name="Anja", last_name="Mersolcek", birth_year="1983", address="Klemenova ulica 44",
                   phone_number="0763676427623", email="anja.mersolcek@yahoo.com")
    katarina = Contact(first_name="Kataraina", last_name="Piccola", birth_year="1990", address="Strazarjeva 3",
                  phone_number="087665667387", email="katarinapiccola@gmail.com")

    contacts = [eduard, spela, anja, katarina]

    while True:
        print ""  # empty line
        print "Plese choose one of these options: "
        print "a) See all contacts"
        print "b) Add a new contact"
        print "c) Edit a contact"
        print "d) Delete a contact"
        print ""  # empty line

        selection = raw_input("Please enter your selection (a, b, c, d): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_contact(contacts)
        elif selection.lower() == "b":
            add_new_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            delete_contact(contacts)
        elif selection.lower() == "e":
            print "Thank you for using Contact List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue


if __name__ == '__main__':
    main()
