#  Ronalds Poļakovs 10A
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#


import json

products = []
discount = 0
checker = False
# read movies file into variable
with open('lists.json', 'r') as openfile:
    # Reading from json file
    products = json.load(openfile)

def check_money():
    global checker
    if money<price_with_discount:    #Ja mainīgais money irlielāks par mainīgo price_with_discount tad izpildās nākamās funkcijas
        checker=False
        print("Kļūda, jums nepietiek līdzekļu")
    else:
        checker=True

def check_discount():
    global checker
    if discount > 100:             #Ja mainīgais discount ir lielaks par 100 tad Validācija nav izieta
        checker = False
        print("ievadītā atlaideir pārāk liela (0-100)")
    else:
        checker=True
def check():
    global checker 
    if len(title) < 2:           #Ja mainīgā title garums ir mazāks par 2 tad validācija nva izieta
        print("Kļūda, ievadītajā nosaukumā jābūt vismaz 2 burtiem")
        checker=False               
    elif len(title) > 120:                # ja mainīgā title garums ir lielāks par 120 tad validācija nav izieta
        print("Kļūda , ievadītais nosaukums nevar pārsniegt 120 burtu daudzumu")
        checker=False
    elif price > 9999:                       # Ja cena pārsniedz 9999 tad validācija nav izieta
        print("Kļūda,cena nevar pārsniegt 9999$")
        checker=False
    else:
        checker=True
while True:         # Kamēr ir paties visas darbības apakšā strādā
    
    function=input('''
1. Pievienot preci ar cenu
2. Apskatīt preču sarakstu
3. Noņemt preci no saraksta (by index)
4. Dzēst visu sarakstu
5. Pievienot atlaidi
6. Samaksāt
e. Iziet
''')
    if function == "1":     # ja function = 1 tad izpildās sekojošās darbības
        item = {}
        title = input("Preces nosaukumks: ")
        price = float(input("Preces cena: "))
        check()
        if checker == True:          # ja nosaukums un cena iziet validāciju tad pārējas darbības nostrādā
            item["title"] = title
            item["price"] = price
            products.append(item)
    elif function == "2":        # ja function = 2 tad izpildās sekojošās darbības
        for product in products:                # izmanto Katru sarakstu no masīva
            print(products.index(product) , ": " , product["title"] , product["price"])
    elif function == "3":          # ja function = 3 tad izpildās sekojošās darbības
        index=int(input("Indeks: "))
        products.pop(index)
    elif function == "4":            # ja function = 4 tad izpildās sekojošās darbības
        products=[]
    elif function == "5":          # ja function = 5 tad izpildās sekojošās darbības
        discount=int(input("Atlaide % : "))
        check_discount()
        if checker == True:                   # ja nosaukums un cena iziet validāciju tad pārējas darbības nostrādā
            total_discount = discount/100
    elif function == "6":           # ja function = 6 tad izpildās sekojošās darbības
        total_price = 0
        print("Notiek rēķināšana ...")
        for product in products:                  # izmanto Katru sarakstu no masīva
            total_price = total_price + product["price"]
            print(product["title"] , product["price"])
        print("Kopā (bez atlaides): " , round(total_price , 2) , "$")
        print("Atlaide: " , discount , "%")
        price_with_discount = total_price - total_price*total_discount
        print("Kopā: " , round(price_with_discount , 2) , "$")
        money = float(input("Samaksāt: "))
        check_money()
        if checker == True:                       # ja nosaukums un cena iziet validāciju tad pārējas darbības nostrādā
            change = money - price_with_discount
            print("Atlikums: " , round(change, 2) , "$")
        
    elif function == "e":
        print("exiting...")
        print("saving...")
        with open("lists.json", "w") as lists_file:
            json.dump(products, lists_file)
        break
    else:
        print("Kļūda, izvēlētā funkcija neeksistē vai tika ievadīta nepareizi. Mēģiniet vēlreiz")









