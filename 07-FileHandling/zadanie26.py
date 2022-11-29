import re
f=open("tekst.txt","r", encoding='utf-8')
f_content = f.read()
print( f_content )

z=re.split("\s", f_content )


for word in z:
    if len(word)>5:
        print(word)

f.close()