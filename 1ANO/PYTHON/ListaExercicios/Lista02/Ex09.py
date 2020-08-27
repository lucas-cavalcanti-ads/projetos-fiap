teclado = input("Digite a distancia percorrida(m): ")
distancia = float(teclado)
teclado = input("Digite a velocidade no percurso(s): ")
velocidade = float(teclado)

ms = distancia / velocidade
kh = ms / 3.6

print("A velocidade média do percurso foi: ",ms,"m/s",", ",kh,"k/h")

