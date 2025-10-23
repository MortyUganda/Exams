class Phone:
    pen = 10
    def __init__(self, color:str, model:str, battery: int) -> None:
        self.color = color
        self.model = model
        self.battery = battery
    
    def __repr__(self) -> str:
        return f'{Phone}'
    
    def __str__(self) -> str:
        return f'Это телефон модели {self.model} цветом {self.color}'

Iphone = Phone('Grey', 'Iphone 12 mini', 80)

print(Phone.pen)
print(Iphone.__repr__())
print(Iphone.__str__())

class My_Phone(Phone):
    def __init__(self, color: str, model: str, battery: int,  _equal) -> None:
        super().__init__(color, model, battery)
        self._equal = self.battery + 20

    def __repr__(self) -> str:
        return (f'My_Phone({self._equal!r})')
    
    def __str__(self) -> str:
        return super().__str__() + f'\nПроцент заряда: {self._equal}'
    
temp = My_Phone('blue', 'Iphone 8', 80, 10)
print(temp.__repr__())















