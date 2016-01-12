# coding: utf-8

def hasSeries(password):
    pwd = list(password)
    i = len(pwd)-1
    count = 0
    while i >= 0:
        if count == 0:
            currentChar = pwd[i]
        if currentChar == pwd[i]:
            count += 1
        else:
            count = 0
        if count == 3:
            return True
        i += 1
    return False

def hasTwoPairs(password):
    pwd = list(password)
    i = len(pwd)-1
    count = 0
    pair1, pair2 = False
    while i >= 0:
        if count == 0:
            currentChar = pwd[i]
        if currentChar == pwd[i]:
            count += 1
        else:
            count = 0
        if count == 2 and pair1 == False:
            pair1 = True
        if count == 2 and pair1 == True:
            pair2 = True
        i += 1
    if pair1 == True and pair2 == True:
        return True
    else:
        return False

def hasNoBadChar(password):
    found = False
    i=len(password)-1
    while found == False:
        if password[i] == 'i' or password[i] == 'o' or password[i] == 'l':
            found = True
        else:
            found = False
        if i > 0:
            i -= 1
        else:
            return found

def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  # Permet de créer un tableau contenant les caractères de la chaine password
    found = False
    i=len(pwd)-1
    if i == -1:
        raise ValueError("Chaîne vide")
    while not found:
        if pwd[i] < 'z':
            pwd[i] = chr(ord(pwd[i])+1)  # ord() renvoi la valeur ASCII d'un caractère, on ajout 1 à cette valeur, chr() permet de convertir cet valeur en char
            found = True
        else:
            pwd[i] = 'a'
            i -= 1
            if i == -1:
                raise ValueError("Longueur de chaîne invalide")

    return ''.join(pwd) # On renvoi au minimum une chaine vide, avec le password à la suite


# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également.
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous.
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py"
#  en console.
if __name__ == "__main__":
    import doctest
    doctest.testmod()