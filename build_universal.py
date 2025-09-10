#!/usr/bin/env python3
"""
Script universal para gerar executável da Eliminação de Gauss
Funciona em Windows, Linux e macOS
"""

import os
import platform
import subprocess
import sys

def install_requirements():
    """Instala dependências necessárias"""
    print("🔧 Verificando dependências...")
    
    try:
        import PyQt5
        print("✅ PyQt5 encontrado")
    except ImportError:
        print("❌ PyQt5 não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])
    
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado")
    except ImportError:
        print("❌ PyInstaller não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """Gera o executável usando PyInstaller"""
    system = platform.system()
    print(f"🖥️  Sistema detectado: {system}")
    print("🔨 Gerando executável da Eliminação de Gauss...")
    
    # Comando Python baseado no sistema
    python_cmd = "python" if system == "Windows" else "python3"
    
    # Separador para --add-data baseado no sistema
    separator = ";" if system == "Windows" else ":"
    
    # Comando PyInstaller
    cmd = [
        python_cmd, "-m", "PyInstaller",
        "--onefile",
        "--name=GaussElimination",
        "--noconsole",
        f"--add-data=src{separator}src",
        "--hidden-import=src.calc",
        "--hidden-import=src.interface", 
        "--hidden-import=PyQt5.QtWidgets",
        "--hidden-import=PyQt5.QtCore",
        "--hidden-import=PyQt5.QtGui",
        "main.py"
    ]
    
    try:
        print("⏳ Gerando executável (isso pode demorar alguns minutos)...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            if system == "Windows":
                executable_path = "dist\\GaussElimination.exe"
                run_command = "dist\\GaussElimination.exe"
            else:
                executable_path = "dist/GaussElimination"
                run_command = "./dist/GaussElimination"
            
            # Verificar se o arquivo foi criado
            if os.path.exists(executable_path):
                # Obter tamanho do arquivo
                size_mb = os.path.getsize(executable_path) / (1024 * 1024)
                
                print("\n🎉 SUCESSO!")
                print(f"✅ Executável gerado: {executable_path}")
                print(f"📦 Tamanho: {size_mb:.1f} MB")
                print(f"🚀 Para executar: {run_command}")
                
                # Tornar executável no Linux/Mac
                if system != "Windows":
                    os.chmod(executable_path, 0o755)
                    print("🔧 Permissões de execução definidas")
                    
            else:
                print("❌ Erro: Executável não foi criado")
                print("📝 Output:", result.stdout)
                print("📝 Errors:", result.stderr)
        else:
            print("❌ Erro ao gerar executável")
            print("📝 Output:", result.stdout) 
            print("📝 Errors:", result.stderr)
            
    except FileNotFoundError:
        print(f"❌ Erro: {python_cmd} não encontrado")
        print("💡 Instale o Python e tente novamente")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def clean_build_files():
    """Remove arquivos temporários de build"""
    import shutil
    
    dirs_to_clean = ["build", "__pycache__"]
    files_to_clean = ["*.spec"]
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🧹 Removido: {dir_name}/")
    
    import glob
    for pattern in files_to_clean:
        for file_path in glob.glob(pattern):
            os.remove(file_path)
            print(f"🧹 Removido: {file_path}")

def main():
    """Função principal"""
    print("=" * 50)
    print("🎯 GERADOR DE EXECUTÁVEL - ELIMINAÇÃO DE GAUSS")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    required_files = ["main.py", "src/calc.py", "src/interface.py"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Arquivos não encontrados: {', '.join(missing_files)}")
        print("💡 Execute este script no diretório do projeto")
        return
    
    try:
        # Instalar dependências
        install_requirements()
        print()
        
        # Gerar executável
        build_executable()
        print()
        
        # Perguntar se quer limpar arquivos temporários
        response = input("🧹 Limpar arquivos temporários? (s/N): ").strip().lower()
        if response in ['s', 'sim', 'y', 'yes']:
            clean_build_files()
        
        print("\n✨ Processo concluído!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Processo cancelado pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {e}")

if __name__ == "__main__":
    main()
