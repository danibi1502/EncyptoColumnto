from alphabets import *
from random import *

class General:

    def insertion_sort(self, list1):
        n = int(len(list1))
        for i in range(1, n):
            insert = list1[i]
            current = i - 1
            while list1[current] > insert and current > -1:
                list1[current + 1] = list1[current]
                current -= 1
            list1[current + 1] = insert
        return list1

    def list_to_string(self, list):
        string = ""
        for i in range(len(list)):
            string += str(list[i])
        return string

class Crypt:

    def __init__(self):
        self.A = Alphabets()
        self.Gen = General()

    def orderkey(self, keyword):
        self.mem = []
        for char in keyword:
            for item in self.A.char.items():
                if item[1][1] is char:
                    self.mem.append(int(item[0]))
        mem = []
        for i in range(len(self.mem)):
            mem.append(self.mem[i])
        sort = self.Gen.insertion_sort(self.mem)
        for i in range(len(self.mem)):
            mem[i] = sort.index(mem[i])
        return mem

class Encrypt:

    def __init__(self, plain, keyword):
        self.data = list(plain)
        self.lendata = len(self.data)
        self.keyword = keyword
        self.key = len(keyword)
        self.cypher = ""
        self.mem = []
        self.Gen = General()
        self.A = Alphabets()
        self.space = self.A.char["53"][1]
        self.C = Crypt()

    def split(self):
        mem = []
        i = 0
        while i < self.lendata:
            for j in range(self.key):
                if self.data[i] is self.space:
                    mem.append(self.A.char[str(randrange(27, 52))][1])
                else:
                    mem.append(self.data[i])
                i += 1
                if i > self.lendata - 1:
                    for k in range(self.key - len(mem)):
                        mem.append(self.A.char[str(randrange(27, 52))][1])
                    break
            self.mem.append(mem)
            mem = []

    def encrypt(self):
        self.split()
        data = self.mem
        pos = self.C.orderkey(self.keyword)
        for i in pos:
            for j in range(len(data)):
                self.cypher += data[j][i]
            # self.cypher += " "
        return self.cypher

class Decrypt:

    def __init__(self, cypher, keyword):
        self.cypher = cypher
        self.lencypher = len(self.cypher)
        self.keyword = keyword
        self.key = len(keyword)
        self.plain = ""
        self.mem = []
        self.Gen = General()
        self.A = Alphabets()
        self.C = Crypt()

    def decrypt(self):
        plain = []
        pos = self.C.orderkey(self.keyword)
        index = 0
        div = int(self.lencypher/self.key)
        while index < div:
            c = []
            for p in pos:
                c.append(self.cypher[(p*div)+index])
            plain.append(c)
            index += 1
        for i in range(len(plain)):
            for j in plain[i]:
                self.plain += j
        return self.plain

print("Encryption using Columnar Transposition\n")
print("Note: The plain text from decryption wouldn't be the same as the text that's to be encrypted. Some null values are added to it!\n")

data = str(input("Data to be encrypted: "))
keyword = str(input("Keyword used to encrypt: "))

print("\n")

E = Encrypt(data, keyword)
cypher = E.encrypt()
print("Cypher text: \n", cypher, "\n")

D = Decrypt(cypher, keyword)
plain = D.decrypt()
print("Plain text: \n", plain, "\n")
