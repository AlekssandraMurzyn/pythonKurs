# zadanie 2.1
print("##################### zadanie 2.1 ##################### ")
longInt = 92835893724000
a = str(longInt)
b = a.count("0")
print(b)

# zadanie 2.2
print("##################### zadanie 2.2 ##################### ")

x = 5
print(x == 5 and 3)  # 3 is not 0 and x is indeed 5 so its True. print(x == 5 and 0) would be false
print(x == 4 and 3)  # False because x is 5, not 4
print(3 and x == 5)  # 3 is not 0 and x is indeed 5 so its True. print(x == 5 and 0) would be false
print(3 and x == 4)  # False because x is 5, not 4. And have to be True on both sides of logical opperand

isinstance(True, int)  # False, because int != bool
isinstance(True, bool)  # True is a bool so isinstance(True, bool) will also be True

# zadanie 2.3
print("##################### zadanie 2.3 ##################### ")

listaNowychWartosci = []
for numer in range(1, 2023, 2):
    listaNowychWartosci.append(numer ** 2)
print(sum(listaNowychWartosci))

# inna metoda
print(sum([x ** 2 for x in range(1, 2023, 2)]))

# zadanie 2.4
print("##################### zadanie 2.4 ##################### ")

listapierwiastkow = [(1, "hydrogen", "H", 1), (2, "helium", "He", 4), (3, "Lithium", "Li", 7)]

print(listapierwiastkow)
print("+----+--------------------+-------+-------+")
print("|No. |   Name (en)        |Symbol |Waga(u)|")
print("+----+--------------------+-------+-------+")
for pierwiastek in listapierwiastkow:
    print("|{}|{}|{}|{}|".format(str(pierwiastek[0]) + " " * (4 - len(str(pierwiastek[0]))),
                                 pierwiastek[1] + " " * (20 - len(pierwiastek[1])),
                                 pierwiastek[2] + " " * (7 - len(pierwiastek[2])),
                                 str(pierwiastek[3]) + " " * (7 - len(str(pierwiastek[3])))))
    print("+----+--------------------+-------+-------+")

# zadanie 2.5
print("##################### zadanie 2.5 ##################### ")
# Let S be a long string (many lines).
wierszyk = '''Stoi na stacji lokomotywa,
Ciężka, ogromna i pot z niej spływa:
Tłusta oliwa.
Stoi i sapie, dyszy i dmucha,
Żar z rozgrzanego jej brzucha bucha:
Uch - jak gorąco!
Puff - jak gorąco!
Uff - jak gorąco!
Już ledwo sapie, już ledwo zipie,
A jeszcze palacz węgiel w nią sypie.
Wagony do niej podoczepiali
'''

# Find the number of words in S.
print("Liczba słów gorąco w wierszu: ", wierszyk.count("gorąco"))

# Find the number of black characters in S.
print("Liczba nie-białych znaków: ", len(wierszyk.replace(" ", "").replace("\n", "")))

# Find the longest word in S.
tablicaSlow = []
tablicaSlowMalymiLiterami = []
for slowo in wierszyk.split(" "):
    for element in slowo.split("\n"):
        tablicaSlow.append(element)
        tablicaSlowMalymiLiterami.append(element.lower())
najdluzszeSlowo = ""
for slowo in tablicaSlow:
    if len(slowo)>len(najdluzszeSlowo):
        najdluzszeSlowo = slowo
    else:
        continue
print("Najdluzsze slowo w wierszu: ", najdluzszeSlowo)
# Sort words from S according to (1) the lexicographic order, (2) the length.

tablicaSlowMalymiLiterami.sort()
print("alfabetycznie: ", tablicaSlowMalymiLiterami)
print("wg dlugosci: ", sorted(tablicaSlow, key=len))

# Find the number of zeros in a long number [hint: change to a string].
longInt = 92835893724000
a = str(longInt)
b = a.count("0")
print(b)


print("##################### zadanie 2.6 ##################### ")

# Find and explain the results.
t = (2, 4)
#print(t[2]) #arrays, touples etc are 0- based. [2] is out of range
#t.append(6) #appened is a touple not list so can;t be modified that way
#a, b = t ; print(a, b) ; means a new line so its assigment touple to the 2 vars, and then normal print od 2 values

print("##################### zadanie 2.7 ##################### ")

konwersjaDoArabskich = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
}
