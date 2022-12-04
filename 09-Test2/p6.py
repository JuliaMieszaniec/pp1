def f(age, course, average) :
    import json
    import math
    count=0
    file=open("test.json","r")
    content=json.load(file)
    for i in content:
        for j in i["studies"]["courses"]:
            if j["name"]==course:
                if sum(j["grades"])/len(["grades"])>=average and i["age"]>=age:
                    count+=1
    print(count)

    #if file["age"]>age:

    file.close()

f(21, "statistics", 4) 