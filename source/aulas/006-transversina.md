# Aula 06: Transversinas — ações, esforços e dimensionamento

```{admonition} Onde estamos?
:class: destaque-azul

1. Conceitos gerais sobre o projeto de pontes
2. Ações na superestrutura
3. Análise computacional com carga móvel
4. Dimensionamento da longarina
5. Dimensionamento do tabuleiro
6. **Dimensionamento da transversina (esta aula)**
7. Mesoestrutura: ações horizontais e distribuição entre os apoios
8. Dimensionamento dos pilares
9. Fundações em tubulão

Esta aula trata das vigas transversais que ligam as longarinas: suas funções, as cargas permanentes vindas da laje, a montagem do trem-tipo da transversina, a operação de macaqueamento e o dimensionamento.
```

## 1. Funções das transversinas

Nas pontes de duas longarinas, as transversinas servem de apoio para a laje do tabuleiro, quando estão ligadas a ela, e contribuem para a rigidez do conjunto sob cargas excêntricas. As transversinas sobre os apoios têm ainda a função de impedir o tombamento lateral das longarinas e de absorver excentricidades dos apoios em relação aos eixos das vigas [[1]](#ref-1). Em resumo, as transversinas:

- **travam as longarinas**, impedindo a distorção da seção transversal e o tombamento durante a construção;
- **distribuem as cargas** entre as longarinas, colaborando com a laje na repartição transversal da carga móvel;
- **apoiam a laje**, recebendo parte das cargas do tabuleiro;
- **servem de ponto de apoio para o macaqueamento**, a elevação do tabuleiro para a inspeção ou a substituição dos aparelhos de apoio, que a NBR 7187 [[2]](#ref-2) exige prever no projeto.

Distinguem-se dois tipos:

- **transversina de vão** (ou intermediária), entre os apoios, solicitada principalmente pela carga móvel;
- **transversina de apoio**, sobre os pilares, solicitada também pelas forças de macaqueamento.

## 2. Modelo estrutural

A transversina é modelada como uma **viga biapoiada nas longarinas**, com vão teórico igual à distância entre os eixos das longarinas. Quando a transversina é ligada à laje, a seção é **T**, com a laje atuando como mesa colaborante. Esse modelo considera as longarinas como apoios indeslocáveis, o que é adequado para o cálculo local da peça. A distribuição global da carga entre as longarinas foi tratada na determinação do trem-tipo da longarina.

## 3. Cargas permanentes

### 3.1 Área de influência

Taguti [[3]](#ref-3) avalia as cargas da laje sobre a transversina pela **área de influência** obtida com as bissetrizes dos cantos dos painéis (Figura 3.1). A transversina é tratada como viga biapoiada nas longarinas, sem consideração da largura colaborante da laje. As cargas são as mesmas usadas na longarina:

- peso próprio da laje;
- pavimento e recapeamento;
- peso próprio da transversina.

```{figure} ../_static/aulas/transversina/tra-areas-trem-tipo.png
:alt: Área de influência por bissetrizes e linha de influência longitudinal da reação na transversina
:width: 100%
:align: center

**Figura 3.1** – À esquerda, área de influência da transversina de vão pelo processo das bissetrizes (dois painéis de $5{,}00 \times 10{,}00\text{ m}$). À direita, linha de influência longitudinal da reação na transversina, usada para montar o trem-tipo.
```

### 3.2 Carga equivalente

Para painéis de $\ell_x \times \ell_y$ com $\ell_y \ge \ell_x$, cada painel transfere à transversina um triângulo de base $\ell_x$ e altura $\ell_x/2$. A carga linear tem forma triangular, com pico no meio do vão da transversina:

$$
q_0=n_p\,g\,\frac{\ell_x}{2},
$$

em que $n_p$ é o número de painéis que descarregam na transversina (dois, para a transversina de vão; um, para a de apoio com balanço longitudinal sem laje). Os esforços na viga biapoiada são:

$$
M_g=\frac{g_{pp}\,\ell^2}{8}+\frac{q_0\,\ell^2}{12}
\qquad\qquad
V_g=\frac{g_{pp}\,\ell}{2}+\frac{q_0\,\ell}{4} .
$$

## 4. Trem-tipo da transversina

### 4.1 Ideia

A carga móvel chega à transversina através da laje. Marchetti [[4]](#ref-4) monta o **trem-tipo da transversina** posicionando o eixo central do veículo sobre a transversina e distribuindo as cargas dos eixos até as transversinas (ou cortinas) vizinhas, a uma distância $L_{t}$. Em outras palavras, usa-se a **linha de influência longitudinal da reação na transversina**, admitindo a laje simplesmente apoiada entre transversinas:

$$
\eta(y)=1-\frac{|y|}{L_t}\qquad(|y|\le L_t).
$$

### 4.2 Cargas do trem-tipo

**Carga por roda** (alinhamento de três rodas, com o eixo central sobre a transversina):

$$
P_t=P\left[1+2\left(1-\frac{1{,}50}{L_t}\right)\right].
$$

**Multidão.** Fora da faixa transversal ocupada pelo veículo, a multidão atua em todo o comprimento de influência. Dentro dessa faixa, só atua fora dos $6{,}00\text{ m}$ do veículo:

$$
q_{t,\mathrm{fora}}=p\int\eta\,dy=p\,L_t
\qquad\qquad
q_{t,\mathrm{sob}}=p\left(L_t-\int_{-3}^{3}\eta\,dy\right).
$$

**Coeficiente dinâmico.** Como na laje, a transversina é um elemento transversal ao tráfego: $\varphi = CIV\cdot CIA$, sem o CNF [[5]](#ref-5).

### 4.3 Posição mais desfavorável na transversina

O trem-tipo transversal tem duas cargas $P_t$ afastadas de $e = 2{,}00\text{ m}$, mais a multidão. Para duas cargas iguais numa viga biapoiada de vão $\ell$, o momento máximo **não** ocorre com as cargas simétricas em relação ao meio do vão. Pelo **teorema de Barré**, ele ocorre sob uma das cargas quando o meio do vão divide ao meio a distância entre essa carga e a resultante:

$$
M_{\max}=\frac{P\,(\ell-e/2)^2}{2\,\ell}
\qquad\text{(Barré)}
\qquad\qquad
M_{\mathrm{sim}}=\frac{P\,(\ell-e)}{2}
\qquad\text{(cargas simétricas)} .
$$

Para $\ell = 5{,}00\text{ m}$ e $e = 2{,}00\text{ m}$: $M_{\max} = 1{,}60\,P$ e $M_{\mathrm{sim}} = 1{,}50\,P$. O cortante máximo ocorre com uma das cargas sobre o apoio.

```{warning}
Considerar apenas o eixo que está sobre a transversina, sem os eixos vizinhos, desconsidera a parcela que a laje leva até ela. Com $L_t = 10{,}00\text{ m}$, os dois eixos vizinhos acrescentam $2 \cdot 0{,}85 = 1{,}70$ vez a carga do eixo central. O modelo do trem-tipo da transversina é conservador, porque admite a laje apoiada só nas transversinas. Um modelo de grelha ou de elementos finitos fornece valores intermediários.
```

## 5. Transversina de apoio e macaqueamento

Na operação de macaqueamento, o tráfego é interrompido e o tabuleiro é erguido por macacos apoiados no topo dos pilares, sob a transversina de apoio. A força por macaco é:

$$
F_{\mathrm{mac},d}=\frac{\gamma_g\,R_{g,k}}{n_{\mathrm{mac}}} ,
$$

em que $R_{g,k}$ é a reação permanente característica da linha de apoio e $n_{\mathrm{mac}}$ o número de macacos. A transversina passa a funcionar como viga apoiada nos macacos e carregada pelas reações das longarinas:

- com os macacos **alinhados com as longarinas**, a transferência é quase direta. O dimensionamento é governado pelo cisalhamento, pela armadura de suspensão e pela pressão de contato sob os macacos;
- com uma **excentricidade** $e_m$ entre macaco e longarina, a transversina trabalha como um balanço curto sobre o macaco e surge o momento negativo (tração na face superior) $M_d = -F_{\mathrm{mac},d}\,e_m$.

## 6. Dimensionamento

**Flexão.** Seção T (laje como mesa) ou retangular. Para viga biapoiada, a largura colaborante de cada lado da alma é $b_1 \le 0{,}10\,a$, com $a = \ell$ [[6]](#ref-6).

**Cisalhamento** (modelo de cálculo I da NBR 6118 [[6]](#ref-6)):

$$
V_{Rd2}=0{,}27\,\alpha_{v2}\,f_{cd}\,b_w\,d
\qquad
\alpha_{v2}=1-\frac{f_{ck}}{250}
\qquad
V_c=0{,}6\,f_{ctd}\,b_w\,d
\qquad
\frac{A_{sw}}{s}=\frac{V_{sd}-V_c}{0{,}9\,d\,f_{ywd}} ,
$$

com $V_{sd} \le V_{Rd2}$ e $(A_{sw}/s)_{\min} = 0{,}2\,(f_{ctm}/f_{ywk})\,b_w$.

**Armadura de pele.** Para alturas superiores a $60\text{ cm}$, $A_{s,\mathrm{pele}} = 0{,}10\%\,A_{c,\mathrm{alma}}$ em cada face, com espaçamento não superior a $20\text{ cm}$ e a $d/3$.

**Torção de compatibilidade.** A rotação das longarinas impõe torção à transversina. Por ser de compatibilidade, ela pode ser desprezada nos esforços de cálculo, desde que se use armadura mínima de torção e se controle a fissuração (estribos fechados e armadura longitudinal distribuída no perímetro) [[6]](#ref-6).

## 7. Exemplo resolvido: transversina de vão da ponte-exemplo

```{admonition} Dados
:class: destaque-azul

Mesma ponte-exemplo da Aula 05 (dados hipotéticos):

- vão da transversina $\ell = 5{,}00\text{ m}$ (eixos das longarinas); transversinas a $L_t = 10{,}00\text{ m}$;
- seção $b_w = 30\text{ cm}$ e $h = 150\text{ cm}$ (incluindo a laje de $22\text{ cm}$);
- carga permanente da laje $g = 9{,}42\text{ kN/m}^2$ (Aula 05);
- C30, CA-50, cobrimento $4\text{ cm}$, $\gamma_g = 1{,}35$ e $\gamma_q = 1{,}50$; $\varphi = 1{,}35\cdot1{,}25 = 1{,}6875$.
```

### 7.1 Cargas permanentes

$$
g_{pp}=25\cdot0{,}30\cdot(1{,}50-0{,}22)=9{,}60\text{ kN/m}
\qquad
q_0=2\cdot9{,}42\cdot\frac{5{,}00}{2}=47{,}10\text{ kN/m}
$$

$$
M_g=\frac{9{,}60\cdot5{,}00^2}{8}+\frac{47{,}10\cdot5{,}00^2}{12}=30{,}00+98{,}13=128{,}1\text{ kN·m}
$$

$$
V_g=\frac{9{,}60\cdot5{,}00}{2}+\frac{47{,}10\cdot5{,}00}{4}=24{,}00+58{,}88=82{,}9\text{ kN}
$$

### 7.2 Trem-tipo da transversina

$$
\sum\eta=1+2\left(1-\frac{1{,}50}{10{,}00}\right)=2{,}70
\qquad\Rightarrow\qquad
P_t=75\cdot2{,}70=202{,}5\text{ kN por roda}
$$

$$
q_{t,\mathrm{fora}}=5\cdot10{,}00=50{,}0\text{ kN/m}
\qquad
\int_{-3}^{3}\eta\,dy=2\cdot3{,}00\cdot\frac{1{,}00+0{,}70}{2}=5{,}10\text{ m}
\qquad
q_{t,\mathrm{sob}}=5\cdot(10{,}00-5{,}10)=24{,}5\text{ kN/m}
$$

O trem-tipo da transversina tem, portanto, duas cargas de $202{,}5\text{ kN}$ a $2{,}00\text{ m}$, com $24{,}5\text{ kN/m}$ na faixa de $3{,}00\text{ m}$ do veículo e $50{,}0\text{ kN/m}$ fora dela (valores sem $\varphi$).

### 7.3 Esforços da carga móvel

Deslocando o trem-tipo ao longo da transversina, o momento máximo ocorre com as rodas em $x = 2{,}15\text{ m}$ e $x = 4{,}15\text{ m}$, na seção $x = 2{,}15\text{ m}$ (posição próxima da de Barré, ajustada pela multidão):

$$
M_q=322{,}2\ (\text{rodas})+95{,}5\ (\text{multidão})=417{,}7\text{ kN·m}
\qquad
M_{q,\varphi}=1{,}6875\cdot417{,}7=704{,}9\text{ kN·m}
$$

O cortante máximo ocorre com uma roda sobre o apoio:

$$
V_q=202{,}5\left(1+\frac{3{,}00}{5{,}00}\right)+77{,}2=324{,}0+77{,}2=401{,}2\text{ kN}
\qquad
V_{q,\varphi}=677{,}0\text{ kN}
$$

### 7.4 Esforços de cálculo

$$
M_d=1{,}35\cdot128{,}1+1{,}50\cdot704{,}9=1\,230\text{ kN·m}
\qquad
V_d=1{,}35\cdot82{,}9+1{,}50\cdot677{,}0=1\,127\text{ kN}
$$

```{note}
Se apenas o eixo sobre a transversina fosse considerado, com as rodas simétricas, $M_{q,\varphi} = 75\cdot1{,}6875\cdot(5{,}00-2{,}00)/2 = 189{,}8\text{ kN·m}$, cerca de um quarto do valor acima. A diferença mostra quanto o modelo adotado para a transferência da carga pela laje pesa no resultado.
```

### 7.5 Armaduras

**Flexão.** Seção T com $b_f = 0{,}30 + 2\cdot0{,}10\cdot5{,}00 = 1{,}30\text{ m}$ e $d = 1{,}43\text{ m}$:

$$
x=1{,}25\cdot1{,}427\left[1-\sqrt{1-\frac{1\,230}{0{,}425\cdot1{,}30\cdot1{,}427^2\cdot21\,430}}\right]=0{,}046\text{ m}<h_f=0{,}22\text{ m}
$$

A linha neutra fica na mesa, e a seção trabalha como retangular de largura $b_f$:

$$
A_s=\frac{1\,230}{43{,}5\cdot(1{,}427-0{,}4\cdot0{,}046)}\approx20{,}1\text{ cm}^2
\quad\Rightarrow\quad 5\,\text{Ø}\,25\ (24{,}5\text{ cm}^2)\ \text{em duas camadas}
\qquad(A_{s,\min}=0{,}15\%\,b_w\,h=6{,}75\text{ cm}^2)
$$

**Cisalhamento.**

$$
V_{Rd2}=0{,}27\cdot0{,}88\cdot21\,430\cdot0{,}30\cdot1{,}427=2\,180\text{ kN}>V_d=1\,127\text{ kN}
$$

$$
V_c=0{,}6\cdot1\,448\cdot0{,}30\cdot1{,}427=372\text{ kN}
\qquad
\frac{A_{sw}}{s}=\frac{1\,127-372}{0{,}9\cdot1{,}427\cdot435\,000}\cdot10^4=13{,}5\text{ cm}^2/\text{m}
$$

Adotam-se estribos Ø10 de dois ramos a cada $11\text{ cm}$ ($14{,}3\text{ cm}^2/\text{m}$), acima do mínimo de $3{,}48\text{ cm}^2/\text{m}$.

**Armadura de pele.** $0{,}10\%\cdot0{,}30\cdot1{,}28 = 3{,}84\text{ cm}^2$ por face, por exemplo 8 Ø8 por face ($4{,}0\text{ cm}^2$), com espaçamento menor que $20\text{ cm}$.

### 7.6 Transversina de apoio: macaqueamento

Com $R_{g,k} = 900\text{ kN}$ por longarina, dois macacos por longarina e excentricidade de $0{,}60\text{ m}$ entre macaco e eixo da longarina:

$$
F_{\mathrm{mac},d}=\frac{1{,}35\cdot900}{2}=607{,}5\text{ kN}
\qquad\qquad
M_d=-607{,}5\cdot0{,}60=-364{,}5\text{ kN·m}
$$

A transversina de apoio é então dimensionada para esse momento, para o cortante correspondente e para a pressão localizada sob os macacos.

## 8. Roteiro

```{admonition} Roteiro do dimensionamento da transversina
:class: destaque-verde

1. Definir a geometria, o vão (eixos das longarinas) e a largura colaborante.
2. Calcular as cargas permanentes pela área de influência e o peso próprio.
3. Montar o trem-tipo da transversina com a LI longitudinal da reação ($P_t$, $q_{t,\mathrm{fora}}$, $q_{t,\mathrm{sob}}$) e aplicar $\varphi = CIV\cdot CIA$.
4. Posicionar o trem-tipo para o momento máximo (Barré) e para o cortante máximo (roda no apoio).
5. Na transversina de apoio, verificar o macaqueamento.
6. Dimensionar a flexão, o cisalhamento ($V_{sd}\le V_{Rd2}$ e estribos), a armadura de pele e a armadura mínima de torção.
```

## Referências

(ref-1)=
**[1]** ARAÚJO, D. de L. *Projeto de ponte em concreto armado com duas longarinas*. 2. ed. Goiânia: UFG, 2018.

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7187**: *Projeto de pontes, viadutos e passarelas de concreto*. Rio de Janeiro: ABNT, 2021.

(ref-3)=
**[3]** TAGUTI. *Pontes de concreto armado*. Notas de aula, 2002 (*apud* material didático da disciplina).

(ref-4)=
**[4]** MARCHETTI, O. *Pontes de concreto armado*. 2. ed. São Paulo: Blucher, 2018.

(ref-5)=
**[5]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7188**: *Ações devido ao tráfego de veículos rodoviários e de pedestres em pontes, viadutos e passarelas*. Rio de Janeiro: ABNT, 2024.

(ref-6)=
**[6]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: *Projeto de estruturas de concreto*. Rio de Janeiro: ABNT, 2023 (Emenda 1: 2026).
