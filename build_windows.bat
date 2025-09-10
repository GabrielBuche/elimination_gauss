@echo off
echo Gerando executável da Eliminação de Gauss para Windows...

REM Comando PyInstaller para Windows
python -m PyInstaller ^
    --onefile ^
    --name="GaussElimination" ^
    --add-data="src;src" ^
    --hidden-import="src.calc" ^
    --hidden-import="src.interface" ^
    --hidden-import="PyQt5.QtWidgets" ^
    --hidden-import="PyQt5.QtCore" ^
    --hidden-import="PyQt5.QtGui" ^
    --noconsole ^
    main.py

echo.
echo Executável gerado em dist\GaussElimination.exe
echo Para executar: dist\GaussElimination.exe
pause
