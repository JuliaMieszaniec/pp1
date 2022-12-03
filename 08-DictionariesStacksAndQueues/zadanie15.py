import json

f=open("icao.txt","w")
dictionary={
    "a":"alfa",
    "b":"bravo",
    "c":"charlie",
    "d":"delta",
    "e":"echo",
    "f":"foxtrot",
    "g":"golf",
    "h":"hotel",
    "i":"india",
    "j":"juliett",
    "k":"kilo",
    "l":"lima",
    "m":"mike",
    "n":"november",
    "o":"oscar",
    "p":"papa",
    "q":"quebec",
    "r":"romeo",
    "s":"sierra",
    "t":"tango",
    "u":"uniform",
    "v":"victor",
    "w":"whiskey",
    "x":"xray",
    "y":"yankee",
    "z":"zulu"
}
f.write(json.dumps(dictionary,indent=4))
f.close()