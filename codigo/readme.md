## **Filtros de Suavização (Passa-Baixa)**

\-\> Os filtros são de grande importância na visão computacional, pois quando adquirimos uma base de dados visual, muitas vezes, pode apresentar **ruído**; e para evitar erros devido à presença desse ruído, aplicamos diversos tipos de filtros para minimizar ao máximo o distúrbio que podem causar no resultado final. Esses filtros são chamados de **Passa-Baixa** ou **Filtros de Suavização**.

\-\> Esse repositório apresenta a aplicação manual (no arquivo `simple_filt.py`) do filtro de média e do filtro de mediana, ambos muito conhecidos:

  * **Filtro de média:** Substitui cada pixel da imagem pela média dos valores dos pixels vizinhos.
      * **Efeito:** Remove detalhes finos e pequenas texturas, resultando em uma imagem mais suave/embaçada.
  * **Filtro de mediana:** Substitui cada pixel pelo valor mediano dos pixels em sua vizinhança.
      * **Efeito:** Remove ruído sal e pimenta (pontos brancos/preto isolados).

<p align="center"\>
    <img src="img/img00.jpeg" width="250"/\>
    <img src="img/simple_filt/saida_med.png" width="250"/\>
    <img src="img/simple_filt/saida_median.png" width="250"/\>
</p\>

* Essas três imagens PARECEM iguais, devido ao tamanho do filtro usado ter sido pequeno, mas ao abrir em seu próprio computador, irão apresentar um leve **BLUR**.

-----

## **Detecção de Bordas (Filtros de Realce/Passa-Alta)**

\-\> A detecção de bordas utiliza métodos matemáticos para identificar pontos em uma imagem onde há uma **mudança significativa na luminosidade** das intensidades dos pixels.

<p align="center"\>
    <img src="img/img00.jpeg" width="250"/\>
    <img src="img/detec_board/board_manual.png" width="250"/\>
    <img src="img/detec_board/board_filtrada.png" width="250"/\>
</p\>

\-\> Os filtros de realce (também chamados de **Passa-Alta** ou de **Filtros de Gradiente**) enfatizam as regiões de bordas e os ruídos, e não enfatizam regiões constantes ou com variações de intensidade suaves.

\-\> O arquivo `detec_board.py` demonstra a aplicação de um **filtro de detecção de bordas horizontais**, que é um tipo de filtro de primeira derivada:

  * **Filtros de Primeira Derivada (Gradiente):** Baseiam-se na primeira derivada espacial da imagem para encontrar bordas.

      * **Exemplos Comuns:** Operadores de **Sobel** e Prewitt. O operador de Sobel utiliza dois *kernels* (máscaras) para calcular as derivadas parciais nas direções $x$ e $y$ (horizontal e vertical), permitindo encontrar bordas em ambas as direções. O gradiente resultante representa a magnitude e a direção das bordas.

  * **Filtros de Segunda Derivada:** Utilizam a segunda derivada espacial da imagem.

      * **Exemplos Comuns:** Operador **Laplaciano**. O Laplaciano é uma medida isotrópica bidimensional da derivada de segunda ordem. Ele realça transições abruptas de intensidade, como bordas, mas é sensível ao ruído e é frequentemente usado em conjunto com técnicas de suavização (como no Laplaciano do Gaussiano - LoG). O Laplaciano é geralmente mais rápido de ser computado que o Sobel.

O filtro implementado em `detec_board.py` usa o seguinte *kernel* para detecção de bordas horizontais (componente $G_x$, que enfatiza bordas verticais):

<p align="center"\>
    <img src="img/temp/matriz_kernel.png" width="250"/\>
</p\>

* Este *kernel* corresponde ao filtro de Sobel na direção $x$.

* A demonstração em `detec_board.py` compara a aplicação do filtro usando a função `cv2.filter2D` e uma implementação manual com *loop* e *padding*. A implementação manual inclui a conversão para `np.int16` para permitir valores negativos do gradiente (diferença) antes do *clip* e conversão final para `np.uint8`.

## **Manipulação de Gama (Correção de Gama)**

A **manipulação de gama**, ou **correção de gama**, é uma técnica fundamental no processamento de imagens usada para ajustar a **luminosidade não linear** dos pixels. Câmeras, sensores e monitores possuem respostas luminosas diferentes, e a correção de gama serve para compensar essas variações e **melhorar o contraste perceptível** da imagem.

A transformação de gama segue a relação matemática:

