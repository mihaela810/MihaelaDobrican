import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit: " + " ".join(progres))
print(f"Încercări rămase: {incercari_ramase}\n")

while incercari_ramase > 0 and "_" in progres:
    litera = input("Introdu o literă: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă validă.\n")
        continue

    if litera in litere_incercate:
        print(f"Ai încercat deja litera '{litera}'. Mai încearcă o dată.\n")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        print(f"Bravo! Litera '{litera}' este în cuvânt.")
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
    else:
        incercari_ramase -= 1
        print(f"Îmi pare rău, litera '{litera}' nu este în cuvânt. Încercări rămase: {incercari_ramase}")

    print("Cuvântul de ghicit: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}\n")

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")