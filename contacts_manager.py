import re
def add_contact(contact_list):
    while True:
        to_add = input("Enter Contact Name: (enter 'done' when finished) ")
        name_criteria = r'[a-zA-Z]+ [A-Za-z]+'
        name_match = re.findall(name_criteria,to_add)

        if to_add.lower() == 'done':
            print(contact_list)
            break

        if name_match:
            name = name_match[0]
            if name not in contact_list:
                contact_list.append(name)

            else:
                print(f'{name} is already inside {contact_list}')
            

        else:
            print("Please enter a first name and a last name")
            continue


# add_contact()

def remove_contact(contact_list):
    print(contact_list)

    while True:
        to_remove = input("Enter Contact to remove: (enter 'done' when finished) ")
        
        if to_remove.lower() == "done":
            print(contact_list)
            break
        
        if to_remove in contact_list:
            contact_list.remove(to_remove)
        
        else:
            print(f"{to_remove} not found try again")
            continue
        
# remove_contact


def display_contacts(contact_list):
    for contact in contact_list:
        print(f"Contact: {contact}")

# display_contacts()