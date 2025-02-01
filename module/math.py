class Matematica:

    def __init__(self, a: int, b: int): ## Dunder method  '__something__'
        self.a = a
        self.b = b

    def somar(self) -> int:
        return self.a + self.b
    
    def subtrair(self) -> int:
        return self.a - self.b
    
    def multiplicar(self) -> int:
        return self.a * self.b