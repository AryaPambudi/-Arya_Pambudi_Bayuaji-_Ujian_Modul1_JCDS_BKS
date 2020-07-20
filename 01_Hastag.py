
def Hastag(string) :
    if string == '' :
        return False
    elif len(string.replace(' ','')) > 139 : # 139 karena sudah ada hastag(#) jadi 140 = '#' + 139
        return False
    else :
        kata = '#'
        string = list(string.split())
        for a in range(0,len(string)) :
            string[a] = string[a].capitalize()
            kata += string[a]
        return kata

print(Hastag(' Hello there how are you doing'))
print(Hastag("  Hello  World  "))
print(Hastag(""))
