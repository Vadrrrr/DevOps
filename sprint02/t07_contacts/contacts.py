import re

def contacts(cont: dict, new: dict, com: str):
    emchek = '^\S\D[A-z]+[@]+[A-z]+[.]+[A-z]+$'
    nchek = '^\S\D[A-z]+$'
    if new.get('email') and new.get('name'):
        email = new.get('email')
        name = new.get('name')
        new.pop('email')
        if re.search(emchek, email) and re.search(nchek, name):
            if com == 'add':
                cont.update({email: {i: new[i] for i in new}})
                return True
            else:
                return False

        if com == 'update':
            if email in cont:
                cont.update({email : {**cont.get(email), **new}})
                return True
            else:
                return False

        if com == 'delete':
            if email in cont:
                cont.pop(new.get('email'))
                return True
            else:
                return False
        else:
            return False
    else:
        return False

