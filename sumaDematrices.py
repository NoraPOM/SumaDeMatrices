def  print_matrix(matrix):
    #print (matrix)
    for row in matrix:
        temp = "["
        for item in row:
            temp+=str(item) + ","
        print(temp[:-1] + "]") 
            
    # agrego los datos por pantalla para primera matriz

def create_matrix(size):
    matrix_0 = []
    print("A continuación vas a ingresar uno a uno de arriba hacia abajo los datos de la primera matriz: ")

    for i in range(size):
        row = []
        for j in range (size):
          # Para solicitar los datos
            a =  input("Dime el dato: ")
            row.append(int(a))
        matrix_0.append(row)
    print_matrix(matrix_0)

    # agrego los datos por pantalla para segunda matriz
    print("A continuación vas a ingresar uno a uno de arriba hacia abajo los datos de la segunda matriz: ")
    matrix_1 = []
    for i in range(size):
        row = []
        for j in range (size):
          # Para solicitar los datos
            a =  input("Dime el dato: ")
            row.append(int(a))
        matrix_1.append(row)
    print_matrix(matrix_1)

    # Vamos a sumar los datos de las matrices
    matrix_total = []
    for i in range (size):
        row = []
        for j in range (size):
            b = matrix_0[i][j] + matrix_1[i][j]
            row.append(b)
        matrix_total.append(row)

    print("Matriz definitiva sumando las dos ingresadas:")
    print_matrix(matrix_total)

def main():
    size = input("Ingrese el numero de filas y colummas de tu matriz cuadrada: ")
    create_matrix(int(size))
if __name__ == "__main__":
    main()
        
