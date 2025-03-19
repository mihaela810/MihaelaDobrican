import random
import csv
import tkinter as tk
from tkinter import ttk
from collections import defaultdict


weight = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

male_names = ["Ion", "Alexandru", "Andrei", "George", "Vasile", "Vlad", "Marin"]
female_names = ["Maria", "Elena", "Ana", "Ioana", "Gabriela", "Anca", "Meda"]
last_names = ["Popescu", "Ionescu", "Vasilescu", "Dumitrescu", "Matache", "Stan", "Matei", "Radu", "Popa", "Bălan", "Dinicu", "Pop"]



counties = {
    "Alba": 1, "Arad": 2, "Argeș": 3, "Bacău": 4, "Bihor": 5, "Bistrița-Năsăud": 6, "Botoșani": 7,
    "Brașov": 8, "Brăila": 9, "Buzău": 10, "Caraș-Severin": 11, "Cluj": 12, "Constanța": 13,
    "Covasna": 14, "Dâmbovița": 15, "Dolj": 16, "Galați": 17, "Gorj": 18, "Harghita": 19,
    "Hunedoara": 20, "Ialomița": 21, "Iași": 22, "Ilfov": 23, "Maramureș": 24, "Mehedinți": 25,
    "Mureș": 26, "Neamț": 27, "Olt": 28, "Prahova": 29, "Satu Mare": 30, "Sălaj": 31, "Sibiu": 32, "Suceava": 33, "Teleorman": 34,
    "Timiș": 35, "Tulcea": 36, "Vaslui": 37, "Vâlcea": 38, "Vrancea": 39, "București": 40, "Călărași": 51, "Giurgiu": 52
}

procente = [0.0171, 0.0213, 0.0288, 0.0298, 0.0286, 0.0145, 0.02, 0.0286, 0.0167, 0.0218, 0.0130, 0.0354, 0.0328, 0.0102, 0.0245, 0.0315, 0.0259, 0.0162, 0.0155, 0.0192, 0.0132, 0.0397, 0.0283, 0.0240, 0.0119, 0.0270, 0.0245, 0.0193, 0.0327, 0.0172, 0.0109, 0.0207, 0.0331, 0.0175, 0.0356, 0.0101, 0.0195, 0.0185, 0.0162, 0.0895, 0.0149, 0.0138 ]

genders = {
    "bărbat": 0.49,
    "femeie": 0.51
}

ages = {
    "0-14": 0.18,
    "15-29": 0.22,
    "30-44": 0.24,
    "45-59": 0.18,
    "60+": 0.18
}

def choose_county():
    county_name = random.choices(list(counties.keys()), weights=procente, k=1)[0]
    return county_name, counties[county_name]

def choose_gender():
    gender = random.choices(list(genders.keys()), list(genders.values()))
    return gender[0]

def choose_age():
    age = random.choices(list(ages.keys()), list(ages.values()))
    return age[0]

def get_random_day(year, month):
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 != 0):
            max_day = 29
        else:
            max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
    return max_day


def generate_cnp():
    county_name, county_code = choose_county()
    gender = choose_gender()
    age_group = choose_age()

    if age_group == "0-14":
        year = random.randint(2010, 2025)
    elif age_group == "15-29":
        year = random.randint(1995, 2009)
    elif age_group == "30-44":
        year = random.randint(1980, 1994)
    elif age_group == "45-59":
        year = random.randint(1965, 1979)
    else:
        year = random.randint(1930, 1964)

    month = random.randint(1, 12)
    day = random.randint(1, get_random_day(year, month))

    if year >= 2000:
        sex_num = 5 if gender == "bărbat" else 6
    else:
        sex_num = 1 if gender == "bărbat" else 2

    #try:
       # birthdate = f"{str(day).zfill(2)}{str(month).zfill(2)}{str(year)[-2:]}"
    #except ValueError:
       # return None

    specifics_n = random.randint(1, 999)
    day_str = f"{day:02}"
    month_str = f"{month:02}"
    year_str = f"{year:02}"
    county_code_str = f"{county_code:02d}"
    partial_cnp = f"{sex_num}{year_str[2:4]}{month_str}{day_str}{county_code_str}{specifics_n:03}"
    suma = 0

    for i in range(len(partial_cnp)):
        suma += int(partial_cnp[i]) * weight[i]
    c = suma % 11
    c = 1 if c == 10 else c

    #first_name = random.choice(male_names) if sex_num in [1, 5] else random.choice(female_names)
    #last_name = random.choice(last_names)

    final_cnp = partial_cnp + str(c)
    return final_cnp

