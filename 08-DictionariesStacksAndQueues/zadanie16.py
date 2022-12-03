import shutil


f=open("studentsdata.json", "w")
z=open('dane.json','r')

shutil.copyfile('studentsdata.json','dane.json')


z.close()
f.close()