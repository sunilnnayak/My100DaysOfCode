# 

def format_name(f_name, l_name):
    print(f_name.title())               #https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python
    print(l_name.title())

format_name("sunil","SUNIL")

##
def format_name(f_name, l_name):
    formated_f_name=print(f_name.title())
    formated_l_name=print(l_name.title())

    print(f"{formated_f_name} {formated_l_name}")

format_name("sunil","SUNIL")

###
def format_name(f_name, l_name):
    formated_f_name=print(f_name.title())
    formated_l_name=print(l_name.title())

    return f"{formated_f_name} {formated_l_name}"
    #if we have print statement after return, it won't b execuited. Because return tells the computer that this is end of function
    #and to exit from function

formated_string=format_name("sunil","SUNIL")
print(formated_string)
# or print(format_name("sunil","SUNIL"))


####
#We can even have multiple return statements
def format_name(f_name, l_name):
    if f_name=="" or l_name=="":
        return
    formated_f_name=print(f_name.title())
    formated_l_name=print(l_name.title())

    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("what is first name? "),input("what is last name? ")))