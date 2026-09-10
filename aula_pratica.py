class animal:
    def __init__(self, especie, idade):
        self.especie = especie
        self.idade = idade
        
    def apresentar(self):
        print(f'Espécie: {self.especie}')
        print(f'Idade: {self.idade}')
        
    def falar(self):
        print("som generico")
        
class cachorro(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
        
    def falar(self):
        print("au au au")
        
class gato(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print("miau miau miau")
        
class galinha(animal):
    def __init__(self, especie, idade, raca,):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print("coco coco coco")
        
class pinguim(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print('gnaw gnaw gnaw')
        
class rato(animal):
    def __init__(self,especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print('squik squik squik')
        
class golfinho(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print('eek eek eek')
        
class cobra(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print('tssssssssss')
        
class urso(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print('hur hur hur')
        
class passaros(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print('tweet tweet tweet')
        
class abelhas(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca
        
    def falar(self):
        print("bzzz bzzz bzzz")
        
meus_animais = [
    cachorro('cachorro', 2, 'poodle'), 
    gato('gato', 3, "vira-lata"), 
    galinha('galinha', 1, "d'angola"),
    pinguim('pinguim', 1, "pinguim-imperador"),
    rato('rato', 3 ,'gerbil'),
    golfinho('golfinho', 12, 'golfinho bico de garrafa'),
    cobra('cobra', 12, 'cobra-coral'),
    urso('urso', 12, 'urso-pardo'),
    passaros('passaro', 12, 'bem-te-vi'),
    abelhas('abelha', 12, 'abelha-domestica comum')]


for animal in meus_animais:
    animal.apresentar()
    animal.falar()
    print('_' * 15)
    
