meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

while studenti:
    student1= studenti.pop(0)
    comanda1= comenzi.pop(0)
tavi.pop()
print(f"Studentul {student1} a comandat {comanda1}.")
print('S-au comandat 1 guias, 3 ceafa, 1 papanasi.')
print("Mai sunt 5 tavi.")

for i in range(len(studenti)) :
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f"Studentul {student} a comandat {comanda}. ")
    print(studenti)
    print(comenzi)
    istoric_comenzi.append([student, comanda])
    tavi.pop()

guias_inceput = meniu.count('guias')
guias_comanda = 1
pret_guias = 5
castig_guias = guias_comanda * pret_guias
guias_disponibil = (guias_inceput - guias_comanda)
print(castig_guias)
print(guias_disponibil)
if guias_disponibil > 0 :
    print("Mai este guias: True")
else:
    print("Mai este guias: False")
papanasi_inceput = meniu.count('papanasi')
papanasi_comanda = 1
pret_papanasi = 7
castig_papanasi = papanasi_comanda * pret_papanasi
papanasi_disponibili = (papanasi_inceput - papanasi_comanda)
print(castig_papanasi)
print(papanasi_disponibili)
if papanasi_disponibili > 0 :
    print("Mai sunt papanasi:True")
else:
    print("Mai sunt papanasi:False")
ceafa_inceput = meniu.count('ceafa')
ceafa_comanda = 3
pret_ceafa = 10
castig_ceafa = ceafa_comanda * pret_ceafa
ceafa_disponibila = (ceafa_inceput - ceafa_comanda)
print(castig_ceafa)
print(ceafa_disponibila)
if ceafa_disponibila > 0 :
    print("Mai este ceafa:True")
else:
    print("Mai este ceafa: False")
total_castiguri = castig_guias + castig_papanasi + castig_ceafa
print(total_castiguri)
for i in range(len(studenti)) :
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f"{student} a comandat {comanda}")
mancare_ieftina = []

for mancare_pret in preturi:
    pret_mancare = mancare_pret[1]
    nume_mancare = mancare_pret[0]
    if pret_mancare <= 7 :
        mancare_ieftina.append(nume_mancare)
print(mancare_ieftina)
print(len(mancare_ieftina))
