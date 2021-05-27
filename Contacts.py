contacts = {
    "number":4,
    "student":
    [
        {"name":"Vo Nhat Cuong 1", "email":"Vonhatcuong1@gmail.com"},
        {"name":"Vo Nhat Cuong 2", "email":"Vonhatcuong2@gmail.com"},
        {"name":"Vo Nhat Cuong 3 ", "email":"Vonhatcuong3@gmail.com"},
        {"name":"Vo Nhat Cuong 4", "email":"Vonhatcuong4@gmail.com"}
    ]
}

for student in contacts["student"]:
    print(student["name"])