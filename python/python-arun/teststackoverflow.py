userAnswer="2314"

computerNumber="1234"

value = ""
tmp = [False]*4 
for i in range(4):
    for j in range(4):
        if userAnswer[i] == computerNumber[j]:
            if i==j and tmp[j]!= True:
                tmp[j] = True 
                value += "R"
            elif tmp[j] != True:
                tmp[j] = True
                value += "F"
            break
print  value