import sys
from math import exp

entrada = []


def get_bias(archivo):
    lista = []
    bias = open(archivo, "r")
    for a in bias.readlines():
        lista.append(float(a))
    return lista


def get_weights(archivo):
    lista = []
    weights = open(archivo, "r")
    for a in weights.readlines():
        aux = a.split("	")
        laux = [float(aux[0]), float(aux[1]), float(aux[2])]
        lista.append(laux)
    return lista


def get_sigmoidal(sigma=None, bias=None):
    sigmoidal = []
    for index in range(len(bias)):
        sigmoidal.append(1 / (1 + exp(-1 * (bias[index] + sigma[index]))))
    return sigmoidal


def get_sigma(sigmoidal, pesos):
    sigma = []
    for peso in range(len(pesos[0])):
        value = 0
        for index_sigmoidal in range(len(sigmoidal)):
            value += sigmoidal[index_sigmoidal] * pesos[index_sigmoidal][peso]
        sigma.append(value)
    return sigma


bias_entrada = get_bias("BiasEntrada.txt")
bias_oculta = get_bias("BiasOculta.txt")
bias_salida = get_bias("BiasSalida.txt")

peso_entrada_oculta = get_weights("PesosEntradaOculta.txt")
peso_salida_oculta = get_weights("PesosSalidaOculta.txt")

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 1:
        for index_args in range(len(args)):
            if index_args is 0:
                pass
            else:
                entrada.append(int(sys.argv[index_args]))
    else:
        entrada = [0, 0, 0, 1, 1, 1]

    sigmoidal_entrada = get_sigmoidal(sigma=entrada, bias=bias_entrada)
    sigma_oculta = get_sigma(sigmoidal_entrada, peso_entrada_oculta)
    sigmoidal_oculta = get_sigmoidal(sigma=sigma_oculta, bias=bias_oculta)
    sigma_salida = get_sigma(sigmoidal_oculta, peso_salida_oculta)
    sigmoidal_salida = get_sigmoidal(sigma=sigma_salida, bias=bias_salida)
    # print("sigmoidal_entrada", sigmoidal_entrada)
    # print("sigma_oculta", sigma_oculta)
    # print("sigmoidal_oculta", sigmoidal_oculta)
    # print("sigma_salida", sigma_salida)
    # print("peso_entrada_oculta", peso_entrada_oculta)
    # print("sigmoidal_salida", sigmoidal_salida)

    if sigmoidal_salida[0] > 0.8:
        print("GIRA A LA IZQUIERDA")
    if sigmoidal_salida[1] > 0.8:
        print("AVANZA")
    if sigmoidal_salida[2] > 0.8:
        print("GIRA A LA DERECHA")