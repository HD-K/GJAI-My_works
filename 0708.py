import json

with open('0708.json', encoding='UTF8') as json_stud:
    data = json.load(json_stud)
    stud_info = data["students"]


##학생 이름 전부 출력
def print_list_name():
    for index_num in range(len(stud_info)):
        print(stud_info[index_num]["name"])

#20세 미만의 학생을 추가
def append_member_under20(name, age, job, id, password):
    if (age < 20):
        data20 = {
            "students": [
                {
                "name": name,
                "age": age,
                "job": job,
                "id": id,
                "password": password
                }
            ]
        }
        with open("stud_under20.json", "w") as under20:
            json.dump(data20, under20, ensure_ascii=False)
        data
        stud_info += 

    else:
        print("20세 미만이 아닙니다.")

#20세 미만의 학생 출력
def print_list_name_under20():
    for index_num in range(len(stud_info)):
        if (stud_info[index_num]["age"] < 20):
            print(stud_info[index_num]["name"])

#print_list_name()
append_member_under20("김가람", 18, "학생", "ramram77", "77char")
#print_list_name_under20()
  
