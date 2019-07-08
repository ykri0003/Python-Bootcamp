inputs = list()
print("Enter 10 integers")
for i in range(0,10):
    inputs.append(int(input()))
list2 = []
for i in range(len(inputs)-1):
    for j in range(1,len(inputs)):
        if (inputs[i]*inputs[j]%2 == 0) & ((inputs[i]+inputs[j])%2 != 0):
            if (inputs[j],inputs[i]) not in list2:
                list2.append((inputs[i],inputs[j]))
print("Formatted list of pairs \n",list2)