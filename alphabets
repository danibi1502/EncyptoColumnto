
# bit manipulation class
class bit_man:

    """function to reverse a list"""
    def reverse_list(self, list):
        l = []
        for i in range(len(list)):
            l.append(list.pop())
        return l

    """function to add leading zeros to a binary number"""
    def add_zeros(self, a, diff):
        for i in range(diff):
            a.append(0)
        return a

    """function used to make sure all manipulated binary numbers are of the same length"""
    def equalise(self, a, diff):
        return self.reverse_list(self.add_zeros(self.reverse_list(a), diff))

    """function to toggle a bit in a binary number"""
    def toggle(self, a):
        t = a^1
        return t

    """function that demonstrates the half adder circuit used to add two bits"""
    def half_adder(self, a: int, b: int):
        sum = a^b
        carry = a&b
        return sum, carry

    """function that demonstrates the full adder cicuit"""
    def full_adder(self, a, b, c=0):
        s1, c1 = self.half_adder(a, b)
        sum, c2 = self.half_adder(s1, c)
        cout = c1|c2
        return sum, cout

    """function that uses the functionality of the full adder circuit to add two binary numbers"""
    def add(self, a: list, b: list):
        c, p = 0, 0
        sum_list = []
        diff = len(a) - len(b)
        if diff < 0:
            a = self.equalise(a, abs(diff))
        if diff > 0:
            b = self.equalise(b, abs(diff))
        l = len(a) - 1
        for i in range(len(a)):
            s, c = self.full_adder(a[l-p], b[l-p], c)
            p += 1
            sum_list.append(s)
        if c == 1: sum_list.append(c)
        return self.reverse_list(sum_list)

    """function that changes a binary number to it's two's compliment format"""
    def twos_compliment(self, a):
        l, p = len(a), 0
        for i in range(l):
            a[i] = self.toggle(a[i])
        a = self.add(a, [1])
        return a

    """function that subtracts two binary numbers with the use of the full adder"""
    def subtract(self, a, b):
        b = self.twos_compliment(b)
        return self.add(a, b)

