def f():
    file=open("proba.txt","r",encoding="utf-8")
    #content=file.read()
    import re
    for line in file:
        if(re.match(".*c.*",line)):
            print(line)
        else:
            break

    #sum=0
    #for line in content:
      #  if c in line:
          #  sum+=1
    #for count, line in enumerate(content):
     #    if c in line:
      #      sum+=1

    #print(sum)
    file.close()

f()
