from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik


rycerze = []
lucznicy = []

for _ in range(4):
    rycerze.append(Rycerz())
print(rycerze)

for rycerz in rycerze:
    rycerz.maszeruj(2000)

rycerze.append(Rycerz())
rycerz.atakuj()
print(rycerze)

for _ in range(3):
    lucznicy.append(Lucznik())
print(lucznicy)

armia = rycerze + lucznicy
print(armia)
for wojownik in armia:
    wojownik.atakuj()
print(armia)

# if __name__ == '__main__':
#     rycerz = Rycerz()
#     print(rycerz)
#     idz = rycerz.maszeruj(10)
#     wal = rycerz.atakuj()
#     print(rycerz)
#     lucznik = Lucznik()
#     print(lucznik)
#     idz1 = lucznik.maszeruj(10)
#     wal1 = lucznik.atakuj()
#     print(lucznik)
