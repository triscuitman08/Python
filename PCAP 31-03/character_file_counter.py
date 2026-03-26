letters = {}
file_name = input("What is the name of the file to check (full path including extension)?\n")

try:
    if file_name.split("."[1]) in ["txt","text","html","json","doc","docx","xslx","yaml"]:       
        try:
            file = open(file_name,"r")
        except IOError as e:
            print("Unable to open file you dipshit, make sure it actually exists. Moron")
            exit (e.errorno)
    
        file_line = file.readline()
        file_line_cnt = 0
        while file_line > 0:
            #foreach loop ch in file_line here
                
            file_line_cnt +=1

    else:
        print("Hey dipshit, we're counting characters over here.... send me a text file to gobble up!")
    
except:
    raise ("You've got a problem with your file! Try again!")
    exit