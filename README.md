# Sistema de Equações Lineares - Eliminação de Gauss

## 📋 Descrição
Este programa implementa o método de eliminação de Gauss para resolver sistemas de equações lineares com uma interface gráfica intuitiva desenvolvida em PyQt5.

## 🚀 Como Usar

### Opção 1: Executar o código Python
```bash
python3 main.py
```

### Opção 2: Executar o executável (Recomendado)
```bash
./dist/GaussElimination
```

## 💻 Funcionalidades

- **Interface Gráfica Intuitiva**: Entrada visual para coeficientes das equações
- **Tamanhos Flexíveis**: Suporte para matrizes de 2x2 até 6x6
- **Troca de Linhas Automática**: Lida automaticamente com pivôs zero
- **Resultados Detalhados**: Mostra o processo completo de eliminação
- **Verificação**: Confirma automaticamente se a solução está correta
- **Exemplos Pré-definidos**: Botão para carregar matriz de exemplo

## 📁 Estrutura dos Arquivos

```
├── main.py              # Arquivo principal (inicializa a interface)
├── src/                 # Pasta com módulos do projeto
│   ├── __init__.py      # Torna src um pacote Python
│   ├── calc.py          # Funções de cálculo (eliminação de Gauss)
│   └── interface.py     # Interface gráfica PyQt5
├── build_universal.py   # Script universal para build (Windows/Linux/macOS)
├── build_windows.bat    # Script específico para Windows
├── build_linux.sh       # Script específico para Linux/macOS
├── dist/
│   └── GaussElimination # Executável standalone (Linux)
│   └── GaussElimination.exe # Executável standalone (Windows)
├── README.md            # Este arquivo
└── BUILD_GUIDE.md       # Guia detalhado de build
```

## 🛠️ Instalação e Build

### Opção 1: Script Universal (Recomendado)
Funciona em **Windows**, **Linux** e **macOS**:
```bash
# Executar script universal
python build_universal.py
```

### Opção 2: Scripts Específicos

**Windows:**
```cmd
# Executar arquivo batch
build_windows.bat
```

**Linux/macOS:**
```bash
# Executar script bash
./build_linux.sh
```

### Opção 3: Comando Manual

**Windows:**
```cmd
python -m PyInstaller --onefile --noconsole --name="GaussElimination" main.py
```

**Linux/macOS:**
```bash
python3 -m PyInstaller --onefile --noconsole --name="GaussElimination" main.py
```

## 📖 Como Usar a Interface

1. **Escolher Tamanho**: Selecione o tamanho da matriz (n×n)
2. **Inserir Coeficientes**: Digite os valores dos coeficientes e termos independentes
3. **Resolver**: Clique em "Resolver Sistema"
4. **Ver Resultados**: Os valores de x₁, x₂, ..., xₙ aparecerão na área de resultados

## 🔧 Botões Disponíveis

- **Resolver Sistema**: Executa a eliminação de Gauss
- **Limpar**: Limpa todos os campos
- **Carregar Exemplo**: Carrega uma matriz de exemplo 4×4

## ⚠️ Notas Técnicas

- O programa lida automaticamente com pivôs zero através de troca de linhas
- A verificação da solução é feita substituindo os valores encontrados nas equações originais
- O executável tem ~48MB e não requer instalação do Python

## 👨‍💻 Desenvolvedor
Gabriel Buche - Cálculo Numérico

## 📝 Exemplo de Sistema
```
x₁ + 2x₂ + 3x₃ + 4x₄ = 10
2x₁ + x₂ + 2x₃ + 3x₄ = 7
3x₁ + 2x₂ + x₃ + 2x₄ = 6
4x₁ + 3x₂ + 2x₃ + x₄ = 5
```

Solução: x₁ = -2, x₂ = 3, x₃ = 1, x₄ = 0
