import socket
import requests
import pandas as pd

with open("seznam_website") as soubor:
    obsah = soubor.read()

seznam = obsah.split()
borci = []
hadi = []
IPhada = []
IPborce = []
TYPhada = []
TYPborce = []
PARborec= []

for x in seznam:
    if (socket.gethostbyname(x) == "IPaddress1") or (socket.gethostbyname(x) == "IPaddress2"):
        borci.append(x)        
        try:
            r = requests.get("http://" + x, verify=False)
            TYPborce.append(r.status_code)
            OBSAHborce = r.text

            if "PARKOVACÍ STRÁNKA UNIQUE STRING" in OBSAHborce:
                PARborec.append("Parkovací stránka")
            else:
                PARborec.append("Zákaznický web")

        except:
            TYPborce.append("Rozbito")
            PARborec.append("Rozbito")

    else:
        hadi.append(x)
        IPhada.append(socket.gethostbyname(x))        
        try:
            r = requests.get("http://" + x, verify=False)
            TYPhada.append(r.status_code)
        except:
            TYPhada.append("Connection Timed Out")

tabulka_hadu = {"doména": hadi, "IP adresa": IPhada, "Response Type": TYPhada} 
tabulka_borcu = {"doména": borci, "ResponseType": TYPborce, "Parkovač?": PARborec} 

ne = pd.DataFrame(tabulka_hadu)
ano = pd.DataFrame(tabulka_borcu)

ano.to_csv("seznamborcu-parking.csv", index=False)
ne.to_csv("seznamhadu-parking.csv", index=False)

print("DONEZO")
