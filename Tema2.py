articol = """Sâmbătă, 19 octombrie 2024, Radu Drăgușin (22 de ani) a văzut doar de pe banca de rezerve duelul Tottenham – West Ham 4-1, din etapa 8 a Premier League, și imediat după fluierul final s-a vehiculat că ar fi tentat să se transfere la o altă echipă.\n O serie de echipe din Italia, între care și Napoli, îl monitorizează intens. Cu toate acestea, jucătorul în vârstă de 22 de ani îi rămâne fidel lui Tottenham și nu va căuta să se transfere la mijlocul sezonului, chiar dacă nu va primi minutele dorite. Cristian Romero și Micky van de Ven rămân perechea de fundași centrali ideală pentru Ange Postecoglou, dar există încredere că Radu Drăgușin va primi în continuare șanse atât în Europa, cât și în cupe. Surse apropiate jucătorului indică faptul că internaționalul român, care a marcat recent pentru țara sa, în victoria cu Cipru, scor 3-0, se concentrează doar pe a arăta de ce este capabil în teren, încercând să demonstreze că merită un post de titular”, notează jurnaliștii de la Mirror."""
lungime = len(articol)
jumatate = lungime//2
print(jumatate)
prima_parte = articol[0:jumatate]
majuscule = prima_parte.upper()
print(majuscule)
fara_spatiu = prima_parte.strip()
print(fara_spatiu)
a_doua_parte = articol[jumatate:]
print(a_doua_parte)
inversate = articol[jumatate:0:-1]
print(inversate)
litere_mari = a_doua_parte.title()
print(litere_mari)
import string
fara_semne = a_doua_parte.translate(str.maketrans('', '', string.punctuation))
print(fara_semne)
rezultat = fara_spatiu+fara_semne
print(rezultat)