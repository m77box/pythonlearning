def count_unique_characters(s):
    #create a empty string
    txt = set()  #create a empty set by useing x = set()
    for i in s:
        #it sets the value of the variable 'unique_char' to 'True'
        #this is an assignment statement
        unique_char = True
        new_i = i.lower()
        if new_i == " ":
            continue
        for j in txt:
            if j == new_i:
               unique_char = False
        #"==" is a comparison operation, it checks if the value of 'unique_char'
        # is equal to "True"
        if unique_char == True:
            txt.add(new_i)
    return len(txt)

    # Convert the string to lowercase
    # Use a set to store unique alphabetic characters
    # Return the size of the set
text = "lilylily"
print(count_unique_characters(text))
# print(count_unique_characters("Hello, World!"))

# Expected: 7 (Unique characters are: h, e, l, o, w, r, d)