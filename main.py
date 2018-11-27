import xml.etree.ElementTree as ET

# e = ET.parse('avtomat.xml').getroot()
# beginNode = int(e.find("begin").get("id"))
# endNode = int(e.find("end").get("id"))
# e = e.find("nodes")
# A = []
# numberOfNodes = len(e)

def klini(a):
    b = a.copy()
    b[2]=b[2]-1
    c = b.copy()
    c[1] = c[2]+1
    d = c.copy()
    d[0] = d[1]
    e = b.copy()
    e[0] = e[2] + 1
    if(a[2]!=0):
        A.append("(")
        A.append(klini(b))
        A.append("+")
        A.append(klini(c))
        A.append("(")
        A.append(klini(d))
        A.append(")*")
        A.append(klini(e))
        A.append(")")
        return ""
    else:
        return str(a)

def findWord(a,e):
    p=-1
    id = a[1:2]
    l = len(e)
    destNode = a[4:5]
    for i in range(0,l):
        if e[i].get("id") == str(id):
            p = i
            break
    if(p==-1):
        return None
    for j in range(0,len(e[p])):
        if e[p][j].get("id") == str(destNode):
            return e[p][j].text
    return None


# klini([beginNode,endNode,numberOfNodes])
# A = list(filter(len,A))

# print("".join(A))
def replace():
    p = len(A)
    j = 0
    while j < p:
        i=j
        j = j + 1
        if len(A[i])>2:
            a = findWord(A[i],e)
            if a!=None:
                if A[i+1] == "+":
                    A[i]=a
                else:
                    if A[i+1]=="(" and A[i+3]==")*":
                        b = findWord(A[i+4],e)
                        if b!= None:
                            A[i] = a
                            continue
                        else:
                            del A[i]
                            del A[i]
                            del A[i]
                            del A[i]
                            del A[i]
                            if A[i-1] == "+":
                                del A[i-1]
                                p=p-6
                                j=j-2
                            else:
                                p=p-5
                                j = j - 1
                    else:
                        A[i] = a
            else:
                if A[i+1]=="+":
                    del A[i+1]
                    del A[i]
                    p=p-2
                    j = j - 1
                    continue
                if A[i-1]=="(" and A[i+1]==")*" :
                    del A[i+1]
                    del A[i]
                    del A[i-1]
                    p=p-3
                    j = j - 2
                    continue
                if A[i+1]=="(" and A[i+3]==")*":
                    del A[i]
                    del A[i]
                    del A[i]
                    del A[i]
                    del A[i]
                    if A[i-1] == "+":
                        del A[i-1]
                        p = p-6
                        j = j-2
                    else:
                        p = p-5
                        j = j-1
                    continue
    #delete empty brackets
    p = len(A)
    j = 0
    while j<p :
        if A[j] == "(" and ( A[j+1] == ")" or A[j+1] == ")*" ) :
            if A[j+2] == "+" :
                del A[j]
                del A[j]
                del A[j]
                p = p-3
                j = j-2
            else :
                del A[j]
                del A[j]
                p=p-2
                j = j - 2
        j = j+1





# print(A)
# replace()
# print(A)
# print("".join(A))

if __name__ == "__main__":
    e = ET.parse('avtomat.xml').getroot()
    beginNode = int(e.find("begin").get("id"))
    endNode = int(e.find("end").get("id"))
    e = e.find("nodes")
    A = []
    numberOfNodes = len(e)
    klini([beginNode, endNode, numberOfNodes])
    A = list(filter(len, A))
    replace()
    print("".join(A))

# ((a)(b))+ab(aab)*((aa)(b))
# ab+(ab)(aab)*(aab)
# a(ba)*b+(a(ba)*a)((b+aa)(ba)*a)*(a+(b+aa)(ba)*b)