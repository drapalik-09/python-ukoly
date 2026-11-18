import urllib.request
URL = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"
odpoved = urllib.request.urlopen(URL)
pocet_dnu= 0
celkem_srazky= 0
radek= odpoved.readline()

while bool(radek):
    text = radek.decode("utf-8").strip()
    srazka = float(text)
    if srazka > 0:
        celkem_srazky += srazka
        pocet_dnu += 1
    radek= odpoved.readline()
odpoved.close()
print(celkem_srazky/pocet_dnu)