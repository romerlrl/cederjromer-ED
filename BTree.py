class page:
    def __init__(self, ehRaiz=False, profundidade=0, m=2, head=True):
        self.profundidade=profundidade
        if profundidade:   
            self.head=[]
            for x in range(2*m+1):
                if x%2:
                    self.head.append(x)
                else:
                    self.head.append(page(profundidade=profundidade-1, m=m))
        else:
            self.head=[x for x in range(m*2+1)]

    def __str__(self):
        #string='\n.'+ '   '* (4-self.profundidade)
        string=' ['
        for x in self.head:
            string+='\n'+'   '* (4-self.profundidade)
            if isinstance(x, int):
                string+=str(x)+','
                #print(x, end=' ')
            elif isinstance(x, page):
                string+=x.__str__()
            #string+=','
        string+='\n'+'   '* (4-self.profundidade)+'],'
        return string

    def __repr__(self):
        return self.__str__()
x=page(True, 3, 2)
        
        
print(x)
