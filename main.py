import handler

def main():

	print("Welcome!!!")
	handler.menu()

	while True:
	    response = int(input("Enter your response: "))
	    switcher = {
	        1: handler.input_details,
	        2: handler.view_saved_contacts,
	        3: handler.edit_saved_contact,
	        4: handler.delete_saved_contact,
	        5: exit
	    }

	    action = switcher.get(response)
	    if action:
	        action()
	    else:
	        print("Invalid input. Program will now exit.")
	        break


if __name__=="__main__":
    main()