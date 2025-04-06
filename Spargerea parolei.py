special_characters_list = ["!", "@","#", "$"]

def is_valid(password):
    capitals = []
    lowercase = []
    digits = []
    specials = []
    for char in password:
        if char.isalpha():
            if char.islower():
                lowercase.append(char)
            else:
                capitals.append(char)
        elif char.isdigit():
            digits.append(char)
        elif char in special_characters_list:
            specials.append(char)
        else:
            return False
    return len(lowercase)== 3 and len(capitals)== 1 and len(digits)== 1 and  len(specials)== 1
#print(is_valid("Aaaa4$"))


import hashlib
def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

target_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"


#special_characters = "!@#$"
import random
import string
#def generate_password(password, special_characters, max_length=6, target_hash=None):
    #if len(password) == max_length:
        #if is_valid(password):
            #hashed = hashlib.sha256(password.encode()).hexdigest()
            #if hashed == target_hash:
                #print("Matching password found:", password)
                #exit()
        #return
    #for char in string.ascii_letters + string.digits + special_characters:
        #generate_password(password + char, special_characters, max_length, target_hash)

#generate_password("", special_characters, max_length=6, target_hash=target_hash)

# def generate_candidate_backtrack(length, current_str="", used_special=False):
#
#     if len(current_str) == length:
#         return current_str if is_valid(current_str) else None
#     possible_chars = list(string.ascii_letters + string.digits)
#     if not used_special:
#         possible_chars.append(random.choice(special_characters_list))
#         random.shuffle(possible_chars)
#         for char in possible_chars:
#            new_str = current_str + char
#            result = generate_candidate_backtrack(length, new_str, used_special or char in special_characters_list)
#            if result:
#                return result
#     return None
# random_string = generate_candidate_backtrack(6)
# if __name__ == "__main__":
#    print(random_string)
#
# candidate_hashed = get_hash(random_string)
# print(candidate)
#
# def check_hash(password):
#    while candidate:
#        if password == candidate:
#            print(f"Parola găsită:{random_string} ")
#            break
#        else:
#            random_string = generate_candidate_backtrack(6)
# check_hash(target_hash)

# def generate_candidate(result, memo={}):
#     if result in memo:
#         if get_hash(result) == target_hash:
#             return memo[result]
#     candidate = ""
#     uppers = list(string.ascii_letters.upper())
#     lowers = list(string.ascii_letters.lower())
#     nums = list(string.digits)
#     for i in range(uppers):
#         first = str(i)
#         characters_random = ''.join(random.choices(string.ascii_lowercase, k=3))
#         candidate = first + characters_random + str(random.choices(special_characters_list))+ str(random.choice(nums))
#         if is_valid(result):
#             final = generate_candidate(candidate)
#             if final:
#                 return final
#             memo[result] = -1
#         return None
#     result = [-1] * candidate
#     return generate_candidate(result, 0)
# print(generate_candidate(result))

# def generate_candidate(hashed_password):  #parola data in hash
#     def backtrack(result, hashed_candidate): # parola generata, aceeasi in hash
#         if hashed_candidate == hashed_password:
#             return result[:]

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "!@#$"

ALL_CHARS = LOWER + UPPER + DIGITS + SPECIAL

calls = 0
found = False

def backtrack(current, count_lower, count_upper, count_digit, count_special):
    global calls, found
    if found:
        return
    calls += 1

    if calls % 10000 == 0:
        print(f"Apeluri recursive: {calls}")

    if len(current) == 6:
        if is_valid(current):
            if get_hash(current) == target_hash:
                print("Parola găsită:", current)
                print("Număr apeluri recursive:", calls)
                found = True
        return

    if len(current) == 0:
        candidates = UPPER
    else:
        candidates = ALL_CHARS

    for char in candidates:
        if char in LOWER and count_lower >= 3:
            continue
        if char in UPPER and count_upper >= 1:
            continue
        if char in DIGITS and count_digit >= 1:
            continue
        if char in SPECIAL and count_special >= 1:
            continue

        backtrack(
            current + char,
            count_lower + (char in LOWER),
            count_upper + (char in UPPER),
            count_digit + (char in DIGITS),
            count_special + (char in SPECIAL)
        )

backtrack("", 0, 0, 0, 0)