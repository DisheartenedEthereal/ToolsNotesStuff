import re
def validate(pattern):
    user_input = input("Input an email:")
    if re.search(patt,user_input):
        print("Validated with pattern :"+pattern)
    else:
        print("Invalid with pattern: "+pattern)
mode = input("Select mode: GMAIL|ANY|PROTONMAIL|CUSTOM\n ~>")
if mode == "ANY":
    patt = "[a-zA-Z0-9]+@[a-zA-z]+\.(com|edu|net)"
    validate(patt)
elif mode == "GMAIL":
    patt = "[a-zA-Z0-9]+@gmail\.com"
    validate(patt)
