
def secure_name(name):
    return name[0] + '**'

def secure_cn(cn):
    return cn[0:8] + '******'

def secure_phone(phone):
    return phone[4:8], '****'