email1 = 'cv131116@student.sgh.waw.pl'
email2 = '@student.sgh.waw.pl'
email3 = 'cv131116@student.sgh.waw.@pl'
email4 = 'cv131116\sgh.waw'
email5 = 'cv131116/sgh.waw@.'

email_list = [email1, email2, email3, email4, email5]

def email_validation(email):
    for i in range(len(email)):
        if (ord(email[i]) in range(32,46)) \
        or (ord(email[i]) in range(58,64)) \
        or (ord(email[i]) in range(91,97)) \
        or (ord(email[i]) in range(123,127)) \
        or (ord(email[i]) == 47): return False
    if email.find('@') == -1:
        return False
    elif email[len(email)-1].lower() \
        not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']: 
        return False
    elif (email[0].lower() \
        not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) \
        and (email[0] not in ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']): 
        return False
    elif (email.rfind('@') != email.find('@')): return False
    else: return True

for i in range(len(email_list)):
    print(str(email_list[i]) + '  ' + str(email_validation(email_list[i])))
