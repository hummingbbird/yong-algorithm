word = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
changed = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

for s in word:
    print(alphabet[changed.index(s)], end='')