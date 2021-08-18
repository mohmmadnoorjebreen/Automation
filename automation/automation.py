import re 

with open('assets/potential-contacts.txt','r') as file:
    read_file=file.read()
    new_email=re.findall("[\w\.-]+@[\w\.-]+",read_file)
    my_email_list = list(dict.fromkeys(new_email))
    emails = sorted(my_email_list)
    with open('assets/emails.txt', 'w') as file:
        for email in emails:
            file.write(f'{email}\n')
    print(emails)


with open('assets/potential-contacts.txt','r') as file:
    read_file=file.read()
    new_phone=re.findall("(\d{3}[-\.]?\d{3}[-\.]?\d{4}|\(\d{3}\)\d{3}[-\.]?\d{4})",read_file)
    missing_area_code=re.findall("(\d{3}[-\.]?\d{4})",read_file)
    missing_area_code_list = []
    for area in missing_area_code:
        for string in area:
            if string ==  '.' or string == '-':
                missing_area_code_list.append(f'206{string}{area}')
        if len(area) ==7:
            missing_area_code_list.append(f'206{area}')
    my_phone_num_list = list(dict.fromkeys(new_phone)) +list(dict.fromkeys(missing_area_code_list)) 
    my_phone_num_list_formated = []
    for unformatted in my_phone_num_list:
        my_phone_num_list_formated.append(re.sub('\.','-',unformatted))     
    phones = sorted(my_phone_num_list_formated)
    with open('assets/phone_numbers.txt', 'w') as file:
        for phone in phones:
            file.write(f'{phone}\n')
    print(phones)

