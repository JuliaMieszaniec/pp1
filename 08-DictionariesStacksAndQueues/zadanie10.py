kraje=[
    {"country":"polska", "populacja": "40 mln"},
    {"country":"niemcy", "populacja": "45 mln"},
    {"country":"hiszpania", "populacja": "70 mln"},
    {"country":"argentyna", "populacja": "90 mln"},
    {"country":"włochy", "populacja": "140 mln"},
]

i=0
while i<len(kraje):
    for key, value in kraje[i].items():
        print(key," : ",value)
    i+=1