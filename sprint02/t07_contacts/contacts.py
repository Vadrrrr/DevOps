import re

def contacts(cont: dict, new: dict, com: str):
    emchek = '^\S\D[A-z]+[@]+[A-z]+[.]+[A-z]+$'
    nchek = '^\S\D[A-z]+$'
    if new.get('email') and new.get('name'):
        email = new.get('email')
        name = new.get('name')
        if re.search(emchek, email) and re.search(nchek, name):
            if com == 'add':
                new.pop('email')
                cont.update({email: {i: new[i] for i in new}})
                return True
            if com == 'update':
                new.pop('email')
                if email not in cont:
                    cont[email] = {}
                    cont[email] = new
                else:
                    temp_con = []
                    temp_pas = []
                    res = []
                    for i in cont[email]:
                        temp_con.append(i)

                    for i in new:
                        temp_pas.append(i)

                    for i in temp_pas:
                        if i in temp_con:
                            pass
                        else:
                            res.append(i)

                    for i in new:
                        if i in res:
                            cont[email][i] = new[i]
                return True
        if com == 'delete':
            if email in cont:
                cont.pop(new.get('email'))
                return True
            else:
                return False
    else:
        return False

