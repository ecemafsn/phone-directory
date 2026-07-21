contacts=[]

while True:
    print("Phone Directory")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    try:
        choice=int(input("Enter Your Choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue
    
    if choice == 1:
       print("Add Contact Selected")
       name=input("Enter Name: ")
       phone=input("Enter Phone Number: ")
       contact={
           "name": name,
           "phone": phone
       }
       contacts.append(contact)
       print("Contact Added Successfully!")

    elif choice == 2:
       print("View Contacts Selected")
       if len(contacts)==0:
              print("No contacts found.")
       for contact in contacts:
           print("Name:", contact["name"])
           print("Phone:", contact["phone"])
           print()

    elif choice == 3:
       print("Search Contact Selected")
       search_name=input("Enter Name to Search:")
       found=False
       for contact in contacts:
              if contact["name"].lower() == search_name.lower():
                        print("Name:", contact["name"])
                        print("Phone:", contact["phone"])
                        found=True
                        break
       if not found:
                print("Contact not found.")
    

    elif choice == 4:
       print("Delete Contact Selected")
       delete_number=input("Enter Phone Number to Delete:")
       found=False
       for contact in contacts:
            if contact["phone"]==delete_number:
                 contacts.remove(contact)
                 print("Contact deleted successfully!")
                 found=True
                 break
       if not found:
            print("Contact not found.")     
            

    elif choice == 5:
       print("Goodbye!")
       break

    else:
       print("Invalid Choice!")


