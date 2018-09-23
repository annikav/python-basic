def ceasarEncode(word, key):
    encodedWord = ""
    for char in word:
        encodedWord += str(chr(ord(char) + key))
    return encodedWord

def ceasarDecode(word, key):
    encodedWord = ""
    for char in word:
        encodedWord += str(chr(ord(char) - key))
    return encodedWord

print("Encode the word github")

print(ceasarEncode("github", 2))
print(ceasarDecode(ceasarEncode("github", 2), 2))