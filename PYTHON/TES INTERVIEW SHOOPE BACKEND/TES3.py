# Input    : Kumpulan Parenthesis
# Output   : Hitung jumlah parenthesis (tanda kurung) yang tidak valid
# Contoh Input | Contoh Output | ket
# (()) | 0 ket : valid
# ((()) | 1 ket : kurung buka pertama tidak ditutup
# ))() | 2 ket : kurung tutup pertama dan kedua tidak memiliki kurung buka
# (())() | 0 ket : valid
data = input()
noOpen = 0
needClose = 0
for i in data:
  if i == ")" and needClose == 0:
    noOpen += 1
  elif i == ")" and needClose > 0:
    needClose -= 1
  elif i == "(":
    needClose += 1
print(noOpen + needClose)