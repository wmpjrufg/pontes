# Aula 05: Tabuleiro — esforços nas lajes de pontes

```{admonition} Onde estamos?
:class: destaque-azul

O curso está organizado em torno das seguintes etapas de projeto:

1. Conceitos gerais sobre o projeto de pontes
2. Ações na superestrutura
3. Análise computacional com carga móvel
4. Dimensionamento da longarina
5. **Dimensionamento do tabuleiro (esta aula)**
6. Dimensionamento da transversina
7. Mesoestrutura: ações horizontais e distribuição entre os apoios
8. Dimensionamento dos pilares
9. Fundações em tubulão

Esta aula mostra como obter os esforços nas lajes do tabuleiro: a laje central, entre as longarinas, e a laje em balanço, no bordo. Ao final, os momentos das duas lajes são compatibilizados no apoio comum e a armadura é dimensionada.
```

## 1. O tabuleiro da ponte

### 1.1 Estruturas de superfície

Stucchi [[1]](#ref-1) classifica como **estruturas de superfície** os elementos que têm uma dimensão, a **espessura**, muito menor que as outras duas. A **superfície média** é o lugar geométrico dos pontos a meia espessura. Conforme a forma da superfície média e a direção do carregamento, distinguem-se:

- **placa:** superfície média plana carregada perpendicularmente a ela. As placas de concreto armado são as **lajes**;
- **chapa:** superfície média plana carregada paralelamente a ela. As chapas de concreto armado são as **vigas-parede**;
- **casca:** superfície média curva.

O tabuleiro das pontes de concreto é formado por lajes ligadas de diversas maneiras aos demais elementos da superestrutura. Os elementos que servem de apoio às lajes são as longarinas, as transversinas e as vigas de fechamento (cortinas). Por isso, as dimensões e as condições de apoio das lajes dependem da distribuição desses elementos. Nas pontes de duas longarinas, uma dimensão da laje costuma ser bem maior que a outra, e as condições de apoio podem ser de apoio simples, engaste parcial ou balanço [[2]](#ref-2).

### 1.2 As duas lajes de uma ponte de duas longarinas

Numa ponte de duas longarinas, o tabuleiro se divide em duas regiões que se comportam de modo muito diferente (Figura 1.1):

- **Laje central (L1):** painel entre as longarinas, limitado longitudinalmente pelas transversinas. É uma placa apoiada nos quatro lados, com continuidade nas longarinas (com os balanços) e nas transversinas (com os painéis vizinhos).
- **Laje em balanço (L2):** trecho que se projeta além da longarina até o bordo do tabuleiro, onde fica a barreira. É uma placa engastada na longarina e livre no bordo.

```{figure} ../_static/aulas/tabuleiro/tab-planta-lajes.png
:alt: Planta do tabuleiro da ponte-exemplo com a laje central e as lajes em balanço
:width: 100%
:align: center

**Figura 1.1** – Planta do tabuleiro da ponte-exemplo desta aula: laje central L1 ($\ell_x \times \ell_y = 5{,}00 \times 10{,}00\text{ m}$) e lajes em balanço L2 nos bordos.
```

A estratégia clássica, adotada nesta aula, é calcular **cada laje isoladamente**, com condições de contorno idealizadas (engaste nos apoios contínuos), e depois **compatibilizar** os momentos negativos no apoio comum, corrigindo os momentos positivos.

### 1.3 Métodos de cálculo

Segundo Araújo [[2]](#ref-2), os esforços nas lajes de ponte podem ser obtidos por:

- **métodos elásticos**, baseados na teoria das placas e no conceito de **superfície de influência**. As tabelas de Rüsch [[3]](#ref-3) são o exemplo clássico;
- **métodos de ruptura**, baseados nas linhas de ruptura (charneiras plásticas), que fornecem os momentos a partir do equilíbrio de um mecanismo de colapso;
- **métodos numéricos**, como o método dos elementos finitos ou a analogia de grelha, que fornecem uma visão mais completa do comportamento do tabuleiro.

Esta aula usa o método elástico. Ele é o que melhor se conecta com o que já foi visto para a longarina: a superfície de influência é a extensão, para a placa, da linha de influência da viga.

## 2. Superfície de influência

### 2.1 Definição

A **superfície de influência** de um esforço $S$ num ponto da laje é a função $\eta(x,y)$ que fornece o valor de $S$ quando uma carga unitária vertical é aplicada no ponto $(x,y)$. É exatamente o conceito de linha de influência, agora em duas dimensões.

Com a superfície conhecida, o esforço produzido por um conjunto de cargas concentradas $P_i$ e de cargas distribuídas $p$ é obtido por superposição:

$$
S=\sum_i P_i\,\eta_i+\sum_j p_j\iint_{A_j}\eta(x,y)\,dA ,
$$

em que $\eta_i$ é a ordenada no ponto de aplicação de cada carga concentrada e $A_j$ é a região carregada por cada carga distribuída [[2]](#ref-2). Assim como na viga, a carga distribuída só é colocada nas regiões em que $\eta$ tem o sinal do esforço procurado.

A Figura 2.1 mostra as superfícies de influência do momento $m_x$ no centro e no bordo engastado da laje central da ponte-exemplo, com o veículo TB-450 nas posições mais desfavoráveis encontradas no exemplo da seção 7.

```{figure} ../_static/aulas/tabuleiro/tab-superficies-influencia.png
:alt: Superfícies de influência do momento mx no centro e no engaste da laje central
:width: 100%
:align: center

**Figura 2.1** – Superfícies de influência de $m_x$ na laje central ($\ell_x = 5{,}00\text{ m}$, $\ell_y = 10{,}00\text{ m}$, engastada nas longarinas e apoiada nas transversinas). Os retângulos laranja são as áreas de contato das rodas do TB-450 distribuídas até a superfície média; o tracejado é o contorno do veículo ($3{,}00 \times 6{,}00\text{ m}$).
```

Duas observações importantes:

1. A superfície de influência de momento tem uma **singularidade** (cresce sem limite) no próprio ponto analisado. Por isso a carga da roda não pode ser tratada como pontual: ela é espalhada numa área e o esforço é calculado com a **ordenada média** da superfície nessa área.
2. A superfície do momento no engaste é **toda negativa** e concentrada perto do bordo. As rodas mais próximas da longarina dominam o resultado.

### 2.2 Área de distribuição da carga da roda

Admite-se que a carga da roda se espalha a $45^\circ$ através do pavimento e da laje até a superfície média [[2]](#ref-2). Para a roda do TB-450, com área de contato de $0{,}20\text{ m}$ (direção do tráfego) por $0{,}50\text{ m}$ (direção transversal), as dimensões na superfície média são:

$$
b_1=0{,}20+2\,e_{\mathrm{asf}}+h
\qquad\qquad
b_2=0{,}50+2\,e_{\mathrm{asf}}+h ,
$$

em que $e_{\mathrm{asf}}$ é a espessura do pavimento e $h$ a espessura da laje. As tabelas de Rüsch trabalham com uma área quadrada equivalente de lado $t$:

$$
t'=\sqrt{0{,}20\cdot0{,}50}=0{,}316\text{ m}
\qquad\qquad
t=t'+2\,e_{\mathrm{asf}}+h .
$$

## 3. Ações no tabuleiro

### 3.1 Ações permanentes

As cargas nas lajes são expressas por unidade de área ($\text{kN/m}^2$):

$$
g_1=\gamma_c\,h
\qquad\qquad
g_2=\gamma_{\mathrm{asf}}\,e_{\mathrm{asf}}+2{,}0 ,
$$

com $\gamma_c = 25\text{ kN/m}^3$, $\gamma_{\mathrm{asf}} = 24\text{ kN/m}^3$ e $2{,}0\text{ kN/m}^2$ de reserva para recapeamento [[4]](#ref-4). No balanço entram ainda as cargas lineares da barreira e do guarda-corpo.

### 3.2 Ação variável e coeficientes dinâmicos

A carga móvel é o TB-450 da NBR 7188 [[5]](#ref-5): rodas de $P = 75\text{ kN}$, eixos a $1{,}50\text{ m}$, rodas de um mesmo eixo a $2{,}00\text{ m}$ e multidão $p = 5\text{ kN/m}^2$ em volta do veículo.

Nas lajes e transversinas, que são elementos transversais ao tráfego, **não se aplica o CNF** [[5]](#ref-5). O coeficiente dinâmico é:

$$
\varphi=CIV\cdot CIA .
$$

Para a laje, o vão de referência é o próprio vão da laje. Como ele é inferior a $10\text{ m}$, $CIV = 1{,}35$; com $CIA = 1{,}25$ (concreto), $\varphi = 1{,}6875$.

```{note}
A NBR 7188 [[5]](#ref-5) prevê o CIA para as seções situadas a menos de $5\text{ m}$ de juntas e descontinuidades estruturais. Neste curso, como nos parâmetros do trabalho prático, o CIA é aplicado em todo o tabuleiro, o que fica a favor da segurança.
```

## 4. Tabelas de Rüsch

### 4.1 O que são

As tabelas de Rüsch [[3]](#ref-3) fornecem os momentos fletores em lajes retangulares de ponte, para condições de apoio prefixadas (apoio simples, engaste perfeito ou bordo livre), devidos às cargas das rodas de um veículo-tipo e à carga distribuída em volta dele. Elas foram obtidas exatamente pelo processo da seção 2: cada coeficiente é uma integral da superfície de influência sobre a área carregada. A carga móvel das tabelas é a da antiga norma alemã DIN 1072, cuja geometria é compatível com a do TB-450 (rodas a $2{,}00\text{ m}$ e eixos a $1{,}50\text{ m}$).

### 4.2 Roteiro de leitura

1. **Identificar a vinculação** da laje (apoiada, engastada ou livre em cada bordo), conforme os símbolos da tabela.
2. **Identificar a direção do tráfego** (*Fahrtrichtung*) em relação aos bordos.
3. Calcular $\ell_y/\ell_x$ para escolher a tabela.
4. Calcular os parâmetros de entrada $\ell_x/a$ e $t/a$, com $a = 2{,}00\text{ m}$ (distância entre rodas de um eixo) e $t$ conforme a seção 2.2.
5. Ler os coeficientes:
   - $k$ para a carga permanente, na parte superior da tabela (*Gleichlast über die ganze Platte*, carga uniforme sobre toda a placa);
   - $M_L$ para as rodas e $M_p$, $M_{p'}$ para as cargas distribuídas, interpolando linearmente quando necessário. Atenção à posição da vírgula na tabela.
6. Calcular os momentos:

$$
M_g=k\,g\,\ell_x^2
\qquad\qquad
M_q=\varphi\left(P\,M_L+p\,M_p+p'\,M_{p'}\right).
$$

Os índices dos momentos indicam a posição: terminação **m** para o meio da placa e **e** para o engaste.

### 4.3 Laje calculada pela superfície de influência

Quando não há tabela para a geometria ou a vinculação desejada, a superfície de influência pode ser calculada numericamente e carregada com o veículo, que é o que as tabelas fazem. No exemplo da seção 7, a laje central foi calculada assim, por diferenças finitas, com o script {download}`superficie_influencia.py <../_static/aulas/tabuleiro/superficie_influencia.py>`. O mesmo script reproduz os coeficientes clássicos de placas: momento no centro de uma placa quadrada apoiada sob carga uniforme $0{,}0479\,q\,a^2$ ($\nu = 0{,}3$) e momento no engaste de uma faixa longa $-q\,\ell^2/12$.

## 5. Laje em balanço

### 5.1 Modelo

A laje em balanço é calculada como uma faixa de $1{,}00\text{ m}$ engastada na face da longarina. Para as ações permanentes:

$$
M_{g}=\sum_i G_i\,x_i ,
$$

somando o peso próprio da laje (com espessura variável, se for o caso), o pavimento até a face da barreira, a barreira e o guarda-corpo, cada um com seu braço $x_i$ até o engaste.

### 5.2 Carga da roda

A roda é posicionada o mais perto possível do bordo: o veículo encostado na face da barreira e o centro da roda a $0{,}50\text{ m}$ da lateral do veículo. A carga se distribui a $45^\circ$ em direção ao engaste. Assim, a largura de distribuição no engaste, para uma roda à distância $x$, é $b_{\mathrm{ef}} = b_1 + 2x$ (Figura 5.1).

```{figure} ../_static/aulas/tabuleiro/tab-balanco-distribuicao.png
:alt: Distribuição a 45 graus das cargas das rodas na laje em balanço
:width: 65%
:align: center

**Figura 5.1** – Laje em balanço: as faixas de distribuição das três rodas do alinhamento externo se sobrepõem no engaste.
```

**Atenção à sobreposição.** As rodas de um mesmo alinhamento estão a $1{,}50\text{ m}$ umas das outras. Quando $b_{\mathrm{ef}} > 1{,}50\text{ m}$, as faixas se sobrepõem e as três rodas passam a atuar juntas numa largura conjunta:

$$
b_{\mathrm{ef,conj}}=2\cdot1{,}50+b_{\mathrm{ef}}
\qquad\qquad
M_q=\frac{3\,P\,x}{b_{\mathrm{ef,conj}}}
\qquad\qquad
V_q=\frac{3\,P}{b_{\mathrm{ef,conj}}} .
$$

Considerar uma única roda, nesse caso, subestima o momento no engaste.

## 6. Continuidade e compatibilização dos momentos

### 6.1 Por que compatibilizar

Calculadas isoladamente, a laje central (engastada na longarina) e a laje em balanço fornecem dois valores diferentes de momento negativo no apoio comum. Na estrutura real, o momento no apoio é único. A **compatibilização** escolhe esse valor e corrige o momento positivo da laje central de forma coerente.

### 6.2 Critério de compatibilização

O critério consolidado na prática brasileira, aceito pela NBR 6118 [[6]](#ref-6) (item 14.7.6.2) quando as lajes são calculadas isoladas, é:

$$
X=\max\left\{\frac{X_1+X_2}{2};\ 0{,}8\,X_{\mathrm{maior}};\ X_{\mathrm{bal}}\right\},
$$

em que $X_1$ e $X_2$ são os módulos dos momentos de engaste das duas lajes. A terceira parcela vale quando uma das lajes é um **balanço**: como o balanço é isostático, seu momento no engaste não pode ser reduzido.

### 6.3 Correção do momento positivo

Se o momento compatibilizado $X$ é menor que o momento de engaste $X_{\mathrm{iso}}$ calculado para a laje central isolada, o apoio "devolve" parte do momento ao vão. O momento positivo é então aumentado:

$$
M^{+}_{\mathrm{corr}}=M^{+}+\frac{X_{\mathrm{iso}}-X}{2} .
$$

Se $X > X_{\mathrm{iso}}$, o momento positivo **não é reduzido**, a favor da segurança.

```{note}
**Continuidade na direção do tráfego.** Entre painéis vizinhos da laje central (sobre as transversinas), Araújo [[2]](#ref-2) apresenta o procedimento simplificado da antiga NB-2: cada painel é calculado como simplesmente apoiado e o momento negativo no apoio é adotado entre $1/3$ e $2/3$ do momento máximo do vão, com a correspondente redução do momento positivo. Como os momentos da carga móvel predominam, a correção costuma ser feita só neles.
```

## 7. Exemplo resolvido: esforços nas lajes da ponte-exemplo

```{admonition} Dados
:class: destaque-azul

Os dados são **hipotéticos** e não correspondem à ponte de referência do trabalho prático.

- Duas longarinas com eixos a $5{,}00\text{ m}$ e alma $b_w = 40\text{ cm}$; transversinas nos apoios e no meio do vão de $20{,}00\text{ m}$.
- Laje central L1: $\ell_x = 5{,}00\text{ m}$ (entre eixos das longarinas) e $\ell_y = 10{,}00\text{ m}$ (entre transversinas); $h = 22\text{ cm}$, com mísula até $30\text{ cm}$ junto às longarinas.
- Laje em balanço L2: $\ell_b = 2{,}00\text{ m}$ da face da longarina ao bordo; espessura variando de $30\text{ cm}$ no engaste a $20\text{ cm}$ no bordo; barreira New Jersey com área $0{,}23\text{ m}^2$ ($p_{\mathrm{barr}} = 5{,}75\text{ kN/m}$), base de $40\text{ cm}$ e centro de gravidade a $1{,}83\text{ m}$ do engaste.
- Pavimento de $8\text{ cm}$ mais $2\text{ kN/m}^2$ de recapeamento; concreto C30; aço CA-50; cobrimento $4\text{ cm}$.
- $\gamma_g = 1{,}35$ e $\gamma_q = 1{,}50$.
```

### 7.1 Ações e coeficientes

$$
g_1=25\cdot0{,}22=5{,}50\text{ kN/m}^2
\qquad
g_2=24\cdot0{,}08+2{,}0=3{,}92\text{ kN/m}^2
\qquad
g=9{,}42\text{ kN/m}^2
$$

$$
\varphi=1{,}35\cdot1{,}25=1{,}6875
\qquad
b_1=0{,}20+0{,}16+0{,}22=0{,}58\text{ m}
\qquad
b_2=0{,}50+0{,}16+0{,}22=0{,}88\text{ m}
$$

### 7.2 Laje central L1 (isolada)

A laje é considerada **engastada nas longarinas** (continuidade com os balanços) e, a favor da segurança para $m_x$, **apoiada nas transversinas**. Como $\ell_y/\ell_x = 2$, o momento principal é $m_x$, na direção transversal ao tráfego.

**Carga permanente.** Integrando as superfícies de influência sobre toda a placa:

| Momento | Coeficiente | Valor ($\text{kN·m/m}$) |
|---|---:|---:|
| $m_{x,g}$ no centro | $0{,}0419\,g\,\ell_x^2$ | $9{,}87$ |
| $m_{y,g}$ no centro | $0{,}0100\,g\,\ell_x^2$ | $2{,}36$ |
| $X_{g}$ no engaste ($m_x$, borda) | $-0{,}0843\,g\,\ell_x^2$ | $-19{,}84$ |

O coeficiente do engaste, próximo de $1/12 = 0{,}0833$, confirma que a laje trabalha praticamente como uma faixa transversal biengastada.

**Carga móvel.** O veículo foi deslocado em toda a placa (passo de $5\text{ cm}$) até se encontrar a posição mais desfavorável para cada momento. A multidão foi aplicada fora do contorno do veículo, só onde a superfície tem o sinal procurado:

| Momento | Rodas | Multidão | Total (sem $\varphi$) | Com $\varphi$ | Posição crítica |
|---|---:|---:|---:|---:|---|
| $m_{x,q}$ no centro | $25{,}87$ | $1{,}45$ | $27{,}32$ | $46{,}10$ | uma roda no centro |
| $m_{y,q}$ no centro | $13{,}36$ | $0{,}56$ | $13{,}93$ | $23{,}50$ | uma roda no centro |
| $X_{q}$ no engaste | $-51{,}81$ | $-1{,}86$ | $-53{,}67$ | $-90{,}56$ | roda a $0{,}80\text{ m}$ da longarina |

Valores em $\text{kN·m/m}$. Repare que a multidão quase não contribui: na laje, as rodas dominam.

**Esforços de cálculo da laje isolada:**

$$
M^{+}_{x,d}=1{,}35\cdot9{,}87+1{,}50\cdot46{,}10=82{,}48\text{ kN·m/m}
$$

$$
M^{+}_{y,d}=1{,}35\cdot2{,}36+1{,}50\cdot23{,}50=38{,}44\text{ kN·m/m}
$$

$$
X_{d,\mathrm{iso}}=1{,}35\cdot(-19{,}84)+1{,}50\cdot(-90{,}56)=-162{,}63\text{ kN·m/m}
$$

### 7.3 Laje em balanço L2

**Carga permanente** (por metro, momentos em relação à face da longarina):

| Parcela | Carga | Braço (m) | Momento ($\text{kN·m/m}$) |
|---|---:|---:|---:|
| Laje (trapézio $30 \to 20\text{ cm}$) | $25\cdot\frac{0{,}30+0{,}20}{2}\cdot2{,}00=12{,}50\text{ kN/m}$ | $0{,}933$ | $11{,}67$ |
| Pavimento até a barreira ($1{,}60\text{ m}$) | $3{,}92\cdot1{,}60=6{,}27\text{ kN/m}$ | $0{,}80$ | $5{,}02$ |
| Barreira | $5{,}75\text{ kN/m}$ | $1{,}83$ | $10{,}52$ |
| **Total** | $V_g = 24{,}52\text{ kN/m}$ | | $M_g = 27{,}21$ |

**Carga móvel.** Com o veículo encostado na barreira, o alinhamento externo de rodas fica a $x = 1{,}60 - 0{,}50 = 1{,}10\text{ m}$ do engaste. Nesse ponto a laje tem $h = 24{,}5\text{ cm}$, logo $b_1 = 0{,}20 + 0{,}16 + 0{,}245 = 0{,}605\text{ m}$ e:

$$
b_{\mathrm{ef}}=0{,}605+2\cdot1{,}10=2{,}805\text{ m}>1{,}50\text{ m}\ \Rightarrow\ \text{as faixas se sobrepõem}
$$

$$
b_{\mathrm{ef,conj}}=2\cdot1{,}50+2{,}805=5{,}805\text{ m}
$$

$$
M_q=\frac{3\cdot75\cdot1{,}10}{5{,}805}=42{,}64\text{ kN·m/m}
\qquad
V_q=\frac{3\cdot75}{5{,}805}=38{,}76\text{ kN/m}
$$

Com uma única roda, o resultado seria $75 \cdot 1{,}10/2{,}805 = 29{,}41\text{ kN·m/m}$, cerca de $30\%$ menor.

**Esforços de cálculo:**

$$
M_{d,\mathrm{bal}}=1{,}35\cdot27{,}21+1{,}50\cdot(1{,}6875\cdot42{,}64)=36{,}73+107{,}93=144{,}65\text{ kN·m/m}
$$

$$
V_{d,\mathrm{bal}}=1{,}35\cdot24{,}52+1{,}50\cdot(1{,}6875\cdot38{,}76)=33{,}10+98{,}12=131{,}22\text{ kN/m}
$$

### 7.4 Compatibilização no apoio comum (longarina)

$$
\frac{X_1+X_2}{2}=\frac{162{,}63+144{,}65}{2}=153{,}64
\qquad
0{,}8\cdot162{,}63=130{,}10
\qquad
X_{\mathrm{bal}}=144{,}65
$$

$$
X_d=\max\{153{,}64;\ 130{,}10;\ 144{,}65\}=153{,}64\text{ kN·m/m}
$$

Como $X_d < X_{d,\mathrm{iso}} = 162{,}63$, o momento positivo da laje central é corrigido:

$$
M^{+}_{x,d,\mathrm{corr}}=82{,}48+\frac{162{,}63-153{,}64}{2}=82{,}48+4{,}49=86{,}97\text{ kN·m/m}
$$

**Resumo dos esforços de cálculo** ($\text{kN·m/m}$ e $\text{kN/m}$):

| Seção | Isolada | Compatibilizada |
|---|---:|---:|
| L1 – vão, $m_x$ | $82{,}48$ | $86{,}97$ |
| L1 – vão, $m_y$ | $38{,}44$ | $38{,}44$ |
| Apoio L1/L2 (sobre a longarina) | $-162{,}63$ / $-144{,}65$ | $-153{,}64$ |
| L2 – cortante no engaste | | $131{,}22$ |

### 7.5 Armaduras

Com $f_{cd} = 30/1{,}4 = 21{,}43\text{ MPa}$, $f_{yd} = 435\text{ MPa}$ e as expressões de flexão simples para $b_w = 1{,}00\text{ m}$:

$$
x=1{,}25\,d\left[1-\sqrt{1-\frac{M_d}{0{,}425\,b_w\,d^2\,f_{cd}}}\right]
\qquad\qquad
A_s=\frac{M_d}{f_{yd}\,(d-0{,}4\,x)}
$$

| Posição | $M_d$ | $d$ (m) | $x/d$ | $A_s$ ($\text{cm}^2/\text{m}$) | Adotado |
|---|---:|---:|---:|---:|---|
| L1 vão, $m_x$ (inferior, transversal) | $86{,}97$ | $0{,}172$ | $0{,}22$ | $12{,}76$ | Ø16 c/15 ($13{,}40$) |
| L1 vão, $m_y$ (inferior, longitudinal) | $38{,}44$ | $0{,}159$ | $0{,}11$ | $5{,}81$ | Ø10 c/13 ($6{,}04$) |
| Apoio L1/L2 (superior, $h = 30\text{ cm}$) | $153{,}64$ | $0{,}252$ | $0{,}18$ | $15{,}10$ | Ø16 c/13 ($15{,}47$) |

Todos os valores superam $A_{s,\min} = 0{,}15\%\,b_w\,h$ ($3{,}30$ e $4{,}50\text{ cm}^2/\text{m}$) e todos os domínios atendem $x/d \le 0{,}45$.

**Cortante no engaste do balanço.** Com $\rho_1 = 15{,}47/(100\cdot25{,}2) = 0{,}0061$, $k = 1{,}6 - 0{,}252 = 1{,}35$ e $\tau_{Rd} = 0{,}25\,f_{ctd} = 0{,}362\text{ MPa}$:

$$
V_{Rd1}=0{,}362\cdot1{,}35\cdot(1{,}2+40\cdot0{,}0061)\cdot1000\cdot0{,}252\approx178\text{ kN/m}>V_d=131{,}22\text{ kN/m},
$$

e a laje dispensa armadura transversal.

### 7.6 Momentos para a verificação à fadiga

Para lajes de tabuleiro de pontes rodoviárias, a combinação frequente de fadiga usa $\psi_1 = 0{,}8$ [[6]](#ref-6):

| Seção | $M_{\mathrm{fad,máx}}=M_g+0{,}8\,M_q$ | $M_{\mathrm{fad,mín}}=M_g$ |
|---|---:|---:|
| L1 vão, $m_x$ | $46{,}75$ | $9{,}87$ |
| Engaste L1 | $-92{,}29$ | $-19{,}84$ |
| Engaste L2 | $-84{,}76$ | $-27{,}21$ |

Com esses valores calcula-se a variação de tensão $\Delta\sigma_s$ nas barras e compara-se com os limites da NBR 6118 [[6]](#ref-6). As barras da laje, com grande parcela de carga móvel, costumam ser governadas pela fadiga.

## 8. Roteiro do cálculo do tabuleiro

```{admonition} Roteiro
:class: destaque-verde

1. Definir os painéis: laje central (entre longarinas e transversinas) e laje em balanço.
2. Calcular $g_1$, $g_2$, as cargas da barreira e $\varphi = CIV\cdot CIA$.
3. Laje central isolada: momentos $m_x$, $m_y$ e de engaste por Rüsch ou por superfície de influência.
4. Laje em balanço: momentos e cortante no engaste, verificando a sobreposição das faixas das rodas.
5. Compatibilizar o momento no apoio comum e corrigir o momento positivo da laje central.
6. Dimensionar as armaduras (flexão, mínimas, distribuição) e verificar o cortante ($V_{Rd1}$).
7. Verificar a fadiga com $\psi_1 = 0{,}8$.
```

## Referências

(ref-1)=
**[1]** STUCCHI, F. R. *Pontes e grandes estruturas*. Notas de aula. São Paulo: Escola Politécnica da USP, 2006.

(ref-2)=
**[2]** ARAÚJO, D. de L. *Projeto de ponte em concreto armado com duas longarinas*. 2. ed. Goiânia: UFG, 2018.

(ref-3)=
**[3]** RÜSCH, H. *Berechnungstafeln für rechtwinklige Fahrbahnplatten von Straßenbrücken*. Deutscher Ausschuss für Stahlbeton, Heft 106. Berlin: Ernst & Sohn, 1960.

(ref-4)=
**[4]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7187**: *Projeto de pontes, viadutos e passarelas de concreto*. Rio de Janeiro: ABNT, 2021.

(ref-5)=
**[5]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7188**: *Ações devido ao tráfego de veículos rodoviários e de pedestres em pontes, viadutos e passarelas*. Rio de Janeiro: ABNT, 2024.

(ref-6)=
**[6]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: *Projeto de estruturas de concreto*. Rio de Janeiro: ABNT, 2023 (Emenda 1: 2026).

(ref-7)=
**[7]** TIMOSHENKO, S.; WOINOWSKY-KRIEGER, S. *Theory of plates and shells*. 2. ed. New York: McGraw-Hill, 1959.

(ref-8)=
**[8]** MARCHETTI, O. *Pontes de concreto armado*. 2. ed. São Paulo: Blucher, 2018.