# Alphabets class
class Alphabets:
    BM = bit_man() # initialisation of the bit manipulation class

    """dictionary that holds characters"""
    char = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": "",
            "10": "",
            "11": "",
            "12": "",
            "13": "",
            "14": "",
            "15": "",
            "16": "",
            "17": "",
            "18": "",
            "19": "",
            "20": "",
            "21": "",
            "22": "",
            "23": "",
            "24": "",
            "25": "",
            "26": "",
            "27": "",
            "28": "",
            "29": "",
            "30": "",
            "31": "",
            "32": "",
            "33": "",
            "34": "",
            "35": "",
            "36": "",
            "37": "",
            "38": "",
            "39": "",
            "40": "",
            "41": "",
            "42": "",
            "43": "",
            "44": "",
            "45": "",
            "46": "",
            "47": "",
            "48": "",
            "49": "",
            "50": "",
            "51": "",
            "52": "",
            "53": "",
            "54": "",
            "55": "",
            "56": "",
            "57": "",
            "58": "",
            "59": "",
            "60": "",
            "61": "",
            "62": "",
            "63": "",
            "64": "",
            "65": "",
            "66": "",
            "67": "",
            "68": ""}

    """to move from a character to the next, the binary value is incremented by one"""
    #    obj     J's binary rep of char  char
    char["1"] = [[0, 0, 0, 0, 0, 0, 1], "a"]
    char["2"] = [BM.add(char["1"][0], [1]), "b"]
    char["3"] = [BM.add(char["2"][0], [1]), "c"]
    char["4"] = [BM.add(char["3"][0], [1]), "d"]
    char["5"] = [BM.add(char["4"][0], [1]), "e"]
    char["6"] = [BM.add(char["5"][0], [1]), "f"]
    char["7"] = [BM.add(char["6"][0], [1]), "g"]
    char["8"] = [BM.add(char["7"][0], [1]), "h"]
    char["9"] = [BM.add(char["8"][0], [1]), "i"]
    char["10"] = [BM.add(char["9"][0], [1]), "j"]
    char["11"] = [BM.add(char["10"][0], [1]), "k"]
    char["12"] = [BM.add(char["11"][0], [1]), "l"]
    char["13"] = [BM.add(char["12"][0], [1]), "m"]
    char["14"] = [BM.add(char["13"][0], [1]), "n"]
    char["15"] = [BM.add(char["14"][0], [1]), "o"]
    char["16"] = [BM.add(char["15"][0], [1]), "p"]
    char["17"] = [BM.add(char["16"][0], [1]), "q"]
    char["18"] = [BM.add(char["17"][0], [1]), "r"]
    char["19"] = [BM.add(char["18"][0], [1]), "s"]
    char["20"] = [BM.add(char["19"][0], [1]), "t"]
    char["21"] = [BM.add(char["20"][0], [1]), "u"]
    char["22"] = [BM.add(char["21"][0], [1]), "v"]
    char["23"] = [BM.add(char["22"][0], [1]), "w"]
    char["24"] = [BM.add(char["23"][0], [1]), "x"]
    char["25"] = [BM.add(char["24"][0], [1]), "y"]
    char["26"] = [BM.add(char["25"][0], [1]), "z"]
    char["27"] = [BM.add(char["26"][0], [1]), "A"]
    char["28"] = [BM.add(char["27"][0], [1]), "B"]
    char["29"] = [BM.add(char["28"][0], [1]), "C"]
    char["30"] = [BM.add(char["29"][0], [1]), "D"]
    char["31"] = [BM.add(char["30"][0], [1]), "E"]
    char["32"] = [BM.add(char["31"][0], [1]), "F"]
    char["33"] = [BM.add(char["32"][0], [1]), "G"]
    char["34"] = [BM.add(char["33"][0], [1]), "H"]
    char["35"] = [BM.add(char["34"][0], [1]), "I"]
    char["36"] = [BM.add(char["35"][0], [1]), "J"]
    char["37"] = [BM.add(char["36"][0], [1]), "K"]
    char["38"] = [BM.add(char["37"][0], [1]), "L"]
    char["39"] = [BM.add(char["38"][0], [1]), "M"]
    char["40"] = [BM.add(char["39"][0], [1]), "N"]
    char["41"] = [BM.add(char["40"][0], [1]), "O"]
    char["42"] = [BM.add(char["41"][0], [1]), "P"]
    char["43"] = [BM.add(char["42"][0], [1]), "Q"]
    char["44"] = [BM.add(char["43"][0], [1]), "R"]
    char["45"] = [BM.add(char["44"][0], [1]), "S"]
    char["46"] = [BM.add(char["45"][0], [1]), "T"]
    char["47"] = [BM.add(char["46"][0], [1]), "U"]
    char["48"] = [BM.add(char["47"][0], [1]), "V"]
    char["49"] = [BM.add(char["48"][0], [1]), "W"]
    char["50"] = [BM.add(char["49"][0], [1]), "X"]
    char["51"] = [BM.add(char["50"][0], [1]), "Y"]
    char["52"] = [BM.add(char["51"][0], [1]), "Z"]
    char["53"] = [BM.add(char["52"][0], [1]), " "]
    char["54"] = [BM.add(char["53"][0], [1]), "."]
    char["55"] = [BM.add(char["54"][0], [1]), ","]
    char["56"] = [BM.add(char["55"][0], [1]), "!"]
    char["57"] = [BM.add(char["56"][0], [1]), "?"]
    char["58"] = [BM.add(char["57"][0], [1]), "'"]
    char["59"] = [BM.add(char["58"][0], [1]), '"']
    char["60"] = [BM.add(char["59"][0], [1]), "-"]
    char["61"] = [BM.add(char["60"][0], [1]), "="]
    char["62"] = [BM.add(char["61"][0], [1]), "+"]
    char["63"] = [BM.add(char["62"][0], [1]), ")"]
    char["64"] = [BM.add(char["63"][0], [1]), "("]
    char["65"] = [BM.add(char["64"][0], [1]), ";"]
    char["66"] = [BM.add(char["65"][0], [1]), ":"]
    char["67"] = [BM.add(char["66"][0], [1]), "@"]
    char["68"] = [BM.add(char["67"][0], [1]), "#"]