def validare_cnp(final_cnp):
    if len(final_cnp) != 13 or not final_cnp.isdigit():
        return False
    sum = 0
    for i in range(len(final_cnp) - 1):
        sum += int(final_cnp[i]) * weight[i]
    c = sum % 11
    c = 1 if c == 10 else c
    return int(final_cnp[-1]) == c


cnp_list= []

with open("cnp_list_with_names.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Last Name", "CNP"])
    for i in range(1000000):
        cnp = generate_cnp()
        if cnp and validare_cnp(cnp):
            gender = choose_gender()
            first_name = random.choice(male_names) if gender == "bărbat" else random.choice(female_names)
            last_name = random.choice(last_names)
            writer.writerow([first_name, last_name, cnp])
            cnp_list.append(cnp)
            #index = custom_hash(cnp, table_size)
            #if index not in hash_table:
              #  hash_table[index] = []
           # hash_table[index].append((first_name, last_name, cnp))
        if i % 100000 == 0:
            print(f"Generated {i} CNPs with names...")

#print("1 million CNPs with names have been generated and saved to 'cnp_list_with_names.csv'.")

def custom_hash(cnp, table_size):
    hash_value = 0
    prime = 31
    for char in cnp:
        hash_value = (hash_value * prime + int(char)) % table_size
    return hash_value

table_size = 2003
hash_table = {}

csv_file = "cnp_list_with_names.csv"
num_rows = 0

test_cnps = []

try:
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            num_rows += 1
            name, last_name, cnp = row

            index = custom_hash(cnp, table_size)
            if index not in hash_table:
                hash_table[index] = []
            hash_table[index].append((name, last_name, cnp))
            if random.random() < 0.001:
                test_cnps.append(cnp)
#except FileNotFoundError:
    #print("Fișierul CSV nu a fost găsit")

    #print(f"Numărul total de linii din fișier: {num_rows}")
    #if num_rows == 1_000_000:
        #print(" Fișierul CSV conține exact 1.000.000 de înregistrări.")
    #else:
       # print(" Numărul de linii din fișier nu este corect!")
    #print(f" Tabelul hash a fost populat cu {len(hash_table)} intrări distincte.")
except FileNotFoundError:
    print(" Fișierul nu a fost găsit!")

#print("Tabelul hash a fost populat.")



def search_cnp_hash(cnp):
    index = custom_hash(cnp, table_size)
    iterations = 0
    if index in hash_table:
        for entry in hash_table[index]:
            iterations += 1
            if entry[2] == cnp:
                return entry, iterations
    return None, iterations

#def search_cnp_sequential(cnp):
    #iterations = 0
    #for key in hash_table:
        #for entry in hash_table[key]:
            #iterations += 1
            #if entry[2] == cnp:
                #return entry, iterations
    #return None, iterations

sample_size = min(1000, len(cnp_list))
sample_cnps = random.sample(cnp_list, sample_size)
search_results = []

for cnp in sample_cnps:
    result_hash, iterations_hash = search_cnp_hash(cnp)
    #result_seq, iterations_seq = search_cnp_sequential(cnp)
    search_results.append([first_name, last_name, cnp, iterations_hash])
    print(f"CNP: {cnp} |  Hash: {iterations_hash} iterații")

