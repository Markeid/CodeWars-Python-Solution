def disemvowel(string):
    vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    lista = list(string)
    for x in lista:
        if x in vogais:
            lista.remove(x)
    string = ''.join(lista)
    return string

# 2ª solução #
def disemvowel(string):
    return "".join([ch for ch in string if ch not in "aeiouAEIOU"])

# 3ª solução #
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")