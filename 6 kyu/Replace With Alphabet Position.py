def alphabet_position(text):
    alfabeto = 'abcdefghijklmenopqrstuvwxyz'
    return ' '.join([str(alfabeto.find(x) + 1) for x in text.lower() if x in alfabeto])