with open("search_results.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([ "CNP", "Iterații Hash"])
    writer.writerows(search_results)



#print("Căutările pentru 1000 de CNP-uri au fost finalizate și salvate în 'search_results.csv'.")

#test_cnp = random.choice
#result, iterations = search_cnp_sequential(test_cnp)
#if result:
 #   print(f"CNP găsit prin căutare secvențială: {result}, Iterații: {iterations}")
#else:
 #   print("CNP-ul nu a fost găsit.")


#def show_csv():
    #root = tk.Tk()
    #root.title("Vizualizare CNP-uri")

    #frame = ttk.Frame(root)
    #frame.pack(fill="both", expand=True)

    #tree = ttk.Treeview(frame, columns=("Name", "Last Name", "CNP"), show="headings")
    #tree.heading("Name", text="Name")
    #tree.heading("Last Name", text="Last Name")
    #tree.heading("CNP", text="CNP")

    #tree.column("Name", width=150)
    #tree.column("Last Name", width=150)
    #tree.column("CNP", width=150)

    #scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    #tree.configure(yscrollcommand=scrollbar.set)

    #scrollbar.pack(side="right", fill="y")
    #tree.pack(fill="both", expand=True)

   # try:
        #with open("cnp_list_with_names.csv", mode="r", encoding="utf-8") as file:
            #reader = csv.reader(file)
            #next(reader)
            #data = list(reader)
            #if not data:
                #print("Fișierul este gol!")
                #return
            #for i, row in enumerate(reader):
                #if i >= 1000:
                    #break
                #tree.insert("", "end", values=row)
    #except FileNotFoundError:
        #print("Eroare: Fișierul 'cnp_list_with_names.csv' nu există!")

    #root.mainloop()

#updated_rows = []
#with open("cnp_list_with_names.csv", mode="r", encoding="utf-8") as file:
    #reader = csv.reader(file)
    #header = next(reader)
    #header.extend(["Iterații Hash"])
    #updated_rows.append(header)

    #for row in reader:
        #cnp = row[2]
        #result_hash, iterations_hash = search_cnp_hash(cnp)
        #row.extend([iterations_hash])
        #updated_rows.append(row)

#with open("cnp_list_with_names.csv", mode="w", newline="", encoding="utf-8") as file:
    #writer = csv.writer(file)
    #writer.writerows(updated_rows)

#show_csv()


cnp_data = []
try:
    with open("cnp_list_with_names.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cnp_data.append(row)
except FileNotFoundError:
    print("Fișierul nu a fost găsit!")

county_count = defaultdict(int)
gender_count = {"bărbat": 0, "femeie": 0}
age_count = {"0-14": 0, "15-29": 0, "30-44": 0, "45-59": 0, "60+": 0}



for index, entries in hash_table.items():
    for entry in entries:
        name, last_name, cnp = entry
        county_code = int(cnp[7:9])
        county_name = [key for key, value in counties.items() if value == county_code][0]
        county_count[county_name] += 1

        gender_code = int(cnp[0])
        if gender_code in [1, 5]:
            gender_count["bărbat"] += 1
        elif gender_code in [2, 6]:
            gender_count["femeie"] += 1

        birth_year = int(cnp[1:3])
        if gender_code in [1, 2]:  # 1900-1999
            birth_year += 1900
        elif gender_code in [5, 6]:  # 2000+
            birth_year += 2000
        else:  # 1800+
            birth_year += 1800

        age = 2024 - birth_year
        if age <= 14:
            age_count["0-14"] += 1
        elif age <= 29:
            age_count["15-29"] += 1
        elif age <= 44:
            age_count["30-44"] += 1
        elif age <= 59:
            age_count["45-59"] += 1
        else:
            age_count["60+"] += 1



root = tk.Tk()
root.title("Statistici CNP")

canvas = tk.Canvas(root, width=1000, height=600, bg="white")
canvas.pack()


def draw_histogram(data, x, y, width, height, title):
    max_value = max(data.values()) if data else 1
    bar_width = width / len(data)

    canvas.create_text(x + width / 2, y - 20, text=title, font=("Arial", 12, "bold"))

    for i, (key, value) in enumerate(data.items()):
        bar_height = (value / max_value) * height
        canvas.create_rectangle(
            x + i * bar_width, y + height - bar_height,
            x + (i + 1) * bar_width, y + height,
            fill="blue"
        )
        canvas.create_text(x + i * bar_width + bar_width / 2, y + height + 10, text=key, font=("Arial", 8), angle=90)

county_count = defaultdict(int)

for row in cnp_data:
    name, last_name, cnp = row
    county_code = int(cnp[7:9])
    county_name = [key for key, value in counties.items() if value == county_code][0]

    county_count[county_name] += 1


def draw_pie_chart(data, x, y, size, title, colors, legend_x, legend_y):
    total = sum(data.values()) if data else 1
    start_angle = 0

    canvas.create_text(x, y - size // 2 - 20, text=title, font=("Arial", 12, "bold"))

    for i, ((key, value), color) in enumerate(zip(data.items(), colors)):
        extent = (value / total) * 360
        canvas.create_arc(x - size // 2, y - size // 2, x + size // 2, y + size // 2, start=start_angle, extent=extent,
                          fill=color)
        start_angle += extent

        legend_offset = 20
        canvas.create_rectangle(legend_x + legend_offset, legend_y + i * 20, legend_x + legend_offset + 12,
                                legend_y + i * 20 + 12, fill=color)
        canvas.create_text(legend_x + legend_offset + 20, legend_y + i * 20 + 6, text=f"{key}: {value}", anchor="w",
                           font=("Arial", 10))


draw_histogram(county_count, 50, 350, 850, 200, "Distribuție pe județe")

draw_pie_chart(gender_count, 200, 120, 150, "Distribuție pe sexe", ["blue", "pink"], 400, 50)

draw_pie_chart(age_count, 600, 120, 150, "Distribuție pe vârstă", ["yellow", "green", "red", "orange", "purple"], 850,
               50)

root.mainloop()