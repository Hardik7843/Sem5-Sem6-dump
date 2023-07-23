def stuff(sig):
    onecounter = 0  
    index = 0  
    one = []  
    signal = list(sig)
    for i in signal:
        index += 1
        if i == '0':
            onecounter = 0
        else:
            onecounter += 1
        if onecounter == 5:
            one.append(index)
            onecounter = 0
    k = 0  
    for i in one:
        signal.insert(i + k, '0')
        k += 1
    return signal



def destuff(sig):
    onecounter = 0  
    index = 0   
    one = [] 
    sig = list(sig)
    for i in sig:
        index += 1
        if i == '0':
            onecounter = 0
        else:
            onecounter += 1
        if onecounter == 5:
            one.append(index)
            onecounter = 0
    k = 0  
    for i in one:
        sig.pop(i + k)
        k -= 1
    return sig

signal = input("Enter the signal: ")
print("Original Signal : ", signal)

stuffed = stuff(signal)
print("Stuffed Signal: ", end="")
print("".join([a for a in stuffed]))

destuffed = destuff(stuffed)
print("Destuffed Signal: ", end="")
print("".join([a for a in destuffed]))
