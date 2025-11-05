import cv2
from matplotlib import pyplot as plt
import numpy as np

# Carrega a imagem e converte para escala de cinza
foto = cv2.imread("../img/img01.jpeg")
foto_gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

# Calcula histograma com OpenCV (não é usado no algoritmo abaixo)
hist = cv2.calcHist([foto_gray], [0], None, [256], [0, 256])

# Inicializa variáveis para histograma manual e cálculo de Otsu
val = [0] * 256        # Histograma manual
prob = [0] * 256       # Probabilidade p(i)
mu = [0] * 256         # Média acumulada μ(t)
omega = [0] * 256      # Probabilidade acumulada ω(t)
mu_acumulada = 0
mu_t = 0               # Média total da imagem

altura = len(foto_gray)
largura = len(foto_gray[0])

# Calcula o histograma manual
for i in range(altura - 1):
    for j in range(largura - 1):
        aux = foto_gray[i][j]
        val[aux] += 1

# Calcula p(i), ω(t), μ(t) e μ total
for x in range(256):
    prob[x] = val[x] / (altura * largura)  # probabilidade
    omega[x] = prob[x] + (omega[x - 1] if x > 0 else 0)  # acumulada
    mu_acumulada += prob[x] * x
    mu[x] = mu_acumulada
    mu_t += prob[x] * x  # média total

# Converte listas para arrays para facilitar o cálculo
prob = np.array(prob)
omega = np.array(omega)

# Calcula variância entre classes σ_b²(t)
sigma_b_squared = (mu_t * omega - mu)**2 / (omega * (1 - omega) + 1e-10)

# Encontra o melhor t (limiar de Otsu)
otsu_thresh = np.argmax(sigma_b_squared)
print(f'Limiar de Otsu encontrado: {otsu_thresh}')

# Aplica o limiar à imagem
for i in range(altura):
    for j in range(largura):
        foto_gray[i][j] = 255 if foto_gray[i][j] > otsu_thresh else 0

# Exibe a imagem binarizada
cv2.imshow("Imagem em Preto e Branco", foto_gray)
cv2.imwrite("../img/limiar/img_limiarizada_otsu.png", foto_gray)

# Plota histograma com matplotlib
plt.figure()
plt.title("Histograma em Escala de Cinza")
plt.xlabel("Pontos")  
plt.ylabel("Precença dos Pixels")
plt.plot(val, color='black')
plt.xlim([0, 256])
plt.show()

# Fecha a janela ao pressionar 'q'
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
