# 🔨 Guia de Build Multiplataforma

Este guia explica como gerar executáveis para diferentes sistemas operacionais.

## 🎯 Scripts Disponíveis

### 1. **build_universal.py** (Recomendado)
- ✅ Funciona em **Windows**, **Linux** e **macOS**
- ✅ Detecta automaticamente o sistema operacional
- ✅ Instala dependências automaticamente
- ✅ Interface amigável com emojis e cores
- ✅ Limpeza automática de arquivos temporários

### 2. **build_windows.bat**
- ✅ Específico para **Windows**
- ✅ Arquivo batch nativo
- ✅ Pausa no final para ver resultados

### 3. **build_linux.sh**
- ✅ Específico para **Linux/macOS** 
- ✅ Script bash nativo
- ✅ Colorido e informativo

## 🚀 Como Usar

### Windows

**Opção 1 - Script Universal:**
```cmd
python build_universal.py
```

**Opção 2 - Arquivo Batch:**
```cmd
build_windows.bat
```

**Opção 3 - Comando Direto:**
```cmd
python -m PyInstaller --onefile --noconsole --name="GaussElimination" main.py
```

### Linux/macOS

**Opção 1 - Script Universal:**
```bash
python3 build_universal.py
```

**Opção 2 - Script Bash:**
```bash
./build_linux.sh
```

**Opção 3 - Comando Direto:**
```bash
python3 -m PyInstaller --onefile --noconsole --name="GaussElimination" main.py
```

## 📦 Arquivos Gerados

### Windows
- **Executável**: `dist\GaussElimination.exe`
- **Tamanho**: ~50-60 MB
- **Formato**: Executável Windows PE

### Linux
- **Executável**: `dist/GaussElimination`
- **Tamanho**: ~45-55 MB  
- **Formato**: ELF executável

### macOS
- **Executável**: `dist/GaussElimination`
- **Tamanho**: ~45-55 MB
- **Formato**: Mach-O executável

## ⚡ Parâmetros PyInstaller

| Parâmetro | Função |
|-----------|--------|
| `--onefile` | Gera um único arquivo executável |
| `--noconsole` | Remove janela do console (GUI apenas) |
| `--name="Nome"` | Define nome do executável |
| `--add-data` | Inclui arquivos adicionais |
| `--hidden-import` | Força importação de módulos |

## 🎨 Diferenças entre Sistemas

### Separadores --add-data
- **Windows**: `;` (ponto e vírgula)
- **Linux/macOS**: `:` (dois pontos)

### Comandos Python
- **Windows**: `python`
- **Linux/macOS**: `python3`

### Extensões
- **Windows**: `.exe`
- **Linux/macOS**: sem extensão

## 🔧 Dependências Necessárias

```bash
pip install PyQt5 pyinstaller
```

## 📝 Exemplo de Uso Completo

```bash
# 1. Clonar/baixar o projeto
git clone <repository-url>
cd code_eli_gauss

# 2. Instalar dependências
pip install PyQt5 pyinstaller

# 3. Gerar executável
python build_universal.py

# 4. Executar
# Windows: dist\GaussElimination.exe
# Linux: ./dist/GaussElimination
```

## ⚠️ Observações Importantes

1. **Antivírus**: Alguns antivírus podem detectar falsamente executáveis PyInstaller
2. **Tamanho**: O executável contém todo o interpretador Python e dependências
3. **Compatibilidade**: Execute no sistema onde será usado para máxima compatibilidade
4. **Arquitetura**: Gera executáveis para a arquitetura do sistema atual (x86/x64/ARM)

## 🐛 Solução de Problemas

### "Python não encontrado"
- Instale Python 3.8+ e adicione ao PATH

### "PyInstaller não encontrado"  
- Execute: `pip install pyinstaller`

### "PyQt5 não encontrado"
- Execute: `pip install PyQt5`

### Executável não abre
- Verifique dependências do sistema
- Execute em terminal para ver erros
- Recompile no sistema de destino
