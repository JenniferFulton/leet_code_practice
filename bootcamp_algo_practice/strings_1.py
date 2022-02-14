# Remove Blanks
# Create a function that, given a string, returns all of that string’s contents, but without blanks. 
# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

def rm_blank(string):
    new_string = string.replace(" ","")
    return(new_string)

print(rm_blank("hell o wo r ld"))

# Get Digits
# Create a Python function that given a string, returns the integer made from the string’s digits. 
# Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.

def get_digits(string):
    new_string = ""
    for character in string:
        if character.isdigit() == True:
            new_string += character
    return(int(new_string))

print(get_digits("hjkh6gyg3ljl1ljklhjk0bjb543210"))

# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 
# Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
# Given "Live from New York, it's Saturday Night!", return "LFNYISN".

def acronym(string):
    cap_string = string.title()
    acro = ""
    for char in cap_string:
        if char.isupper() == True:
            acro += char
    return (acro)

print(acronym("jennifer loves the ocean"))

# Zip Arrays into Map
# Associative arrays are sometimes called maps because a key (string) maps to a value. 
# Given two arrays, create an associative array (map) containing keys of the first, and values of the second. 
# For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

def zip_array(arr1,arr2):
    dict = {}
    for key, value in zip(arr1, arr2):
        dict[key] = value
    return (dict)

print(zip_array(["abc", 3, "yo"],[42, "wassup", True]))

# Invert Hash
# Associative arrays are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. 
# Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

def invert(dictionary):
    for key in dictionary.items():
        print(key)
    # return (dictionary)

print(invert({"name": "Zaphod", "charm": "high", "morals": "dicey"}))



