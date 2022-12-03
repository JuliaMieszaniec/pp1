student_data={
    "name":"julia",
    "surname": "Mieszaniec",
    "age": 19,
    "study":{"university":"Uek", "course":"Computer science"},
    "subjects":["pp","ewd","tpi","wf","ask"],
    "female":True
}
import json
f=open("student.json","w")
json.dump(student_data,f,indent=4)
f.close()
