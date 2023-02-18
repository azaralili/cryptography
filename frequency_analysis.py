import string # module for string cosntants
import urllib.request # module for openning the URL

# In case file in local machine
    #file_name = r'C:\..\..\..\cipher.txt'
    # with open(file_name, 'r') as file:
    #     contents = file.read()
    #encrypted_text = contents

# Downloading the encrypted text file
url = "http://www.phanivadrevu.com/files/teaching/cipher.txt"
response = urllib.request.urlopen(url)
encrypted_text = response.read().decode()
print("Encrypted text:", encrypted_text)

# Here we have to define the character set and frequency table for English language
charset = string.ascii_lowercase + "\"',-.; "
freq_table = {'e': 12.70,
              't': 9.06,
              'a': 8.17,
              'o': 7.51,
              'i': 6.97,
              'n': 6.75,
              's': 6.33,
              'h': 6.09,
              'r': 5.99,
              'd': 4.25,
              'l': 4.03,
              'u': 2.76,
              'c': 2.78,
              'm': 2.41,
              'w': 2.36,
              'f': 2.23,
              'g': 2.02,
              'y': 1.97,
              'p': 1.93,
              'b': 1.50,
              'v': 0.98,
              'k': 0.77,
              'j': 0.15,
              'x': 0.15,
              'q': 0.10,
              'z': 0.07,
              ' ': 18.0,
              '"': 1.0,
              "'": 1.0,
              ',': 1.0,
              '-': 1.0,
              '.': 1.0,
              ';': 1.0}

# Here we can calculate the frequencies in the ciphertext for letter and symbols
char_freq = {}
for char in encrypted_text:
    if char in charset:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

# This is for soring the character frequencies in descending order
sorted_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
#print(sorted_freq) # By uncommenting here we can see the number of letters in ciphertext
# Next step is to map between the most frequent characters in the ciphertext
                  # and the most frequent characters in the English language
key = ""
for i in range(len(sorted_freq)):
    if sorted_freq[i][0] == ' ':
        key += ' '
    else:
        key += freq_table.popitem()[0]

# Decrypt the text using the key
plaintext = ""
for char in encrypted_text:
    if char not in key:
        plaintext += char
    else:
        #plaintext += charset[freq_table.get(key[key.find(char)], -1)]
        plaintext += charset[key.index(char)]

# Here we can the palintext and the key
print("Plaintext: " + plaintext)
print("Key: " + key)


