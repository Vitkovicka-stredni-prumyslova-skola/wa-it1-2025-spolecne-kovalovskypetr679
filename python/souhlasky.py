souhlasky = ["h", "ch", "k", "r", "d", "t", "n", "ž", "š", "č", "ř", "c", "j", "ď", "ť", "ň", "b", "f", "l", "m", "p", "s", "v", "z"]
x = input()
f = 0
for pismenko in x:
    if pismenko in souhlasky:
        f = f+1
print(f)