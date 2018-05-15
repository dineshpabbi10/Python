class Flower:
    _name = str()
    _number = int()
    _price = int()

    def __init__(self):
        self._name = 'default'
        self._number = 1
        self._price = 1

    def __init__(self,_name,_number,_price):
        self._name = _name
        self._number = _number
        self._price = _price

    def get(self):
        return self._name,self._number,self._price


xyz = Flower('Dinesh',10,20)
x= xyz.get()
print("Flower Name: "+x[0]+"\nQuantity: "+str(x[1])+"\nPrice: "+str(x[2]))
