def f(first_letter,last_letter) :
    file=open("test.txt","r")
    content=file.read()
    import re
    x = re.search("^first_letter.*last_letter$", content)
    print(x)
    file.close()

f("w", "d") 