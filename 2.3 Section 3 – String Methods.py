# capitalize - First letter is an upper-case
print('aBcD'.capitalize())
print(' Alpha'.capitalize())
print("αβγδ".capitalize(), end = "\n\n")

# centers the string inside a specified width
print('[' + 'alpha'.center(20) + ']')
print("[" + "beta".center(12, "*") + ']', end = "\n\n")

# endswith() checks if the given string ends with the specified argument and returns True or False
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"), end = '\n\n')

# find() it looks for a substring and returns the index of the first occurrence of this substring, but:
# it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)

print("Eta".find('ta'))
print("Eta".find("mma"))

# The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 2)

#  the third argument points to the first index which won't be taken into consideration during the search
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4),  end = '\n\n')

# isalnum() - checks if the string contains only digits or alphabetical characters (letters)

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())

t = 'Six lambdas'  # space is nor digit nor letter
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum(), end = '\n\n')

# isalpha() - letters only

print("Mooooo".isalpha())
print('gay228'.isalpha(), end = '\n\n')

# isdigit() - digits only

print('2018'.isdigit())
print("Year2019".isdigit(), end = '\n\n')


# islower() - lower-case letters only

print("Moooo".islower())
print('moooo'.islower(), end = '\n\n')

# isspace() whitespaces only
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace(), end = '\n\n')

# isupper() upper-case only

print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper(), end = '\n\n')

# join() ',' - separator
print(",".join(["omicron", "pi", "rho"]), end = '\n\n')

# lower() - makes all of them lower-case
print("SiGmA=60".lower(), end = '\n\n')

# lstrip() without param removes leading whitespaces
print("[" + "    tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))
# То есть lstrip("w.") - это не "удали префикс 'w.'", а "удали все символы 'w' и '.' из начала, пока они встречаются

print("pythoninstitute.org".lstrip(".org"), end = '\n\n')
# none of .org symbols at the beginning - so result is the same

# replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2),  end = '\n\n')

# rfind() - same as find() but from the end
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3,9), end = '\n\n')
# 9 НЕ ВКЛЮЧАЕМ

# rstrip()
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"), end = '\n\n')

# split()  - substrings are delimited by space - results list with substrings
print("phi chi psi".split(), end = '\n\n')

# startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"), end = '\n\n')

# strip() - combined rstrip() and lstrip()
print("[" + "   aleph   ".strip() + "]", end = '\n\n')

# swapcase() - lower to upper and vice versa
print("I know that I know nothing.".swapcase(), end = '\n\n')

# title() - every word starts with upper case
print("I know that I know nothing. Part 1.".title(), end = "\n\n")

# upper() method - all upper case
print("I know that I know nothing. Part 2.".upper(), end = "\n\n")


# ------------------------------------- #

def mysplit1(strng):
    if strng == "" and strng.isspace():
        return []

    words = []
    current_word = ""

    for char in strng:
        if char.isspace():
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    return words

print(mysplit1("To be or not to be, that is the question"))
print(mysplit1("To be or not to be,that is the question"))
print(mysplit1("   "))
print(mysplit1(" abc "))
print(mysplit1(""))