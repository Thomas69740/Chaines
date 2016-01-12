# coding: utf-8

def hasSeries(password):
    return False
def hasTwoPairs(password):
    return False
def hasNoBadChar(password):
    return False
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