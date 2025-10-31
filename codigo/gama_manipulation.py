import cv2
import math

foto = cv2.imread("img/img00.jpeg")  # Lê a imagem
if foto is None:
    print("Erro ao carregar a imagem.")
    exit()
foto_gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)  # Converte a imagem para tons de cinza

# Cria cópias da imagem original para aplicar diferentes correções gama
foto_gray_gama_exp = foto_gray.copy()
foto_gray_gama_quad = foto_gray.copy()  
foto_gray_gama_log = foto_gray.copy() 
foto_gray_gama_raiz = foto_gray.copy() 

#Obtém a altura e largura da imagem
altura = len(foto_gray) 
largura = len(foto_gray[0])  

for i in range(altura): 
    for j in range(largura):  

        # Aplica correção gama exponencial (x^5)
        foto_gray_gama_exp[i][j] = float(((foto_gray[i][j]/255) ** 5)*255)

        # Aplica correção gama quadrática (x^2)
        foto_gray_gama_quad[i][j] = float(((foto_gray[i][j]/255) ** 2)*255)

        # Aplica correção gama logarítmica (base e)
        if foto_gray[i][j]== 0:
            foto_gray_gama_log[i][j] = math.log(1) * 255 / math.log(256) # Evita log(0) que é indefinido
        else:
            foto_gray_gama_log[i][j] =  math.log(foto_gray[i][j]) * 255 / math.log(255)

        # Aplica correção gama de raiz quadrada (x^(1/2))
        foto_gray_gama_raiz[i][j] = math.sqrt(foto_gray[i][j]) * 255 / math.sqrt(255)

# Exibe as imagens
cv2.imshow("Imagem em Preto e Branco", foto_gray)
cv2.imshow("Imagem Gama Exponencial", foto_gray_gama_exp) 
cv2.imwrite("img/gama/gama_exp.png", foto_gray_gama_exp) 
cv2.imshow("Imagem Gama Quadrado", foto_gray_gama_quad)
cv2.imwrite("img/gama/gama_quad.png", foto_gray_gama_quad) 
cv2.imshow("Imagem Gama Logaritmo", foto_gray_gama_log) 
cv2.imwrite("img/gama/gama_log.png", foto_gray_gama_log) 
cv2.imshow("Imagem Gama Raiz Quadrada", foto_gray_gama_raiz)
cv2.imwrite("img/gama/gama_raiz.png", foto_gray_gama_raiz) 

# Espera até que a tecla 'q' seja pressionada para fechar as janelas
if cv2.waitKey(0) == ord('q'): 
    cv2.destroyAllWindows()  