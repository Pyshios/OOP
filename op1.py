


class asimple:
    amem = list()
    def __init__(self , size ) :
        self.size = size
        self.amem = list()

    def calc(self, word):
        self.amem.append(word)
        ll = len(self.amem)
        if ll > self.size:
            cut = ll - self.size
            self.amem.pop(cut)


    def put(self):
        print(self.amem)

a = asimple(4)

a.calc('amor')
a.calc("anjo")
a.calc("ontem")
a.calc("vida")
a.calc("seu")


print(a.put())