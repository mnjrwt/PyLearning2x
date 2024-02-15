def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
#    print(rev_str)
    if str == rev_str:
        print(str, "is Palindrome:")
    else:
        print(str, "is not Palindrome.")
    return rev_str


original_str2 = input("Enter any string:\n")

reverse_string(original_str2)