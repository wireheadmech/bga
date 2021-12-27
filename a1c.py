# function to calculate A1C
def aonec():


getbgc = input("gluc?")
bgc = float(getbgc)
atrans = (bgc + 46.7)
aonec = (atrans / 28.7)

    return(round(aonec,2))

