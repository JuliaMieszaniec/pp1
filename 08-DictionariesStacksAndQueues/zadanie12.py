favourite_book={
    "nazwa": "Tamte dni tamte noce",
    "autor": "Andre Aciman",
    "rok_wydania": 2007,
    "postacie":["Oliver","Elio"],
    "gatunek": "dramat",
    "zagraniczny_autor": True
    }
import json
out_file=open("film.json", "w")
json.dump(favourite_book, out_file, indent=4 )
out_file.close()