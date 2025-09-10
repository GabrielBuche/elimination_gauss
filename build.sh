#!/bin/bash

echo "Gerando executável da Eliminação de Gauss..."

# Comando PyInstaller simples
/bin/python3 -m PyInstaller \
    --onefile \
    --name="GaussElimination" \
    --add-data="calc.py:." \
    --add-data="interface.py:." \
    --hidden-import="calc" \
    --hidden-import="interface" \
    --hidden-import="PyQt5.QtWidgets" \
    --hidden-import="PyQt5.QtCore" \
    --hidden-import="PyQt5.QtGui" \
    --noconsole \
    main.py

echo "Executável gerado em dist/GaussElimination"
echo "Para executar: ./dist/GaussElimination"
