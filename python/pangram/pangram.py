def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = [char for char in sentence.lower() if char in alphabet]
    return set(sentence) == set(alphabet)
