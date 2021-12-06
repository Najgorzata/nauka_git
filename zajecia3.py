samochody = ["syrena", "polonez"]
print(samochody[0])
for s in samochody:
        print(s)

for idx in range(len(samochody)):
        print("idx: "+ str(idx) + " : " + samochody[idx])

print(",".join(samochody))
lista = "a,b,c,d,e" .split(",")
print(list(samochody[0]))
del samochody[0]
print(samochody)

samochody[0] = "kia"
print(samochody)
samochody.append("fiat")
print(samochody)


samochody = ["syrena", "polonez"]
ilosc = [3,5]
for idx in range(len(samochody)):
        print("idx: {0} {1}".format(idx, samochody[idx]))
        print(samochody[idx] + " ma ilość drzwi "+ str(ilosc[idx]))



zwierze = ["człowiek", "kitku"]
nogi = [2,4]

for idx in range(len(zwierze)):
        print("idx: {0} {1}".format(idx, zwierze[idx]))
        print(zwierze[idx]+ " ma " + str(nogi[idx]) + " nogi"))

        