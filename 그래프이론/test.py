class Coin:
    """Do not fix this function"""
    def toss():
        import random
        return random.randint(0, 1)

class Dice:    
    @staticmethod
    def toss():
        # Don't use python random library,
        # Only use Coin.toss()
        
        r = dict()
        
        while len(r)==0:
            
            for i in range(1,7):
                t = Coin.toss()
                if t:
                    r[i] = t
        r_temp = r
        print(r_temp)
        while len(r) != 1 :
            k = list(r.keys())

            for i in k:
                if not Coin.toss():
                    r.pop(i)
            
            if len(r) == 0:
                r = r_temp


        return list(r.keys())[0]

d = Dice()
print(d.toss())


def toss():
        # Don't use python random library,
        # Only use Coin.toss()
        
        r = dict()
        
        while len(r)==0:
            
            for i in range(1,7):
                t = Coin.toss()
                if t:
                    r[i] = t

            while len(r) !=0 and len(r) != 1 :
                k = list(r.keys())
                
                for i in k:
                    if not Coin.toss():
                        r.pop(i)