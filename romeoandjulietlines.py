import nltk, unidecode
import matplotlib.pyplot as plt
def read_sents_from_file(filename):
    with open(filename, encoding = "utf-8") as file:
        text_utf8 = file.read()
        text = unidecode.unidecode(text_utf8)
    sents = nltk.sent_tokenize(text)
    return sents
def findStringIn(list1, name):
    #find index of potname
    for i in range(len(list1)):
        if list1[i][0] == name:
            return i
        elif name in list1[i][0]:
            return i
        elif list1[i][0] in name:
            return i
    return None
def checkDupes(names, n):
    for s in names:
        if n in s[0]:
            return True
        elif s[0] in n:
            s[0] = n
            return True
    return False
def copy(grid):
    new = []
    for row in range(len(grid)):
        new.append(grid[row])
    return new
def remove_titles(sents):
    sents[0] = sents[0][sents[0].find("\n"):]
    new = []
    for x in sents:
        if not (x.find("ACT")>=0 or x.find("Scene")>=0 or x.find("SCENE")>=0 or x.find("PROLOGUE")>=0):
            new.append(x)
    return new
def sent_to_word(sents):
    new = []
    for x in sents:
        for i in nltk.word_tokenize(x):
            new.append(i)
    return new
def getNames(words):
    names = []
    tagged = nltk.pos_tag(words)
    for x in range(len(tagged)):
        if (tagged[x][1] == "NNP" or tagged[x][1] == "NNPS") and tagged[x][0].isupper() and len(tagged[x][0])>2:
            potname = tagged[x][0]
            y=1
            while(tagged[x+y][1] == "NNP" or tagged[x+y][1] == "NNPS") and tagged[x][0].isupper() and len(tagged[x][0])>2:
                potname += (" " + tagged[x+y][0])
                y+=1
            if not checkDupes(names, potname):
                names.append([potname, 1])
            else:
                
                names[findStringIn(names, potname)][1] += 1
    return names
def bubbleSort(names):
    n = len(names)
    arr = copy(names)
    for i in range(n):
        for j in range(0, n - i - 1):
             
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def split(list1):
    one = []
    two = []
    for x in list1:
        one.append(x[0])
        two.append(x[1])
    return one, two
def main():

    sents = read_sents_from_file("romeoandjuliet.txt")
    names = getNames(sent_to_word(remove_titles(sents)))
    sortednames = bubbleSort(names)
    print(sortednames)
    x, y = split(sortednames)
    plt.bar(x, y)
    plt.subplots_adjust(bottom=0.3)
    plt.xticks(rotation=90)
    plt.title("Number of Lines for each Character in Romeo and Juliet")
    plt.show()
if __name__ == "__main__":
    main()
