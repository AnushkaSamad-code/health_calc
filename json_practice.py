import json
#dictionary
student_info = {
    "name" : "Annu",
    "course" : "BSCS",
    "semester" : "2"
}
with open("my_data.json","w") as f :
    json.dump(student_info , f , indent=4)

print("Check your folder! 'my_data.json' has been created in your folder")