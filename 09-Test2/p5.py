def f(first_letter,last_letter) :
    import re
    file=open("test.txt","r", encoding="utf-8")
    content=file.read()
    content=re.split("\W",content)
    count=0
    for i in content:
        if (re.match(f"^{first_letter}\w*{last_letter}$",i)):
            count+=1
    print(count)
    #x = re.search(f"^{first_letter}.*{last_letter}$", content)
    #print(x)
    file.close()

f("w", "d") 
