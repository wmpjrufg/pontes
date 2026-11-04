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
&=\boxed{75{,}9225\text{ kN/m}}.
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
=\boxed{89{,}00\text{ kN}}.
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
=\boxed{99{,}00\text{ kN}}.
$$

#### 3.3 Carga concentrada resultante por longarina

Caso os dois pesos sejam representados no mesmo nó da extremidade do
balanço, a carga concentrada total em cada longarina será:

$$
P_{\mathrm{ext}}
=P_{\mathrm{ala}}+P_{\mathrm{lap}}
=89{,}00+99{,}00
=\boxed{188{,}00\text{ kN}}.
$$
