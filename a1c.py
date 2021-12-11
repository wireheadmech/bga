# function to calculate A1C

getbgc = input("gluc?")
bgc = float(getbgc)
atrans = (bgc + 46.7)
aonec = (atrans / 28.7)

print(round(aonec,2))
