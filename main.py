from Elevador import Elevador

elevador1 = Elevador()
elevador1.inicializar('Torre 1')

print('Código:' , elevador1.codigo)

print('Estado:' , elevador1.estado)

elevador1.ligar()
print('Estado:' , elevador1.estado)
print('Andar->' , elevador1.posicao)

elevador1.mover(7)
print('Andar->' , elevador1.posicao)

elevador1.mover(12)
print('Andar->' , elevador1.posicao)

elevador1.mover(3)
print('Andar->' , elevador1.posicao)

print('Histórico:' , elevador1.totalrun)
print('Movimentos:' , elevador1.totalmuv)