\[
I_{\text{out}} = I_{\text{in}}^{\gamma}
\]

onde:
- \( I_{\text{in}} \) é o valor de entrada do pixel (normalizado entre 0 e 1),
- \( I_{\text{out}} \) é o valor resultante após a correção,
- \( \gamma \) é o fator de correção gama.

---

### **Compreendendo o efeito do gama**

O gráfico abaixo mostra como o valor de saída (eixo Y) se relaciona ao valor de entrada (eixo X) para diferentes valores de \( \gamma \):

<p align="center">
    <img src="img/Gamma-Correction-Graph.jpg" width="500"/>
</p>

 **Interpretação:**
- Curvas **côncavas** (γ < 1) — *clareiam* a imagem, realçando detalhes em regiões escuras.  
- Curvas **lineares** (γ = 1) — mantêm a imagem original.  
- Curvas **convexas** (γ > 1) — *escurecem* a imagem, realçando detalhes em áreas claras.

Essas transformações permitem **controlar o contraste dinâmico** e adaptar a imagem à forma como o olho humano percebe a luz.

---

###  **Importância da Correção de Gama**

Ajustar o gama é essencial em diversas áreas:

-  **Melhora o contraste dinâmico:**  
  Gamas menores (< 1) tornam a imagem mais clara, evidenciando detalhes em sombras.  

-  **Realça regiões escuras ou claras:**  
  Gamas maiores (> 1) tornam a imagem mais escura, evitando o “lavado” causado por brilho excessivo.  

-  **Correção de exibição:**  
  Essencial para calibrar imagens exibidas em diferentes telas, evitando distorções de luminosidade.  

-  **Visão computacional e machine learning:**  
  Usado como pré-processamento para melhorar o reconhecimento de padrões e objetos sob diferentes condições de iluminação.

---

###  **Implementação prática**

O arquivo [`gama_manipulation.py`](gama_manipulation.py) demonstra a aplicação manual da correção de gama em tons de cinza, processando cada pixel individualmente:

---

## **Manipulação de Gama (Correção de Gama)**

A **manipulação de gama**, ou **correção de gama**, é uma técnica fundamental no processamento de imagens usada para ajustar a **luminosidade não linear** dos pixels. Câmeras, sensores e monitores possuem respostas luminosas diferentes, e a correção de gama serve para compensar essas variações e **melhorar o contraste perceptível** da imagem.

A transformação de gama segue a relação matemática:

\[
I_{\text{out}} = I_{\text{in}}^{\gamma}
\]

onde:
- \( I_{\text{in}} \) é o valor de entrada do pixel (normalizado entre 0 e 1),
- \( I_{\text{out}} \) é o valor resultante após a correção,
- \( \gamma \) é o fator de correção gama.



-> **Compreendendo o efeito do gama**

O gráfico abaixo mostra como o valor de saída (eixo Y) se relaciona ao valor de entrada (eixo X) para diferentes valores de \( \gamma \):

<p align="center">
    <img src="img/temp/Gamma-Correction-Graph.jpg" width="500"/>
</p>

-> **Interpretação:**
- Curvas **côncavas** (γ < 1) — *clareiam* a imagem, realçando detalhes em regiões escuras.  
- Curvas **lineares** (γ = 1) — mantêm a imagem original.  
- Curvas **convexas** (γ > 1) — *escurecem* a imagem, realçando detalhes em áreas claras.

Essas transformações permitem **controlar o contraste dinâmico** e adaptar a imagem à forma como o olho humano percebe a luz.

-> **Importância da Correção de Gama**

Ajustar o gama é essencial em diversas áreas:

-  **Melhora o contraste dinâmico:**  
  Gamas menores (< 1) tornam a imagem mais clara, evidenciando detalhes em sombras.  

-  **Realça regiões escuras ou claras:**  
  Gamas maiores (> 1) tornam a imagem mais escura, evitando o “lavado” causado por brilho excessivo.  

-  **Correção de exibição:**  
  Essencial para calibrar imagens exibidas em diferentes telas, evitando distorções de luminosidade.  

-  **Visão computacional e machine learning:**  
  Usado como pré-processamento para melhorar o reconhecimento de padrões e objetos sob diferentes condições de iluminação.


<p align="center">
    <img src="img/gama/gama_exp.png" width="150"/>
    <img src="img/gama/gama_log.png" width="150"/>
    <img src="img/gama/gama_quad.png" width="150"/>
    <img src="img/gama/gama_raiz.png" width="150"/>
</p>

---

