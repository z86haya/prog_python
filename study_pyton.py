def annou(f):
    def wr():
        print("run")
        f()
        print("dpne")
    return wr
    
    #dekorator
@annou   
def helo():
    print("hrello")
    
peop = [
    {"name":"zlata", "age":6},
    {"name":"masa", "age":12}
]

def f(pers):
        return pers["name"]

peop.sort(key = f)
print(peop)


def squre(x,y):
    return x*y

#hello
print(squre(2,4))
