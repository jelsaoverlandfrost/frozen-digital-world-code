def get_details(name, key, phonebook):
    for i in range(0, len(phonebook)):
        if phonebook[i]['name'] == name:
            return phonebook[i][key]

phonebook = [{'name':'Andrew', 'mobile_phone':9477865,  'office_phone':6612345, 'email':'andrew@sutd.edu.sg'},{'name':'Bobby','mobile_phone':8123498, 'office_phone':6654321, 'email': 'bobby@sutd.edu.sg'}]

print get_details("Bobby", 'office_phone', phonebook)