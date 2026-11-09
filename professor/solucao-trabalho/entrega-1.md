## Entrega 1 – Determinação das ações permanentes e variáveis

### 1. Levantamento das áreas da seção transversal

As áreas foram obtidas diretamente dos desenhos em CAD. Para a seção
transversal corrente, foram encontrados os seguintes valores:

| Componente | Área da seção transversal |
|---|---:|
| Pavimentação asfáltica | $0{,}730\text{ m}^2$ |
| Barreira New Jersey (cada bordo) | $0{,}220\text{ m}^2$ |
| Estrutura de concreto: tabuleiro, longarinas e balanços | $4{,}269\text{ m}^2$ |

A ponte possui duas longarinas e é simétrica em relação ao eixo
longitudinal. Portanto, metade do peso da estrutura e da pavimentação é
atribuída a cada longarina. Em cada bordo existe uma barreira e um
guarda-corpo; assim, cada longarina recebe integralmente o peso dos elementos
localizados no bordo correspondente.

### 2. Cargas permanentes distribuídas por longarina

Adotam-se os pesos específicos definidos no enunciado:

$$
\gamma_c=25\text{ kN/m}^3
\qquad\text{e}\qquad
\gamma_{\mathrm{asf}}=24\text{ kN/m}^3.
$$

#### 2.1 Peso próprio da estrutura de concreto

$$
g_{\mathrm{est}}
=\frac{4{,}269}{2}\cdot25
=53{,}3625\text{ kN/m}.
$$

#### 2.2 Peso da barreira New Jersey

Como a área de $0{,}220\text{ m}^2$ corresponde a uma barreira, não se
divide esse valor por dois:

$$
g_{\mathrm{bar}}=0{,}220\cdot25=5{,}500\text{ kN/m}.
$$

#### 2.3 Peso da pavimentação asfáltica

$$
g_{\mathrm{asf}}
=\frac{0{,}730}{2}\cdot24
=8{,}760\text{ kN/m}.
$$

#### 2.4 Reserva para recapeamento futuro

A carga de recapeamento é uma carga superficial e deve ser aplicada
separadamente do peso do CBUQ. Para a pista de rolamento com largura total de
$8{,}20\text{ m}$, cada longarina recebe metade dessa largura:

$$
g_{\mathrm{recap}}
=2{,}0\cdot\frac{8{,}20}{2}
=8{,}200\text{ kN/m}.
$$

#### 2.5 Peso do guarda-corpo metálico

Cada longarina recebe o guarda-corpo existente no seu bordo:

$$
g_{\mathrm{gc}}=0{,}100\text{ kN/m}.
$$

#### 2.6 Carga permanente total

Somando as parcelas:

$$
\begin{aligned}
g_{\mathrm{long}}
&=g_{\mathrm{est}}+g_{\mathrm{bar}}+g_{\mathrm{asf}}
  +g_{\mathrm{recap}}+g_{\mathrm{gc}}\\
&=53{,}3625+5{,}500+8{,}760+8{,}200+0{,}100\\
&=75{,}9225\text{ kN/m}.
\end{aligned}
$$

Para o modelo estrutural, pode-se adotar, com arredondamento,
$g_{\mathrm{long}}=75{,}92\text{ kN/m}$ em cada longarina.

### 3. Cargas concentradas na extremidade do balanço

Além da carga permanente distribuída ao longo da ponte, devem ser
considerados o peso da ala aberta e o peso da laje de aproximação. Neste
modelo simplificado, essas ações são representadas por cargas concentradas na
extremidade do balanço. Como os volumes informados correspondem à largura
total da ponte, metade de cada peso é atribuída a cada longarina.

#### 3.1 Ala aberta

O volume total de concreto da ala aberta, obtido no modelo geométrico, é:

$$
V_{\mathrm{ala}}=7{,}12\text{ m}^3.
$$

O peso total da ala é:

$$
G_{\mathrm{ala,tot}}
=V_{\mathrm{ala}}\gamma_c
=7{,}12\cdot25
=178{,}00\text{ kN}.
$$

Consequentemente, a carga concentrada aplicada em cada longarina é:

$$
P_{\mathrm{ala}}
=\frac{178{,}00}{2}
=89{,}00\text{ kN}.
$$

#### 3.2 Laje de aproximação

A laje de aproximação possui comprimento de $4{,}00\text{ m}$, largura de
$9{,}00\text{ m}$ e espessura de $0{,}22\text{ m}$. Seu volume total é:

$$
V_{\mathrm{lap}}
=4{,}00\cdot9{,}00\cdot0{,}22
=7{,}92\text{ m}^3.
$$

O peso total da laje de aproximação é:

