import json
import os
import data

def menu():
	print("\n-----------MODEL PHONE-BOOK-------------")
	options = ["1. Save a contact", "2. View saved contacts", "3. Edit saved contact", "4. Delete saved contact", "5. Exit program"]
	for option in options:
		print(option)
	print("----------------------------------------\n")
	return None

def input_details():
	fields = {"name" : "", "phone": "", "email": "", "relation": ""}
	for field in fields.keys():
		response = input(f"Enter {field}: ")
		fields[field] = response
	contact = data.Contact(
		name = fields["name"],
		phone = fields["phone"],
		email = fields["email"],
		# relation = fields["relation"]
	)
	save_input_details(contact)


def save_input_details(contact):
    contacts = []
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)

    except FileNotFoundError:
        contacts = []
    except json.JSONDecodeError:
        print("Warning: Invalid JSON in contacts.json. Starting with an empty list.")
        contacts = []

    contacts.append(vars(contact))

    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)
    print("Contact saved successfully!\n")


def edit_saved_contact():
	contacts = []
	name = input("Enter name of the saved contact: ")

	with open('contacts.json', 'r') as file:
		contacts = json.load(file)
	
	for contact in contacts:
		if contact["name"] == name:
			field = input(f"\nEnter the field for {name} to edit: ").lower()
			value = input(f"Enter the new value for {field}: ").lower()
			contact[field] = value

			with open('contacts.json', 'w') as file:
				json.dump(contacts, file, indent = 4)

			print("Contact detail updated successfully\n")
			return None
	print("Contact not found\n")


def view_saved_contacts():
	contacts = []
	with open('contacts.json', 'r') as file:
		contacts = json.load(file)
	
	if not contacts:
		print("No saved contacts available")
		return None

	print("\nSaved contacts are: ")
	for contact in contacts:
		for key, value in contact.items():
			print(f"{key.upper()} : {value}")
		print() 
	contacts.clear()
	print("\n")
	
def delete_saved_contact():
	contacts = []
	name = input("Enter name of the saved contact: ")

	with open('contacts.json', 'r') as file:
		contacts = json.load(file)
	
	for contact in contacts:
		if contact["name"] == name:
			contacts = list(filter(lambda contact: contact["name"] != name, contacts))
			with open('contacts.json', 'w') as file:
				json.dump(contacts, file, indent = 4)
			print("Contact deleted successfully\n")
			return None
	print("Contact not found\n")


