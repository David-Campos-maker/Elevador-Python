class Elevador:
    def __init__(self):
        self.__codigo = 'None'
        self.__estado = 0
        self.__posicao = 0
        self.__totalrun = 0
        self.__totalmuv = 0

    def inicializar(self , codigo):
        if self.__estado == 0:
            self.__codigo = codigo

        else:
            print('Operação ilegal!')

    def ligar(self):
        if self.__estado == 0:
            self.__estado = 1

        else:
            print('Operação ilegal!')

    def mover(self , destino):
        if destino >= 0 and self.__estado == 1:
            if destino > self.__posicao:
                print('Subindo...')
                self.__totalrun += (destino - self.__posicao)

            else:
                print('Descendo...')
                self.__totalrun += (self.__posicao - destino)

            self.__posicao = destino
            self.__totalmuv += 1

        else:
            print('Erro ao mover o elevador!')

    def desligar(self):
        if (self.__posicao == 0) and (self.__estado == 1):
            self.__estado = 0
    
        else:
            print('Elevador em funcionamento!')

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def estado(self):
        return self.__estado

    @property
    def posicao(self):
        return self.__posicao

    @property
    def totalrun(self):
        return self.__totalrun

    @property
    def totalmuv(self):
        return self.__totalmuv
