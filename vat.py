netto = float(input("Podaj kwotę netto: "))
vat = float(input("Podaj wysokość VAT: "))

def calculate_vat(netto,vat):
 brutto = (netto*vat/100) + netto
 return brutto
print("Kwota brutto wynosi: ", calculate_vat(netto,vat), " zł")





