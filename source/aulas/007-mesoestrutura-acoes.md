# Aula 07: Mesoestrutura — ações horizontais e distribuição entre os apoios

```{admonition} Onde estamos?
:class: destaque-azul

1. Conceitos gerais sobre o projeto de pontes
2. Ações na superestrutura
3. Análise computacional com carga móvel
4. Dimensionamento da longarina
5. Dimensionamento do tabuleiro
6. Dimensionamento da transversina
7. **Mesoestrutura: ações horizontais e distribuição entre os apoios (esta aula)**
8. Dimensionamento dos pilares
9. Fundações em tubulão

A mesoestrutura recebe as cargas verticais da superestrutura e todas as forças horizontais que atuam na ponte. Esta aula quantifica essas forças e mostra como elas se distribuem entre os pilares, de acordo com a rigidez de cada apoio.
```

## 1. Do tabuleiro aos pilares

### 1.1 Caminho das forças horizontais

Como o tabuleiro é monolítico, seus deslocamentos horizontais são transmitidos ao topo de cada pilar através dos aparelhos de apoio. Taguti [[1]](#ref-1) agrupa as ações que solicitam os pilares em:

- **esforços longitudinais aplicados no tabuleiro:** frenagem e aceleração, empuxo de terra e sobrecarga nas cortinas, componente longitudinal do vento;
- **esforços transversais aplicados no tabuleiro:** vento, força centrífuga (pontes em curva), empuxo nas cortinas de pontes esconsas;
- **deformações impostas ao tabuleiro:** variação de temperatura e retração;
- **ações aplicadas diretamente nos pilares:** empuxo de terra, pressão do vento e pressão da água.

### 1.2 Aparelhos de apoio de elastômero

Nas pontes correntes de concreto, o tabuleiro se apoia nos pilares por **aparelhos de elastômero fretado** (o "neoprene"): camadas de elastômero intercaladas com chapas de aço, especificadas pela NBR 19783 [[2]](#ref-2). Eles transmitem a carga vertical e permitem rotações e deslocamentos horizontais por distorção do elastômero. Sua rigidez horizontal é:

$$
K_n=\frac{G\,A}{\sum t_i} ,
$$

em que $G$ é o módulo de elasticidade transversal do elastômero (da ordem de $1{,}0\text{ MPa}$), $A$ é a área em planta e $\sum t_i$ é a espessura total das camadas de elastômero (sem as chapas).

## 2. Ações horizontais

### 2.1 Frenagem e aceleração

A NBR 7188 [[3]](#ref-3) define a força horizontal de frenagem ou aceleração, aplicada no nível do pavimento e concomitante com a carga vertical, como:

$$
H_f=0{,}25\,B\,L\,CNF\qquad\text{com}\qquad H_f\ge135\text{ kN},
$$

em que $B$ é a largura efetiva da carga distribuída de $5\text{ kN/m}^2$ e $L$ o comprimento concomitante carregado. A força total é distribuída entre os apoios conforme a rigidez (seção 4). Por simplificação, admite-se a força aplicada no eixo do tabuleiro, já que a largura da ponte é pequena em relação ao comprimento [[4]](#ref-4).

```{note}
A antiga NBR 7187:2003 fixava a frenagem em $30\%$ do peso do veículo-tipo e a aceleração em $5\%$ da carga móvel sobre o tabuleiro. Esse critério aparece em muitos livros e memoriais antigos, mas foi substituído pela expressão acima.
```

### 2.2 Vento

A NBR 7187 [[5]](#ref-5) remete o cálculo do vento à NBR 6123 [[6]](#ref-6). A pressão dinâmica é:

$$
q=0{,}613\,V_k^2\ (\text{N/m}^2)
\qquad\qquad
V_k=V_0\,S_1\,S_2\,S_3 ,
$$

com $V_0$ a velocidade básica do local, $S_1$ o fator topográfico, $S_2$ o fator de rugosidade e altura e $S_3$ o fator estatístico. A força é $F = C_a\,q\,A$, sobre a área exposta. Consideram-se duas situações:

- **ponte descarregada:** área exposta da superestrutura (vigas, laje e barreira);
- **ponte carregada:** área da superestrutura acrescida de uma faixa contínua representando os veículos, com cerca de $2{,}0\text{ m}$ de altura acima do pavimento, para pontes rodoviárias.

Para pré-dimensionamento e fins didáticos, ainda se usa o **processo simplificado tradicional** (antiga NB-2), com pressões de $1{,}5\text{ kN/m}^2$ para a ponte descarregada e $1{,}0\text{ kN/m}^2$ para a ponte carregada, aplicadas sobre as áreas acima [[7]](#ref-7). A componente longitudinal do vento costuma ser tomada como $25\%$ da força transversal na superestrutura e $40\%$ da força nos veículos [[7]](#ref-7).

### 2.3 Variação de temperatura

A variação uniforme de temperatura alonga ou encurta o tabuleiro. Pela NBR 6118 [[8]](#ref-8), para elementos com menor dimensão inferior a $50\text{ cm}$, adota-se $\Delta T$ entre $10$ e $15^\circ\text{C}$; neste curso, $\Delta T = \pm15^\circ\text{C}$. O coeficiente de dilatação do concreto é $\alpha = 10^{-5}/^\circ\text{C}$. A variação não uniforme (gradiente térmico), tratada na NBR 7187 [[5]](#ref-5), afeta principalmente a superestrutura.

### 2.4 Retração

A retração encurta o tabuleiro de forma permanente. Nos casos correntes de concreto armado, a NBR 6118 [[8]](#ref-8) permite adotar $\varepsilon_{cs} = -15\times10^{-5}$, o que equivale a uma **queda de temperatura de $15^\circ\text{C}$**. Por ser lenta, a retração é acompanhada da fluência dos pilares, que alivia parte dos esforços. Desprezar esse alívio fica a favor da segurança.

### 2.5 Empuxo de terra

Os empuxos são calculados pela mecânica dos solos. A NBR 7187 [[5]](#ref-5) admite, a favor da segurança, solo sem coesão e sem atrito solo-estrutura, com peso específico de no mínimo $18\text{ kN/m}^3$ e ângulo de atrito de no máximo $30^\circ$. O empuxo passivo só pode ser considerado se sua ocorrência for garantida durante toda a vida útil. Quando a superestrutura funciona como arrimo dos aterros, os empuxos nas duas extremidades só podem ser considerados simultâneos se não houver juntas intermediárias; deve-se verificar também o caso de empuxo em uma só extremidade. Para pilares em taludes de aterro, usa-se uma largura fictícia igual a três vezes a largura do pilar, limitada à largura da plataforma.

Com $\varphi = 30^\circ$, o coeficiente de empuxo ativo é $K_a = \tan^2(45^\circ - \varphi/2) = 0{,}333$.

### 2.6 Água e colisões

Em pilares dentro de cursos d'água, considera-se a pressão da água em movimento, proporcional ao quadrado da velocidade e dependente da forma do pilar (menor para seções circulares). A NBR 7188 [[3]](#ref-3) define ainda cargas de impacto nas barreiras ($100\text{ kN}$ horizontais com $100\text{ kN}$ verticais concomitantes) e ações excepcionais de colisão de veículos contra pilares próximos ao tráfego.

## 3. Rigidez dos apoios

### 3.1 Pilar em balanço

Com o neoprene, o topo do pilar fica livre para girar. O pilar é então um **console engastado na fundação**, com rigidez horizontal:

$$
K_p=\frac{3\,E\,I}{H^3} .
$$

Em pilares biengastados (topo impedido de girar), a rigidez é $12\,E\,I/H^3$ [[4]](#ref-4).

### 3.2 Pilar e neoprene em série

O pilar e o aparelho de apoio trabalham **em série**: a mesma força passa pelos dois, e os deslocamentos se somam:

$$
\frac{1}{K}=\frac{1}{K_p}+\frac{1}{K_n} .
$$

Como $K_n$ costuma ser da mesma ordem de $K_p$, ou menor, o neoprene tem grande influência na rigidez do conjunto e, portanto, na distribuição das forças.

### 3.3 Flexibilidade da fundação: engastamento fictício

O pilar não está engastado de fato no topo da fundação. O solo em volta do tubulão (ou da estaca) é deformável, e o "engaste" ocorre a uma certa profundidade. Para solos cuja rigidez cresce com a profundidade ($E_s = n_h\,z$), Davisson e Robinson [[9]](#ref-9) propõem substituir o trecho enterrado por um engaste fictício à profundidade:

$$
L_e=1{,}8\,T
\qquad\qquad
T=\sqrt[5]{\frac{E\,I_{\mathrm{fund}}}{n_h}} ,
$$

em que $I_{\mathrm{fund}}$ é a inércia do fuste e $n_h$ é o coeficiente de reação horizontal. Valores de referência de Terzaghi [[10]](#ref-10), em $\text{MN/m}^3$:

| Areia | Seca ou úmida | Submersa |
|---|---:|---:|
| Fofa | $2{,}2$ | $1{,}3$ |
| Medianamente compacta | $6{,}6$ | $4{,}4$ |
| Compacta | $17{,}6$ | $10{,}7$ |

Para um pilar de altura $H$ e inércia $I_p$ sobre o trecho fictício $L_e$ de inércia $I_f$, a flexibilidade do topo é:

$$
\delta_1=\frac{H^3}{3\,E\,I_p}+\frac{L_e^3+3\,L_e^2\,H+3\,L_e\,H^2}{3\,E\,I_f}
\qquad\qquad
K_p=\frac{1}{\delta_1} .
$$

A Figura 3.1 resume o modelo.

```{figure} ../_static/aulas/mesoestrutura/meso-modelo-rigidez.png
:alt: Modelo do apoio elástico com pilar, neoprene e engastamento fictício, e distribuição longitudinal
:width: 100%
:align: center

**Figura 3.1** – À esquerda, modelo do apoio elástico: neoprene, pilar e engastamento fictício na fundação. À direita, rigidez dos apoios da ponte-exemplo e posição do ponto indeslocável.
```

## 4. Distribuição das forças horizontais

### 4.1 Direção longitudinal

O tabuleiro é muito rígido na direção do seu eixo. Sob uma força longitudinal $H$, ele se desloca como corpo rígido, e todos os topos de pilar sofrem o mesmo deslocamento $\delta = H/\sum K_i$. Cada pilar recebe uma parcela proporcional à sua rigidez:

$$
H_i=H\,\frac{K_i}{\sum K_j} .
$$

### 4.2 Temperatura e retração: o ponto indeslocável

Sob variação de temperatura ou retração, o tabuleiro se alonga ou se encurta em torno de um ponto que não se desloca, o **centro de rigidez longitudinal**:

$$
x_0=\frac{\sum K_i\,x_i}{\sum K_i} .
$$

O topo do pilar $i$ sofre o deslocamento imposto $\delta_i = \alpha\,\Delta T\,(x_i - x_0)$, e a força no pilar é:

$$
H_i=K_i\,\alpha\,\Delta T\,(x_i-x_0) .
$$

Essas forças são **autoequilibradas** ($\sum H_i = 0$): os pilares de um lado do ponto indeslocável são puxados num sentido, os do outro lado no sentido contrário [[4]](#ref-4).

### 4.3 Direção transversal

Devido à grande rigidez que a laje confere ao tabuleiro no plano horizontal, ele pode ser considerado uma placa rígida sobre apoios elásticos [[4]](#ref-4). Se a resultante das forças transversais passa pelo centro de rigidez, o tabuleiro apenas se translada e cada apoio recebe uma parcela proporcional à sua rigidez transversal. Se há uma excentricidade $e$, o tabuleiro também gira de um ângulo $\theta$, e cada pilar, à distância $x_i$ do centro de rigidez, recebe a força adicional $K_i\,\theta\,x_i$:

$$
H_i=H\,\frac{K_i}{\sum K_j}+H\,e\,\frac{K_i\,x_i}{\sum K_j\,x_j^2} .
$$

Quando existem vigas transversais ligando os pilares de uma mesma linha (pórticos), a rigidez transversal de cada linha é a do pórtico, obtida como o inverso do deslocamento do topo sob força unitária [[4]](#ref-4).

## 5. Exemplo resolvido: forças horizontais nos pilares da ponte-exemplo

```{admonition} Dados
:class: destaque-azul

Ponte-exemplo das Aulas 05 e 06 (dados hipotéticos):

- comprimento total $28{,}00\text{ m}$ (balanços de $4{,}00\text{ m}$ e vão de $20{,}00\text{ m}$), pista de $8{,}60\text{ m}$, duas faixas;
- linhas de apoio P1 ($x = 4{,}00\text{ m}$) e P2 ($x = 24{,}00\text{ m}$), cada uma com dois pilares circulares de $\text{Ø}\,1{,}20\text{ m}$, um sob cada longarina; alturas de $6{,}00\text{ m}$ (P1) e $7{,}00\text{ m}$ (P2) acima do terreno;
- tubulões com fuste de $\text{Ø}\,1{,}40\text{ m}$ em areia compacta ($n_h = 17{,}6\text{ MN/m}^3$);
- um neoprene por longarina: $40 \times 50\text{ cm}$, $\sum t_i = 50\text{ mm}$, $G = 1{,}0\text{ MPa}$;
- $E = E_{cs} = 26{,}84\text{ GPa}$ (C30); superestrutura com $1{,}80\text{ m}$ de altura e barreira de $0{,}87\text{ m}$.
```

### 5.1 Rigidez dos apoios

$$
I_p=\frac{\pi\,1{,}20^4}{64}=0{,}1018\text{ m}^4
\qquad
I_f=\frac{\pi\,1{,}40^4}{64}=0{,}1886\text{ m}^4
$$

$$
T=\sqrt[5]{\frac{26{,}84\times10^6\cdot0{,}1886}{17\,600}}=3{,}10\text{ m}
\qquad
L_e=1{,}8\cdot3{,}10=5{,}58\text{ m}
$$

$$
K_n=\frac{1\,000\cdot0{,}40\cdot0{,}50}{0{,}050}=4\,000\text{ kN/m}
$$

| Apoio | $H$ (m) | $K_p$ com engaste fictício | $K_p$ com engaste no terreno | $K$ (pilar + neoprene) |
|---|---:|---:|---:|---:|
| P1 | $6{,}00$ | $8\,731$ | $37\,944$ | $2\,743$ |
| P2 | $7{,}00$ | $6\,643$ | $23\,895$ | $2\,497$ |

Valores em kN/m, por pilar. Considerar a fundação engastada no nível do terreno multiplicaria a rigidez do pilar por $3{,}6$ a $4{,}3$. Já o neoprene reduz a rigidez do conjunto a menos da metade da do pilar sozinho.

$$
\sum K=2\cdot(2\,743+2\,497)=10\,480\text{ kN/m}
$$

### 5.2 Frenagem

$$
H_f=\max\{0{,}25\cdot8{,}60\cdot28{,}00\cdot1{,}00;\ 135\}=\max\{60{,}2;\ 135\}=135\text{ kN}
$$

$$
H_{P1}=135\cdot\frac{2\,743}{10\,480}=35{,}3\text{ kN}
\qquad\qquad
H_{P2}=135\cdot\frac{2\,497}{10\,480}=32{,}2\text{ kN}
\qquad\text{(por pilar)}
$$

Para esta ponte curta, o mínimo de $135\text{ kN}$ governa.

### 5.3 Temperatura e retração

$$
x_0=\frac{2\cdot2\,743\cdot4{,}00+2\cdot2\,497\cdot24{,}00}{10\,480}=13{,}53\text{ m}
$$

| Pilar | $x_i - x_0$ (m) | $\delta_i = 10^{-5}\cdot15\cdot\lvert x_i-x_0\rvert$ (mm) | $H_i = K_i\,\delta_i$ (kN) |
|---|---:|---:|---:|
| P1 | $-9{,}53$ | $1{,}43$ | $3{,}92$ |
| P2 | $+10{,}47$ | $1{,}57$ | $3{,}92$ |

As forças são iguais e opostas, como esperado num sistema com duas linhas de apoio. A retração ($-15^\circ\text{C}$ equivalentes) produz as mesmas forças, com sentido de encurtamento e caráter permanente.

### 5.4 Vento transversal

Pelo processo simplificado:

$$
w_{\mathrm{desc}}=1{,}5\cdot(1{,}80+0{,}87)=4{,}00\text{ kN/m}
\qquad
w_{\mathrm{carr}}=1{,}0\cdot(1{,}80+2{,}00)=3{,}80\text{ kN/m}
$$

$$
W=4{,}00\cdot28{,}00=112{,}1\text{ kN},\ \text{aplicada em } x=14{,}00\text{ m}
$$

A resultante tem excentricidade $e = 14{,}00 - 13{,}53 = 0{,}47\text{ m}$ em relação ao centro de rigidez. Admitindo rigidez transversal igual à longitudinal (pilar circular e neoprene de planta quase quadrada):

$$
\sum K_i\,x_i^2=2\cdot2\,743\cdot9{,}53^2+2\cdot2\,497\cdot10{,}47^2=1{,}046\times10^6\text{ kN·m}
$$

| Pilar | Translação | Rotação | Total (por pilar) |
|---|---:|---:|---:|
| P1 | $29{,}35$ | $-1{,}32$ | $28{,}0\text{ kN}$ |
| P2 | $26{,}72$ | $+1{,}32$ | $28{,}0\text{ kN}$ |

### 5.5 Resumo das forças no topo de cada pilar

| Ação (característica) | P1 | P2 | Direção |
|---|---:|---:|---|
| Frenagem | $35{,}3$ | $32{,}2$ | longitudinal |
| Temperatura ($\pm15^\circ\text{C}$) | $3{,}9$ | $3{,}9$ | longitudinal |
| Retração | $3{,}9$ | $3{,}9$ | longitudinal (permanente) |
| Vento | $28{,}0$ | $28{,}0$ | transversal |

Valores em kN. Essas forças, com as cargas verticais, alimentam o dimensionamento dos pilares (Aula 08) e dos tubulões (Aula 09).

## 6. Roteiro

```{admonition} Roteiro da mesoestrutura
:class: destaque-verde

1. Definir o modelo de cada apoio: pilar em balanço, aparelho de apoio em série e engastamento fictício na fundação.
2. Calcular as rigidezes $K_i$ nas direções longitudinal e transversal.
3. Calcular as ações horizontais: frenagem, vento, temperatura, retração, empuxos e, se houver, água.
4. Distribuir as forças longitudinais proporcionalmente a $K_i$ e as deformações impostas a partir do ponto indeslocável.
5. Distribuir as forças transversais considerando translação e rotação do tabuleiro.
6. Montar, para cada pilar, as forças no topo para as combinações da Aula 08.
```

## Referências

(ref-1)=
**[1]** TAGUTI. *Pontes de concreto armado*. Notas de aula, 2002 (*apud* material didático da disciplina).

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 19783**: *Aparelhos de apoio de elastômero fretado — Especificação e métodos de ensaio*. Rio de Janeiro: ABNT, 2015.

(ref-3)=
**[3]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7188**: *Ações devido ao tráfego de veículos rodoviários e de pedestres em pontes, viadutos e passarelas*. Rio de Janeiro: ABNT, 2024.

(ref-4)=
**[4]** ARAÚJO, D. de L. *Projeto de ponte em concreto armado com duas longarinas*. 2. ed. Goiânia: UFG, 2018.

(ref-5)=
**[5]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7187**: *Projeto de pontes, viadutos e passarelas de concreto*. Rio de Janeiro: ABNT, 2021.

(ref-6)=
**[6]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6123**: *Forças devidas ao vento em edificações*. Rio de Janeiro: ABNT, 2023.

(ref-7)=
**[7]** MARCHETTI, O. *Pontes de concreto armado*. 2. ed. São Paulo: Blucher, 2018.

(ref-8)=
**[8]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: *Projeto de estruturas de concreto*. Rio de Janeiro: ABNT, 2023 (Emenda 1: 2026).

(ref-9)=
**[9]** DAVISSON, M. T.; ROBINSON, K. E. Bending and buckling of partially embedded piles. In: INTERNATIONAL CONFERENCE ON SOIL MECHANICS AND FOUNDATION ENGINEERING, 6., 1965, Montreal. *Proceedings*... 1965.

(ref-10)=
**[10]** TERZAGHI, K. Evaluation of coefficients of subgrade reaction. *Géotechnique*, v. 5, n. 4, p. 297-326, 1955.
