A = 70

def printA():
    print ("As esu nauja printA() funkcija")
    print("Dar vienas pakeitimas")





class Vehicle():
    def __init__(self, P, R):
        self.P = P
        self.R = R
class Car(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    def GetSeats(self):
        Txt = self.P + " turi " + str(self.S) + " sedimu vietu"
        return Txt
    

class Bus(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + "turi " + str(self.S) + " sedimu vietu "
        return Txt
    

class Train(Vehicle):
    def __init__(self, P, R, S):
       super().__init__(P, R)
       self.S = S
    
    def GetSeats(self):
        Txt = self.P + "turi " + str(self.S) + " sedimu vietu"
        return Txt






class Txtreader:
    def __init__(self, failo_pavadinimas):
        self.failo_pavadinimas = failo_pavadinimas
        self.I = []
        self.U = []
        self.j = []
        self.P = []
    
    def skaitytojas(self):
        failas = open(self.failo_pavadinimas, mode ='r')
        tekstas = failas.readlines()
        failas.close()

        for eilute in tekstas[1:]:
            u = float(eilute.split(";")[0])
            self.U.append(u)
            i = float(eilute.split(";")[1])
            self.I.append(i)
            J = float(eilute.split(";")[2])
            self.j.append(J)
            p = float(eilute.split(";")[3])
            self.P.append(p)

    def getPmax(self):
        Pmax =max(self.P)
        return Pmax
    
    def getPCE(self):
        Pmax = self.getPmax()
        ats = Pmax / 1000 * 100
        return ats
    

    