def triangulo(H, B):

    area = (H * B/2)

    return area

opc = input ("escoja 1 triangulo")

if opc == 1:
    H = input ("introduzca su altura: ")

    B = input ("introduzca su base: ")

    print triangulo (H, B)
