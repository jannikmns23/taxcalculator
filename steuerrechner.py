#Einkommen angeben
print("Bitte zu versteuerndes Einkommen in Euro eingeben:")

einkommen=input()
einkommen=float(einkommen)

#Steuersatz anwenden
if(einkommen<=5000):
    print("Ihr Einkommen ist steuerfrei.")

elif (einkommen>=5000) and (einkommen<=20000):
    steuern=einkommen*0.22
    print("Auf ihr Einkommen werden", steuern,"Euro Steuern erhoben.")

elif(einkommen>=20000):
    stufe=einkommen-20000
    #print(stufe)
    x=stufe//5000
    #print(x)
    multiplikator=x+1
    #print(multiplikator)
    steuersatz=multiplikator*0.03+0.22
    #print(steuersatz)
    steuern=einkommen*steuersatz
    print("Auf Ihr Einkommen werden", steuern,"Euro erhoben.")

else:
    print("Bitte eine korrekte Eingabe tätigen!")


    

    
