#!/bin/bash

echo "Gerando executável da Eliminação de Gauss para Linux..."

# Comando PyInstaller para Linux
python3 -m PyInstaller \
    --onefile \
    --name="GaussElimination" \
    --add-data="src:src" \
    --hidden-import="src.calc" \
    --hidden-import="src.interface" \
    --hidden-import="PyQt5.QtWidgets" \
    --hidden-import="PyQt5.QtCore" \
    --hidden-import="PyQt5.QtGui" \
    --noconsole \
    main.py

echo ""
echo "✅ Executável gerado em dist/GaussElimination"
echo "Para executar: ./dist/GaussElimination"
