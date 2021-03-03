'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
name = input('Vloz jmeno uzivatele:')
password = input('Vloz heslo uzivatele:')
registred_users ={'bob':'123','ann':'pass123','mike':'password123','liz':'pass123'}
uzivatele = registred_users.keys()
if name in uzivatele:
    if registred_users[name] == password:
        print("Zadane jmeno a heslo je platne!")
    else:
        print('Zadal jsi neplatne heslo!!!')
        exit()
else:
    print('Zadal jsi neznameho uzivatele!!!')
    exit()
print('-'*40)
print('Zdravim te', name,'Pokracujeme dale v analyze')
print('-'*40)
i = 5
while i:
    text = input('Zadej cislo textu, ktery by jsi chtel vybrat[1,2,3]:')
    if text.isdigit() == True:
        text= int(text) - 1
    if text == 0 or text == 1 or text == 2:
        TEXT = TEXTS[text]
        print('-' * 40)
        print ('Vybral jsi text', text+1,'.')
        print('-' * 40)
        break
    else:
        i -= 1
        print ('Uklikl jsi se, proved novou volbu a uz nas jen', i,'pokusy')
else:
    exit()
TEXT = TEXT.replace('-',' ')
TEXT = TEXT.replace('_',' ')
TEXT_list2 = TEXT.split(' ')
TEXT_list = []
for i in TEXT_list2:
    TEXT_list.append(i.strip(',.!?\n\t\f'))
pocet_slov = len(TEXT_list)
velka_pismena = 0
mala_pismena = 0
soucet_cisel = 0
cisla = 0
titulky = 0
delka = 0
delky_slov = dict()
for slova in TEXT_list:
    if slova.isupper():
        velka_pismena += 1
    elif slova.istitle():
        titulky += 1
    elif slova.isdigit():
        cisla += 1
        slovaint = int(slova)
        soucet_cisel = soucet_cisel + slovaint
    else:
        mala_pismena += 1
    delka = len(slova)
    delky_slov[delka] = delky_slov.setdefault(delka,0) + 1
print(f'''There are {pocet_slov} words in the selected text.
There are {titulky} titlecase words.
There are {velka_pismena} uppercase words.
There are {mala_pismena} lowercase words.
There are {cisla} numeric strings.
The sum of all the numbers {soucet_cisel}''')
print('-'*40)
print('Poradi || pocet pismen ||  pocet vyskytu')
print('-'*40)
delky =list(delky_slov.keys())
i = 0
mezera_1 = 0
mezera_2 = 0
for leng in delky:
    if i >= 10:
        mezera_2 = 5
    else:
        mezera_2 = 6
    if leng >= 10:
        mezera_1 = 3
    else:
        mezera_1 = 4
    print(i," " * mezera_1,"||    ",leng," " * mezera_2 ,'||  ',delky_slov[leng] * '*')
    i +=1
