

matriz_input = [
  [1, 2, 3, 4, 10],
  [2, 1, 2, 3, 7],
  [3, 2, 1, 2, 6],
  [4, 3, 2, 1, 5]
]

def substituicao_regressiva(matriz_coeficientes, vetor_resultados):
    n = len(matriz_coeficientes)
    x = [0] * n
  
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matriz_coeficientes[i][j] * x[j]
        
        x[i] = (vetor_resultados[i] - soma) / matriz_coeficientes[i][i]
        print(f"x[{i}] = {x[i]:.4f}")
    
    return x

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
   
  matriz_coeficientes = []
  matriz_resultados = []
  
  for linha in matriz_aux:
    matriz_coeficientes.append(linha[:-1])  # Todas as colunas exceto a última
    matriz_resultados.append(linha[-1])  
    
  solucao = substituicao_regressiva(matriz_coeficientes, matriz_resultados)
  print("Solução:", solucao)
  return solucao
  

    
def main():
  print("Executando método de eliminação de Gauss...")
  gauss_elimination(matriz_input)



if __name__ == "__main__":
  main()

