#elem_list.py

ELEMENT = {
    'Gluant':{
        'Corrompu' : 1.5,
        'Haineux': 0.5,
        'Glitch' : 1.0
    },
    'Corrompu' : {
        'Gluant' : 0.5,
        'Haineux': 1.5,
        'Glitch' : 1.0
    },
    'Haineux' : {      #j'ai pas d'inspi kevin
        'Corrompu' : 0.5,
        'Gluant': 1.5,
        'Glitch' : 1.0
    },  
    'Glitch' : {
        'Corrompu' : 1.5,
        'Haineux': 1.5,
        'Gluant' : 1.5
    }
}