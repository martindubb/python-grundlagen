import string

def is_palindrome(word):
    print(word)
    # alles in kleinbuchstaben konvertieren
    word = word.lower()
    # print("DEBUG", word)

    # leerzeichen entfernen
    word = word.replace(" ", "")
    # print("DEBUG", word)
    
    # satzzeichen entfernen
    word = word.translate(str.maketrans('', '', string.punctuation))
    # print("DEBUG", word)
    
    
    # einzelne buchstanben vergleichen
    for i in range(len(word)):
        if(word[i] != word[len(word)-i-1]):
            return False

    return True


####
print(is_palindrome("RACE   CAR      "))
print(is_palindrome("racecar"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))
print(is_palindrome("reliefpfeiler"))
print(is_palindrome("lageR regaL"))