$$
G_{\mathrm{lap,tot}}
=V_{\mathrm{lap}}\gamma_c
=7{,}92\cdot25
=198{,}00\text{ kN}.
$$

Distribuindo esse peso igualmente entre as duas longarinas:

$$
P_{\mathrm{lap}}
=\frac{198{,}00}{2}
=99{,}00\text{ kN}.
$$

#### 3.3 Carga concentrada resultante por longarina

Caso os dois pesos sejam representados no mesmo nó da extremidade do
balanço, a carga concentrada total em cada longarina será:

$$
P_{\mathrm{ext}}
=P_{\mathrm{ala}}+P_{\mathrm{lap}}
=89{,}00+99{,}00
=188{,}00\text{ kN}.
$$

### 4. Peso próprio das transversinas

O projeto possui uma transversina em cada seção indicada: uma no meio do
vão e uma sobre cada um dos dois apoios, totalizando três peças. Todas as
transversinas possuem comprimento de $4{,}75\text{ m}$ e altura de
$1{,}65\text{ m}$. A espessura é de $0{,}30\text{ m}$ no meio do vão e de
$0{,}40\text{ m}$ nos apoios.

O peso de cada transversina é dividido igualmente entre as duas longarinas e
representado por uma carga concentrada na seção em que a peça está
localizada.

#### 4.1 Transversina do meio do vão

$$
V_{\mathrm{tr,vão}}
=4{,}75\cdot1{,}65\cdot0{,}30
=2{,}35125\text{ m}^3.
$$

$$
G_{\mathrm{tr,vão}}
=2{,}35125\cdot25
=58{,}78125\text{ kN}.
$$

Logo, a carga concentrada aplicada em cada longarina no meio do vão é:

$$
P_{\mathrm{tr,vão}}
=\frac{58{,}78125}{2}
=29{,}39\text{ kN}.
$$

#### 4.2 Transversinas dos apoios

Para cada transversina de apoio:

$$
V_{\mathrm{tr,apoio}}
=4{,}75\cdot1{,}65\cdot0{,}40
=3{,}135\text{ m}^3.
$$

$$
G_{\mathrm{tr,apoio}}
=3{,}135\cdot25
=78{,}375\text{ kN}.
$$

Assim, a carga concentrada aplicada em cada longarina, sobre cada apoio, é:

$$
P_{\mathrm{tr,apoio}}
=\frac{78{,}375}{2}
=39{,}19\text{ kN}.
$$

### 5. Propriedades do concreto

Adota-se concreto com $f_{ck}=30\text{ MPa}$, peso específico de
$25\text{ kN/m}^3$ e agregado graúdo de granito. Para granito, o coeficiente
de correção do módulo de elasticidade é $\alpha_E=1{,}0$.

O módulo de elasticidade inicial é:

$$
\begin{aligned}
E_{ci}
&=\alpha_E\,5600\sqrt{f_{ck}}\\
&=1{,}0\cdot5600\sqrt{30}\\
&=30\,672\text{ MPa}\\
&=30{,}67\text{ GPa}.
\end{aligned}
$$

Para a análise estrutural, utiliza-se o módulo de elasticidade secante. Para
$f_{ck}=30\text{ MPa}$:

$$
\alpha_i=0{,}8+0{,}2\frac{f_{ck}}{80}
=0{,}8+0{,}2\frac{30}{80}
=0{,}875,
$$

$$
E_{cs}=\alpha_iE_{ci}
=0{,}875\cdot30\,672
=26\,838\text{ MPa}
=26{,}84\text{ GPa}.
$$

Portanto, no modelo estrutural, deve-se cadastrar o material com
$E=E_{cs}=26{,}84\text{ GPa}$, equivalente a $26\,838\text{ MPa}$ ou
$2{,}6838\cdot10^7\text{ kN/m}^2$.

### 6. Determinação do trem-tipo da longarina

O trem-tipo da longarina é obtido posicionando o veículo TB-450 na posição
transversal mais desfavorável e calculando a parcela das cargas móveis
transferida para a longarina estudada. Como a ponte é simétrica, as duas
longarinas possuem o mesmo trem-tipo.

#### 6.1 Linha de influência transversal

Adota-se a origem $x=0$ no eixo da longarina estudada e $x=5{,}25\text{ m}$
no eixo da outra longarina. A ordenada da linha de influência da reação
na longarina estudada é:

$$
\eta(x)=1-\frac{x}{5{,}25}.
$$

As cargas que resultam em ordenadas negativas produzem efeito favorável na
longarina estudada e, nesta determinação simplificada, são desprezadas.

A face interna da barreira do lado estudado encontra-se em:

$$
x_{\mathrm{ini}}=-(1{,}875-0{,}40)=-1{,}475\text{ m}.
$$

