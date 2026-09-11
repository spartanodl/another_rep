class animal:
    def __init__(self, especie, idade):
        # Atributos encapsulados (privados)
        self.__especie = especie
        self.__idade = idade

    # Getters para leitura dos atributos privados
    def get_especie(self):
        return self.__especie

    def get_idade(self):
        return self.__idade

    def __len__(self):
        """Retorna o tamanho do nome da espécie."""
        return len(self.__especie)

    # Setter para alteração segura da idade com validação
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Erro: A idade deve ser um valor positivo!")

    def apresentar(self):
        # Acesso interno aos atributos privados
        print(f'Espécie: {self.__especie}')
        print(f'Idade: {self.__idade}')

    def falar(self):
        print("som generico")


# --- CLASSES FILHAS ENCAPSULADAS ---

class cachorro(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca  # Atributo privado da classe filha

    def get_raca(self):
        return self.__raca

    def set_raca(self, nova_raca):
        if len(nova_raca.strip()) > 0:
            self.__raca = nova_raca

    def apresentar(self):
        super().apresentar()  # Aproveita o apresentar() da classe mãe
        print(f'Raça: {self.__raca}')

    def falar(self):
        print("au au au")


class gato(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print("miau miau miau")


class galinha(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print("coco coco coco")


class pinguim(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print('gnaw gnaw gnaw')


class rato(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print('squik squik squik')


class golfinho(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print('eek eek eek')


class cobra(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print('tssssssssss')


class urso(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print('hur hur hur')


class passaros(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print('tweet tweet tweet')


class abelhas(animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def apresentar(self):
        super().apresentar()
        print(f'Raça: {self.__raca}')

    def falar(self):
        print("bzzz bzzz bzzz")


# --- EXECUÇÃO ---

meus_animais = [
    cachorro('cachorro', 2, 'poodle'), 
    gato('gato', 3, "vira-lata"), 
    galinha('galinha', 1, "d'angola"),
    pinguim('pinguim', 1, "pinguim-imperador"),
    rato('rato', 3, 'gerbil'),
    golfinho('golfinho', 12, 'golfinho bico de garrafa'),
    cobra('cobra', 4, 'cobra-coral'),
    urso('urso', 5, 'urso-pardo'),
    passaros('passaro', 6, 'bem-te-vi'),
    abelhas('abelha', 8, 'abelha-domestica comum')
]

# Modificando atributo através do Setter com validação:
meus_animais[0].set_idade(5)  # Funciona perfeitamente
meus_animais[0].set_idade(-2) # Exibe a mensagem de erro

print('_' * 15)

for a in meus_animais:
    a.apresentar()
    a.falar()
    print('_' * 15)