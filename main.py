#test une fonction pour la somme

def calc_somme(v1,v2):
    s=0
    s=v1+v2
    return s


v=int(input("doner la valeur 1 : "))
vv=int(input("donner la valeur 2 : "))
print("la somme est : ",calc_somme(v,vv))