O TB-450 é encostado nessa face. Como o centro da roda externa está a
$0{,}50\text{ m}$ da lateral do veículo, as rodas de cada eixo ficam em:

$$
x_1=-1{,}475+0{,}50=-0{,}975\text{ m},
$$

$$
x_2=-0{,}975+2{,}00=1{,}025\text{ m}.
$$

As principais ordenadas para a conta manual são:

| Posição transversal | $x$ (m) | Ordenada $\eta$ |
|---|---:|---:|
| Face interna da barreira esquerda | $-1{,}475$ | $1{,}2810$ |
| Roda 1 | $-0{,}975$ | $1{,}1857$ |
| Longarina estudada | $0{,}00$ | $1{,}0000$ |
| Roda 2 | $1{,}025$ | $0{,}8048$ |
| Lateral direita do veículo | $1{,}525$ | $0{,}7095$ |
| Segunda longarina | $5{,}25$ | $0{,}0000$ |
| Face interna da barreira direita | $6{,}725$ | $-0{,}2810$ |

#### 6.2 Carga concentrada por eixo

A carga transferida à longarina por um eixo do TB-450 é obtida com as duas
rodas de $75\text{ kN}$:

$$
\begin{aligned}
P
&=75\eta_1+75\eta_2\\
&=75\cdot1{,}1857+75\cdot0{,}8048\\
&=149{,}29\text{ kN}.
\end{aligned}
$$

Portanto, o trem-tipo possui três cargas concentradas de $149{,}29\text{ kN}$,
espaçadas longitudinalmente de $1{,}50\text{ m}$. No comprimento de
$6{,}00\text{ m}$ do veículo, os eixos ficam a $1{,}50\text{ m}$,
$3{,}00\text{ m}$ e $4{,}50\text{ m}$ da extremidade dianteira adotada.

#### 6.3 Carga de multidão fora do veículo

Fora do comprimento ocupado pelo veículo, a multidão atua em toda a largura
da pista. Considera-se somente a área positiva da linha de influência, entre
$x=-1{,}475\text{ m}$ e $x=5{,}25\text{ m}$:

$$
A_I=\frac{1{,}2810\cdot6{,}725}{2}=4{,}3072\text{ m}.
$$

Assim, a carga linear sobre a longarina é:

$$
q_1=5{,}00\cdot4{,}3072=21{,}54\text{ kN/m}.
$$

#### 6.4 Carga de multidão ao lado do veículo

No trecho longitudinal de $6{,}00\text{ m}$ ocupado pelo veículo, a multidão
atua somente na parte da pista não ocupada por ele. Como o veículo está
encostado na borda esquerda, considera-se a área positiva entre sua lateral
direita, em $x=1{,}525\text{ m}$, e a segunda longarina, em
$x=5{,}25\text{ m}$:

$$
A_{II}=\frac{0{,}7095\cdot3{,}725}{2}=1{,}3215\text{ m}.
$$

Logo:

$$
q_2=5{,}00\cdot1{,}3215=6{,}61\text{ kN/m}.
$$

#### 6.5 Coeficientes dinâmicos

Para o cálculo do Coeficiente de Impacto Vertical, considera-se somente o vão
central de $25{,}00\text{ m}$:

$$
\begin{aligned}
CIV
&=1+1{,}06\left(\frac{20}{LIV+50}\right)\\
&=1+1{,}06\left(\frac{20}{25+50}\right)\\
&=1{,}2827.
\end{aligned}
$$

Para duas faixas de tráfego:

$$
CNF=1-0{,}05(2-2)=1{,}0000.
$$

Como a ponte é de concreto:

$$
CIA=1{,}25.
$$

O fator dinâmico combinado é:

$$
F_D=CIV\cdot CNF\cdot CIA
=1{,}2827\cdot1{,}0000\cdot1{,}25
=1{,}6033.
$$

#### 6.6 Trem-tipo final da longarina

Aplicando o fator dinâmico combinado:

$$
P_d=149{,}29\cdot1{,}6033=239{,}35\text{ kN},
$$

$$
q_{1,d}=21{,}54\cdot1{,}6033=34{,}53\text{ kN/m},
$$

$$
q_{2,d}=6{,}61\cdot1{,}6033=10{,}59\text{ kN/m}.
$$

O trem-tipo longitudinal final de cada longarina é composto por:

- três cargas concentradas $P_d=239{,}35\text{ kN}$, espaçadas de
  $1{,}50\text{ m}$;
- carga distribuída $q_{2,d}=10{,}59\text{ kN/m}$ no trecho de
  $6{,}00\text{ m}$ ocupado pelo veículo;
- carga distribuída $q_{1,d}=34{,}53\text{ kN/m}$ fora do comprimento
  ocupado pelo veículo.
