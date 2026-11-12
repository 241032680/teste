print("Hello world!")


i1 = {
    "tipo de inimigo": "leve",
    "hp" : 30,
    "velocidade": 6,
    "mísseis" : 3,
    "escudo": 10,
    #"tipo de missel": tipomissel(),
    #"tipo de escudo": tipoescudo(),
    #"tipo de dano": tipodano(),
  }

i2 = {"tipo" : "medio", 
"hp" : 60,
"escudo": 15}


i3 = {"tipo" : "pesado", 
"hp" : 110,
"escudo": 20}

inimigos = {"i1" : i1,
"i2" : i2,
"i3" : i3} 

inimigos["foo"] = {
"bar": 1,
"buzz": 2
}
#print(inimigos)

print(inimigos.get("foo").get("bar"))