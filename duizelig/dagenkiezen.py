tijd = 0
dag = ["ma","di","wo","do","vr","za","zo"]
while True:
    dagkies =input("Type een dag van de week ma,di,wo,do,vr,za,zo: ")
    if dagkies in dag:
        break
    else:
        print("das geen dag")   
while True:
    if dagkies != dag[tijd]:
        print(dag[tijd])
    else:
        print(dag[tijd])
        break  
    tijd+=1

input('Press ENTER to exit')