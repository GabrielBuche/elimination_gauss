import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QTextEdit, QSpinBox,
                             QGridLayout, QMessageBox, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from .calc import gauss_elimination, substituicao_regressiva

class GaussEliminationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.matriz_inputs = []
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Eliminação de Gauss - Interface Gráfica')
        self.setGeometry(100, 100, 800, 600)
        
        layout_principal = QVBoxLayout()
        
        titulo = QLabel('Sistema de Equações Lineares - Método de Gauss')
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont('Arial', 16, QFont.Bold))
        layout_principal.addWidget(titulo)
        
        layout_tamanho = QHBoxLayout()
        layout_tamanho.addWidget(QLabel('Tamanho da matriz (n x n):'))
        
        self.spin_tamanho = QSpinBox()
        self.spin_tamanho.setRange(2, 6)
        self.spin_tamanho.setValue(4)
        self.spin_tamanho.valueChanged.connect(self.criar_matriz)
        layout_tamanho.addWidget(self.spin_tamanho)
        
        layout_tamanho.addStretch()
        layout_principal.addLayout(layout_tamanho)
        
        self.frame_matriz = QFrame()
        self.frame_matriz.setFrameStyle(QFrame.Box)
        layout_principal.addWidget(self.frame_matriz)
        
        layout_botoes = QHBoxLayout()
        
        btn_resolver = QPushButton('Resolver Sistema')
        btn_resolver.clicked.connect(self.resolver_sistema)
        btn_resolver.setFont(QFont('Arial', 12))
        layout_botoes.addWidget(btn_resolver)
        
        btn_limpar = QPushButton('Limpar')
        btn_limpar.clicked.connect(self.limpar_matriz)
        btn_limpar.setFont(QFont('Arial', 12))
        layout_botoes.addWidget(btn_limpar)
        
        btn_exemplo = QPushButton('Carregar Exemplo')
        btn_exemplo.clicked.connect(self.carregar_exemplo)
        btn_exemplo.setFont(QFont('Arial', 12))
        layout_botoes.addWidget(btn_exemplo)
        
        layout_principal.addLayout(layout_botoes)
        
        self.resultado_texto = QTextEdit()
        self.resultado_texto.setMaximumHeight(200)
        self.resultado_texto.setFont(QFont('Courier', 10))
        layout_principal.addWidget(QLabel('Resultados:'))
        layout_principal.addWidget(self.resultado_texto)
        
        self.setLayout(layout_principal)
        
        self.criar_matriz()
    
    def criar_matriz(self):
        """Cria a grade de inputs para a matriz"""
        if hasattr(self, 'layout_matriz'):
            self.limpar_layout(self.layout_matriz)
        
        self.layout_matriz = QGridLayout()
        self.matriz_inputs = []
        
        n = self.spin_tamanho.value()
        
        for j in range(n):
            label = QLabel(f'x{j+1}')
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont('Arial', 10, QFont.Bold))
            self.layout_matriz.addWidget(label, 0, j+1)
        
        label_b = QLabel('b')
        label_b.setAlignment(Qt.AlignCenter)
        label_b.setFont(QFont('Arial', 10, QFont.Bold))
        self.layout_matriz.addWidget(label_b, 0, n+1)
        
        for i in range(n):
            linha_inputs = []
            
            label_linha = QLabel(f'Eq {i+1}:')
            label_linha.setFont(QFont('Arial', 10, QFont.Bold))
            self.layout_matriz.addWidget(label_linha, i+1, 0)
            
            for j in range(n+1): 
                input_field = QLineEdit()
                input_field.setMaximumWidth(80)
                input_field.setAlignment(Qt.AlignCenter)
                linha_inputs.append(input_field)
                self.layout_matriz.addWidget(input_field, i+1, j+1)
            
            self.matriz_inputs.append(linha_inputs)
        
        self.frame_matriz.setLayout(self.layout_matriz)
    
    def limpar_layout(self, layout):
        """Remove todos os widgets de um layout"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def carregar_exemplo(self):
        """Carrega o exemplo padrão"""
        exemplo = [
            [1, 2, 3, 4, 10],
            [2, 1, 2, 3, 7],
            [3, 2, 1, 2, 6],
            [4, 3, 2, 1, 5]
        ]
        
        n = len(exemplo)
        self.spin_tamanho.setValue(n)
        
        for i in range(n):
            for j in range(n+1):
                self.matriz_inputs[i][j].setText(str(exemplo[i][j]))
    
    def limpar_matriz(self):
        """Limpa todos os campos da matriz"""
        for linha in self.matriz_inputs:
            for input_field in linha:
                input_field.clear()
        self.resultado_texto.clear()
    
    def obter_matriz(self):
        """Obtém a matriz dos inputs"""
        try:
            matriz = []
            n = self.spin_tamanho.value()
            
            for i in range(n):
                linha = []
                for j in range(n+1):
                    valor_texto = self.matriz_inputs[i][j].text().strip()
                    if not valor_texto:
                        raise ValueError(f"Campo vazio na posição ({i+1}, {j+1})")
                    
                    valor = float(valor_texto)
                    linha.append(valor)
                
                matriz.append(linha)
            
            return matriz
        
        except ValueError as e:
            QMessageBox.warning(self, "Erro", f"Entrada inválida: {str(e)}")
            return None
    
    def resolver_sistema(self):
        """Resolve o sistema usando eliminação de Gauss"""
        matriz = self.obter_matriz()
        if matriz is None:
            return
        
        try:
            matriz_copia = [linha[:] for linha in matriz]
            
            self.resultado_texto.clear()
            self.resultado_texto.append("=== RESOLUÇÃO DO SISTEMA ===\n")
            self.resultado_texto.append("Matriz inicial:")
            self.mostrar_matriz(matriz_copia)
            
            solucao = gauss_elimination(matriz_copia)
            
            self.resultado_texto.append("\n=== SOLUÇÃO FINAL ===")
            for i, valor in enumerate(solucao):
                self.resultado_texto.append(f"x{i+1} = {valor:.6f}")
            
            self.resultado_texto.append("\n=== VERIFICAÇÃO ===")
            self.verificar_solucao(matriz, solucao)
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao resolver sistema: {str(e)}")
    
    def mostrar_matriz(self, matriz):
        """Mostra a matriz formatada"""
        for linha in matriz:
            linha_str = "[ " + " ".join(f"{x:8.3f}" for x in linha) + " ]"
            self.resultado_texto.append(linha_str)
        self.resultado_texto.append("")
    
    def verificar_solucao(self, matriz_original, solucao):
        """Verifica se a solução está correta"""
        n = len(solucao)
        for i in range(n):
            soma = sum(matriz_original[i][j] * solucao[j] for j in range(n))
            esperado = matriz_original[i][n]
            erro = abs(soma - esperado)
            self.resultado_texto.append(f"Equação {i+1}: {soma:.6f} ≈ {esperado:.6f} (erro: {erro:.2e})")

