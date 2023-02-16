import pytesseract
import cv2

# Carrega a imagem
imagem = cv2.imread('imagem.jpg')

# Converte a imagem para escala de cinza (opcional)
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica um threshold para transformar a imagem em binária
ret, imagem = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

# Salva a imagem em escala de cinza
cv2.imwrite('imagem_cinza.jpg', imagem)

# Configura o tesseract com o caminho do executável
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Path do executável do tesseract (pode ser necessário alterar)

# dica : 'which tesseract' no terminal para descobrir o path do tesseract no linux e 'where tesseract' no windows.

# Path default do tesseract no Linux (Ubuntu): r'/usr/bin/tesseract'
# Path default do tesseract no Windows : r'C:\Users\Python\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Lê o texto da imagem
texto = pytesseract.image_to_string(imagem, lang='por')

# Imprime o texto lido
print(texto)

# Salva o texto lido em um arquivo
with open('texto.txt', 'w') as arquivo:
    arquivo.write(texto)




