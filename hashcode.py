import numpy as np

# read file and store each line
fp = open('a_example.txt', 'r')
data = fp.readlines()
problemData = data[0].replace('\n', '').split(' ')
totalDays = problemData[2]
books = data[1].replace('\n', '').split(' ')
scannedBooks = [False]* len(books)

def main():
    
    #READING LIBS
    libs = []
    counter = 0
    for x in range(2, len(data), 2):
        libs.append(Library(data[x].replace('\n', ''), data[x+1].replace('\n', ''),counter))
        counter += 1

    #SORTING LIBS
    libs.sort(reverse=True,key=sortLibScore)
    for x in libs:
        print(x.maxScore)

    simulateDays(libs)

def simulateDays(libs):
    id = 0
    day = libs[0].signUpTime
    for x in range(0,int(totalDays)-1):
        if(x == day):
            id += 1
            if(id < len(libs)):
                day += libs[id].signUpTime
        for i in range(0, id):
            libs[i].scanBooks()
            print(libs[i].sentBooks)

    submission(id, libs)

def submission(id, libs):
    sub = open("sub.txt", 'w')
    sub.write(str(id))
    sub.write('\n')
    
    for i in range(0, id):
        sub.write(str(libs[i].id) + ' ' + str(libs[i].countBookSent()) + '\n')
        sub.write(libs[i].orderedBookSent() + '\n')






def sortLibScore(lib):
    return lib.maxScore

def sortBookScore(book):
    return books[int(book)]


class Library:
    def __init__(self, line1, line2, counter):
        tmp1 = line1.split(' ')
        self.bookArray = line2.split(' ')
        self.sentBooks = [False] * len(self.bookArray)
        self.bookArrayIndex = 0

        self.id = counter
        self.nrBooks = int(tmp1[0])
        self.signUpTime = float(tmp1[1])
        self.shipCapacity = int(tmp1[2])
        self.bookScore = 0
        self.allBooks()
        self.maxScore = self.bookScore * self.shipCapacity / self.signUpTime

        #print(self.bookArray)
        #print(self.nrBooks)
        #print(self.signUpTime)
        #print(self.shipCapacity)

    def allBooks(self):
        for x in self.bookArray :
            self.bookScore+= int(books[int(x)])
        self.bookArray.sort(reverse=True, key=sortBookScore)
        print(self.bookArray)

    def nextBook(self):
        if (self.bookArrayIndex >= len(self.bookArray)):
            return

        if (not scannedBooks[int(self.bookArray[int(self.bookArrayIndex)])] ):
            index = int(self.bookArrayIndex)
            print(index)
            self.sentBooks[index] = True
            scannedBooks[int(self.bookArray[int(self.bookArrayIndex)])] = True
            self.bookArrayIndex += 1
        else :
            self.bookArrayIndex += 1
            self.nextBook()

    def scanBooks(self):
        for i in range(0, int(self.shipCapacity)):
            self.nextBook()

    def countBookSent(self):
        sum = 0
        for i in self.sentBooks:
            if (i): 
                sum += 1
        return sum
        
    def orderedBookSent(self):
        sent = ''
        for i in range(0, len(self.bookArray)):
            if (self.sentBooks[int(i)]):
                sent += str(self.bookArray[i]) + ' '
        return sent


  
if __name__== "__main__":
  main()

