def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = [char for char in sentence if char in alphabet]
    return set(sentence) == set('abcdefghijklmnopqrstuvwxyz')
