#status_list.py

STATUS = {
    'poison' : {
        'name' : "Poison",
        'amount' : 0.05,
        'duration' : 4 #On mettra -1 (infini) lorsqu'on aura implémenté les soins de statut (via objet ou compétences peut importe)
    },
    'burn' : {
        'name' : "Brûlure",
        'amount' : 0.08,
        'duration' : 4 #Idem ici
    },
    'sleep' : {
        'name' : "Endormi",
        'chance_to_stop' : 0.50,
        'duration' : 3
    }
}