

matriz_input = [
  [1, 2, 3, 4, 10],
  [2, 1, 2, 3, 7],
  [3, 2, 1, 2, 6],
  [4, 3, 2, 1, 5]
]


def gauss_elimination(matriz_input):

  
  matriz_aux = matriz_input
  
  
  for i in range(len(matriz_aux)):
    pivot = matriz_aux[i][i]
    for j in range(i + 1, len(matriz_aux)):
      next_element = matriz_aux[j][i]
      
      if pivot == 0 and next_element != 0:
        matriz_aux[i], matriz_aux[j] = matriz_aux[j], matriz_aux[i]
        pivot = matriz_aux[i][i]
      
      if next_element != 0:
        factor = next_element / pivot
        for col in range(len(matriz_aux[j])):
          matriz_aux[j][col] = matriz_aux[j][col] - factor * matriz_aux[i][col]
   
  print(matriz_aux)


    

          
      
    
    
      
def main():
  print("Executando método de eliminação de Gauss...")
  gauss_elimination(matriz_input)


if __name__ == "__main__":
  main()

