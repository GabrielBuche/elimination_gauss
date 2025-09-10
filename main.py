

matriz_input = [
  [0, 1, 0, 3],
  [0, 1, -1, 1],
  [2, -1, 0, 1],
  [4, 2, 0, -1]
]


def gauss_elimination(matriz_input):
  matriz_aux = matriz_input
  
  for i in range(len(matriz_aux)):
    pivot = matriz_aux[i][i]
    for j in range(i + 1, len(matriz_aux)):
      
      next_element = matriz_aux[j][i]
      
      if pivot == 0 and next_element != 0:
        matriz_aux[i], matriz_aux[j] = matriz_aux[j], matriz_aux[i]
        break
      
    
  
    
        
        
        
  
   
  
    
    
    
    
    

     




def main():
  print("Executando método de eliminação de Gauss...")
  gauss_elimination(matriz_input)


if __name__ == "__main__":
  main()

