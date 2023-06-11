# define list for store data 
student=[]

def add():
    id = int(input("please insert id : "))
    name = input("please insert name : ")
    fname = input("please insert family name : ")
    year = int(input("please insert year : "))
    field = int(input("1.computer 2.Civil 3.agriculture 4.electrical 5.mechanic\nplease insert integer of top field : "))
    information = {"id" : id ,"name":name, "fname" : fname ,"year":year  , "field": field}
    
    if 1000000 <= id <= 9999999 :
        if 1000 <= year <= 9999 :
            if  1 <= field <= 5 :
                student.append(information)
                print("student add successfully ...")
            else:
                print("Error : field must be in range [1 - 5] ")
        else:
            print("Error : invalid year range !")
    else:
        print("Error : id must be 7 character !")
    
    

def search_by_id(id):
    flag= False
    for i in student:
        if(i['id'] == id):
            flag = True
            print(i)
    if flag == False :
        print("student not found !")


def delete(id):
    flag = False
    for i in range(len(student)):
        if student[i]['id']== id :
            del student[i]
            flag= True
    if flag == False:
        print("student not found !")


def edit(id):
    flag = False
    for i in range(len(student)):
        if student[i]['id']== id :
            flag =True
            for key , value in student[i].items():
                print("this is the key , value -> " , key , " : ", value)
                is_edit=input("if you want to edit -> 1    else -> any character \n your choice is : ")
                if is_edit == "1":
                    if key == 'id' or key == 'year':
                        new_val=int(input("insert new value : "))
                        student[i][key]=new_val
                        print(f"{key} changed with new value : {new_val}")
                    else:
                        new_val=input("insert new value : ")
                        student[i][key]=new_val
                        print(f"{key} changed with new value : {new_val}")
    if flag == False:
        print("student not found !!!")    
    
def show():
    for i in student:
        print(i)



while(True):
    file=open("data.txt" , "w+")
    file.write(str(student))
    file.close()
    menu=int(input("1.add\n2.search by id\n3.edit\n4.delete\n5.show\n6.exit\nyour choice is : "))
    if menu == 1:
        add()
    elif menu == 2:
        id=int(input("please insert id for search : "))
        search_by_id(id)
    elif menu == 3:
        id=int(input("please insert id for search : "))
        edit(id)
    elif menu == 4 :
        id=int(input("please insert id for search : "))
        delete(id)
    elif menu == 5:
        show()
    elif menu == 6:
        print("the end .")
        break
    else:
        print("try again.  invalid choice !! ")