import requests,json

while True:
    A = input("""
        1.Regsiter new student
        2.Edit Student details
        3.Delete Student
        4.Export Students to text file
        5.Export Student details to text
        6.Exit
        Enter Number : """)
    if (A == '1'):
        full_name = input("Enter Full Name :")
        age = input("Enter Age :")
        level = input("Enter Level (A-B-C) :")
        mobile_number = input("Enter Mobile Number : ")
        url = 'http://staging.bldt.ca/api/method/build_it.test.register_student'
        myobj = {'full_name': full_name,
                 'age': age,
                 'level': level,
                 'mobile_number': mobile_number
                 }
        x = requests.post(url, json=myobj)
        print(x.text)
    if (A == '2'):
        ID = input("Enter ID Student : ")
        full_name = input("Enter Full Name :")
        age = input("Enter Age :")
        level = input("Enter Level (A-B-C) :")
        mobile_number = input("Enter Mobile Number : ")
        url = 'http://staging.bldt.ca/api/method/build_it.test.edit_student'
        myobj = {'id': ID,
                 'full_name': full_name,
                 'age': age,
                 'level': level,
                 'mobile_number': mobile_number
                 }
        x = requests.post(url, json=myobj)
        print(x.text)
    if (A == '3'):
        ID_delet = input("Enter ID Delete : ")
        url = 'http://staging.bldt.ca/api/method/build_it.test.delete_student'
        myobj = {'id': ID_delet}
        x = requests.post(url, json=myobj)
        print(x.text)
    if (A == '4'):
        res = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
        data = json.loads(res.text)
        f = open("Students.txt", "a")
        f.write(str(data))
        f.close()
    if (A == '5'):
        ID = input("Enter ID Get : ")
        url = 'http://staging.bldt.ca/api/method/build_it.test.get_student_details'
        myobj = {'id': ID}
        data = requests.post(url,json=myobj)
        print(data.text)
        f = open("Student.txt", "a")
        f.write(str(data.text))
        f.close()
    if A =='6':
        exit()
