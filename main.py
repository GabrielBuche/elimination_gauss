
import sys
from PyQt5.QtWidgets import QApplication
from interface import GaussEliminationGUI

def main():
  app = QApplication(sys.argv)
  
  app.setStyleSheet("""
      QWidget {
          font-family: Arial;
      }
      QPushButton {
          padding: 8px 16px;
          background-color: #4CAF50;
          color: white;
          border: none;
          border-radius: 4px;
      }
      QPushButton:hover {
          background-color: #45a049;
      }
      QLineEdit {
          padding: 4px;
          border: 1px solid #ccc;
          border-radius: 3px;
      }
      QTextEdit {
          border: 1px solid #ccc;
          border-radius: 3px;
      }
  """)
  
  janela = GaussEliminationGUI()
  janela.show()
  
  sys.exit(app.exec_())



if __name__ == "__main__":
  main()

