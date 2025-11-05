import cv2
from matplotlib import pyplot as plt

# Carrega a imagem colorida
foto = cv2.imread("../img/img01.jpeg")

# Converte para escala de cinza
foto_gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

# Calcula histograma da imagem em escala de cinza
hist = cv2.calcHist([foto_gray], [0], None, [256], [0, 256])

# Inicializa vetor para contar pixels por nível de cinza
val = [0] * 256

altura = len(foto_gray)
largura = len(foto_gray[0])

# Conta pixels e aplica limiar fixo 128 para binarização
for i in range(altura - 1):
    for j in range(largura - 1):
        aux = foto_gray[i][j]
        val[aux] += 1

        # Binariza: pixels > 128 ficam brancos, senão pretos
        if foto_gray[i][j] > 128:
            foto_gray[i][j] = 255
        else:
            foto_gray[i][j] = 0

# Exibe imagem binarizada
cv2.imshow("Imagem em Preto e Branco", foto_gray)
cv2.imwrite("../img/limiar/img_limiarizada.png", foto_gray)

# Plota o histograma
plt.figure()
plt.title("Histograma em Escala de Cinza")
plt.xlabel("Pontos")
plt.ylabel("Precença dos Pixels")
plt.plot(val, color='black')
plt.xlim([0, 256])
plt.show()

# Fecha janela ao pressionar 'q'
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
