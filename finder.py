def input_chars(s, l = 5):    
    chars = list(input(s).split())
    if len(chars) > l:
        print(f'''More than {l} character. Retry \n''')
        chars.clear()
        return input_chars(s, l)
    return chars

guess_list = []

try:
    with open('wordlist.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("file not found")

safe_chars =  input_chars("Enter the good alphabets (Space seperated) \n")

unsafe_chars =  input_chars("Enter the bad alphabets (Space seperated) \n", 26)

yellow_chars =  input_chars("Enter the yellow alphabets (Space seperated) (non-yellow to be marked as 0) (Example: W 0 T E 0) \n", 5)

green_chars =  input_chars("Enter the green alphabets (Space seperated) (non-green to be marked as 0) (Example: W 0 T E 0) \n", 5)

temp_tuple = tuple(guess_list)

for word in temp_tuple:
    for x in unsafe_chars:
        if x in word:
            guess_list.remove(word)
            break

temp_tuple = tuple(guess_list)

for word in temp_tuple:
    count = 0
    for x in safe_chars:
        if x in word:
            count+=1
    if count != len(safe_chars):
        guess_list.remove(word)

temp_tuple = tuple(guess_list)

for word in temp_tuple:
    for y in range(len(green_chars)):
        if green_chars[y] != '0' and green_chars[y] != word[y]:
            guess_list.remove(word)
            break

temp_tuple = tuple(guess_list)

for word in temp_tuple:
    for y in range(len(yellow_chars)):
        if yellow_chars[y] != '0' and yellow_chars[y] == word[y]:
            guess_list.remove(word)
            break

print(guess_list)