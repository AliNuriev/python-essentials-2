text = input('Enter your message: ')
cipher = ''

for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if char == "Z":
        code = ord('A')
    cipher += chr(code)

print(cipher,end = '\n\n')

# -----------------------------------------#

cipher = input('Enter your cryptoprogram: ')
text = ''

for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1

    if char == 'A':
        code = ord('Z')
    text += chr(code)

print(text, end = '\n\n')

# -----------------------------------------#

num_str = input('Enter numbers with spaces: ')
nums = num_str.split()
total = 0
try:
    for num in nums:
        total += float(num)
    print('total is: ', total)
except:
    print(nums, 'this is not a number')

print(end = '\n\n')

#-----------------------------------------#

iban = input('Enter valid IBAN number: ')
iban = iban.replace(' ', '')

if not iban.isalnum():
    print('You have entered invalid characters!')
elif len(iban) < 15:
    print('IBAN is too short')
elif len(iban) > 31:
    print('IBAN is too long')
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for char in iban:
        if char.isalpha():
            iban2 += str(10 + ord(char) - ord('A'))
        else:
            iban2 += char
    iban = int(iban2)
    if iban % 97 == 1:
        print('Your IBAN is valid')
    else:
        print('Your IBAN is invalid')


print(end = '\n\n')

# -----------------------------------------##

palindrome = input('Enter a word: ')

palindrome = palindrome.replace(' ', '')

if len(palindrome) >= 3 and palindrome.upper() == palindrome[::-1].upper():
    print('The word is palindrome')
else:
    print('fuck off')

print(end = '\n\n')

# -----------------------------------------#

word1 = str(input('Enter the first word: '))
word2 = str(input('Enter the second word: '))

word1 = word1.replace(' ', '').lower()
word2 = word2.replace(' ', '').lower()


if word1.isalpha() and word2.isalpha():
    if sorted(word1) == sorted(word2):
        print('Anagrams')
    else:
        print('Not at all')

else:
    print('Enter a word')

print(end = '\n\n')

# -----------------------------------------#


d_o_b = (input('Enter you DoB in YYYYMMDD, or YYYYDDMM, or MMDDYYYY format: '))

if len(d_o_b) < 8 and not d_o_b.isdigit():
    print('Invalid format bro')
else:
    while len(d_o_b) > 1:
        sum = 0
        for d in d_o_b:
            sum += int(d)
        print(d_o_b)
        d_o_b = str(sum)

    print('Your Digit of Life is', d_o_b)

print(end = '\n\n')

# -----------------------------------------#

word1 = input('Enter the word we are searching for: ').lower()
word2 = input('Enter the word where we are searching for word1: ').lower()

found = True
start = 0

for char in word1:
    pos = word2.find(char, start)
    if pos == -1:
        found = False
        break
    start = pos + 1
if found:
    print('Yes')
else:
    print('No')



