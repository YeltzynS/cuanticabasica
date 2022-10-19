import math
import numpy as np


def normavec(v):
    vecconj = []
    for i in range(len(v)):
        a = np.conj(v[i])
        vecconj.append(a)
    vecdaga = np.array(vecconj)
    vecdaga = np.array([vecdaga])
    vecdaga = (vecdaga.T)
    norma = np.dot(v, vecdaga)
    norma = norma.real
    norma = math.sqrt(norma)
    return norma

def proba_pos(v, pos):

    norma = normavec(v)
    modulo = abs(v[pos])
    m = modulo ** 2
    n = norma ** 2
    m = int(m)
    n = int(n)
    prob = m / n
    return prob


def proba_2_vect(v1, v2):
    vecconjv1 = []
    for i in range(len(v1)):
        a = np.conj(v1[i])
        vecconjv1.append(a)
    vecdagav1 = np.array(vecconjv1)
    vecdagav1 = np.array([vecdagav1])
    vecdagav1 = (vecdagav1.T)
    normav1 = np.dot(v1, vecdagav1)
    normav1 = normav1.real
    normav1 = math.sqrt(normav1)
    vecconjv2 = []
    for i in range(len(v2)):
        a = np.conj(v2[i])
        vecconjv2.append(a)
    vecdagav2 = np.array(vecconjv2)
    vecdagav2 = np.array([vecdagav2])
    vecdagav2 = (vecdagav2.T)
    normav2 = np.dot(v2, vecdagav2)
    normav2 = normav2.real
    normav2 = math.sqrt(normav2)
    for i in range(len(v1)):
        v1[i] = v1[i]/normav1
    for i in range(len(v2)):
        v2[i] = v2[i]/normav2
    vecprodint = np.dot(v1,v2)
    return vecprodint.round(0)



def amplitud(v1, v2):
    vecconjv1 = []
    for i in range(len(v1)):
        a = np.conj(v1[i])
        vecconjv1.append(a)
    vecdagav1 = np.array(vecconjv1)
    vecdagav1 = np.array([vecdagav1])
    vecdagav1 = (vecdagav1.T)
    normav1 = np.dot(v1, vecdagav1)
    normav1 = normav1.real
    normav1 = math.sqrt(normav1)
    vecconjv2 = []
    for i in range(len(v2)):
        a = np.conj(v2[i])
        vecconjv2.append(a)
    vecdagav2 = np.array(vecconjv2)
    vecdagav2 = np.array([vecdagav2])
    vecdagav2 = (vecdagav2.T)
    normav2 = np.dot(v2, vecdagav2)
    normav2 = normav2.real
    normav2 = math.sqrt(normav2)
    for i in range(len(v1)):
        v1[i] = v1[i]/normav1
    for i in range(len(v2)):
        v2[i] = v2[i]/normav2
    vecprodint = np.dot(v1,v2)
    return vecprodint.round(0)

def matherm(m):
    m = np.array(m)
    x = np.array(m)
    x = np.conj(m)
    x = x.T
    if np.array_equal(x, m):
        return True
    return False


def media(m, v):
    norma = normavec(v)
    for i in range(len(v)):
        v[i] = v[i]/norma
    vecconj = np.conj(v)
    m = np.array(m)
    x = np.array(v)
    x = np.array([x])
    v = (x.T)
    resultado = np.dot(m,x)
    respuesta = np.dot(vecconj, resultado)
    return respuesta.real
def varianza(m, v):
    return 0

def matobse_Ket(m, v):
    m = np.array(m)
    v = np.array(v)
    a = matherm(m)
    if a == True:
        b = media(m, v)
        c = varianza(m, v)
        print("La media es:")
        print(float(b))
        print("la varianza es:")
        print(float(c))
    elif a != True:
        return "La matriz no es hermitiana"


