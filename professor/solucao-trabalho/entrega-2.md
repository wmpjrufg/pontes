## Entrega 2 – Fadiga e armadura final da viga

Esta parte da solução trata da obtenção dos momentos fletores nas seções de
interesse da longarina (item 2.6). Como a ponte é simétrica em relação ao meio
do vão, basta analisar a longarina até essa seção. O cisalhamento não será
abordado neste semestre.

Os modelos do Ftool usados aqui são os mesmos da Entrega 1:
{download}`CargasPermanentes.ftl <../_static/arquivos/entrega1/CargasPermanentes.ftl>`
e {download}`TremTipo-Long.ftl <../_static/arquivos/entrega1/TremTipo-Long.ftl>`.

### 1. Modelo estrutural e seções de interesse

A longarina é modelada como uma viga com dois balanços de $4{,}50\text{ m}$ e
vão central de $25{,}00\text{ m}$, com comprimento total de $34{,}00\text{ m}$.
A origem $x=0$ fica na extremidade do balanço esquerdo, e os apoios estão em
$x=4{,}50\text{ m}$ e $x=29{,}50\text{ m}$.

| Seção | Descrição | $x$ (m) |
|---|---|---:|
| A esq / A dir | Apoio do balanço, à esquerda e à direita | $4{,}50$ |
| B | $1/4$ do vão | $10{,}75$ |
| C | $1/2$ do vão (eixo de simetria) | $17{,}00$ |

Adota-se a convenção usual: momento positivo traciona a fibra inferior. No
Ftool, o momento positivo é desenhado abaixo do eixo da barra.

Para o momento fletor, os valores em A esq e A dir são iguais, porque não há
momento concentrado aplicado no apoio e o diagrama de $M$ é contínuo ali. A
distinção entre os dois lados só altera a força cortante, que sofre um salto
igual à reação de apoio.

### 2. Momentos da carga permanente

As cargas do modelo, determinadas na Entrega 1, são:

| Carga | Valor | Posição |
|---|---:|---|
| Carga permanente distribuída $g_{\mathrm{long}}$ | $75{,}92\text{ kN/m}$ | Toda a viga |
| Carga na extremidade do balanço $P_{\mathrm{ext}}$ | $188{,}00\text{ kN}$ | $x=0$ e $x=34{,}00\text{ m}$ |
| Transversina de apoio $P_{\mathrm{tr,apoio}}$ | $39{,}19\text{ kN}$ | Sobre os apoios |
| Transversina do meio do vão $P_{\mathrm{tr,vão}}$ | $29{,}39\text{ kN}$ | $x=17{,}00\text{ m}$ |

As transversinas de apoio estão aplicadas diretamente sobre os apoios e,
portanto, não produzem momento fletor na longarina.

#### 2.1 Seção A

O balanço é isostático. O momento no apoio é obtido diretamente:

$$
\begin{aligned}
M_{g,A}
&=-P_{\mathrm{ext}}\cdot4{,}50-\frac{g_{\mathrm{long}}\cdot4{,}50^2}{2}\\
&=-188{,}00\cdot4{,}50-\frac{75{,}92\cdot4{,}50^2}{2}\\
&=-846{,}00-768{,}69\\
&=-1\,614{,}69\text{ kN·m}.
\end{aligned}
$$

#### 2.2 Seções B e C

Por simetria, os dois balanços aplicam o mesmo momento $M_{g,A}$ nas
extremidades do vão central. Assim, o momento no vão é a soma do momento da
viga biapoiada com o momento constante $M_{g,A}$. Medindo $x'$ a partir do
apoio, para $x'\le L/2$:

$$
M_g(x')=\frac{g_{\mathrm{long}}\,x'(L-x')}{2}+\frac{P_{\mathrm{tr,vão}}\,x'}{2}+M_{g,A}.
$$

Na seção B, com $x'=6{,}25\text{ m}$:

$$
\begin{aligned}
M_{g,B}
&=\frac{75{,}92\cdot6{,}25\cdot18{,}75}{2}+\frac{29{,}39\cdot6{,}25}{2}-1\,614{,}69\\
&=4\,448{,}44+91{,}84-1\,614{,}69\\
&=2\,925{,}59\text{ kN·m}.
\end{aligned}
$$

Na seção C, com $x'=12{,}50\text{ m}$:

$$
\begin{aligned}
M_{g,C}
&=\frac{75{,}92\cdot25{,}00^2}{8}+\frac{29{,}39\cdot25{,}00}{4}-1\,614{,}69\\
&=5\,931{,}25+183{,}69-1\,614{,}69\\
&=4\,500{,}25\text{ kN·m}.
\end{aligned}
$$

Esses valores coincidem com os do Ftool. No meio do balanço,
$x=2{,}25\text{ m}$, o momento é $-615{,}17\text{ kN·m}$.

### 3. Envoltória do trem-tipo

O trem-tipo longitudinal da longarina, obtido na Entrega 1, é composto por:

- três cargas concentradas $P_d=239{,}36\text{ kN}$, espaçadas de $1{,}50\text{ m}$;
- carga distribuída $q_{2,d}=10{,}60\text{ kN/m}$ no trecho de $6{,}00\text{ m}$ ocupado pelo veículo;
- carga distribuída $q_{1,d}=34{,}53\text{ kN/m}$ fora do trecho ocupado pelo veículo.

São os valores cadastrados no modelo do Ftool. A Entrega 1 apresenta
$P_d=239{,}35\text{ kN}$ e $q_{2,d}=10{,}59\text{ kN/m}$; a diferença é só de
arredondamento. Esses valores já incluem o fator dinâmico $F_D=CIV\cdot CNF\cdot CIA$ e a
distribuição transversal. Não devem ser multiplicados novamente.

A envoltória é obtida com a linha de influência (LI) de momento em cada seção.
Para cada sinal procurado:

1. posicionam-se os eixos do veículo de forma a maximizar $\sum P_d\,\eta$;
   em geral, um dos eixos fica sobre o pico da LI;
2. a multidão é aplicada somente nos trechos em que a LI tem o sinal procurado,
   com $q_{2,d}$ sob o veículo e $q_{1,d}$ no restante.

A carga variável favorável não entra na combinação. Por isso, a multidão só é
colocada nos trechos em que a LI tem o sinal procurado.

#### 3.1 Seção C

A LI de momento em C é triangular no vão, com pico
$\eta_{\mathrm{máx}}=ab/L=12{,}50\cdot12{,}50/25{,}00=6{,}25\text{ m}$.
Nos balanços, a LI é negativa e vale $-2{,}25\text{ m}$ na extremidade.

Para $M_{q,\mathrm{máx}}$, o eixo central fica sobre C, com eixos em
$15{,}50$, $17{,}00$ e $18{,}50\text{ m}$. A área positiva da LI é
$78{,}125\text{ m}^2$, e a área sob o veículo, entre $14{,}00$ e
$20{,}00\text{ m}$, é $33{,}00\text{ m}^2$:

$$
\begin{aligned}
M_{q,\mathrm{máx},C}
&=239{,}36\,(5{,}50+6{,}25+5{,}50)
 +34{,}53\,(78{,}125-33{,}00)
 +10{,}60\cdot33{,}00\\
&=4\,128{,}96+1\,558{,}17+349{,}80\\
&=6\,036{,}93\text{ kN·m}.
\end{aligned}
$$

Para $M_{q,\mathrm{mín}}$, o veículo fica encostado na extremidade de um dos
balanços, com eixos em $0$, $1{,}50$ e $3{,}00\text{ m}$. Cada balanço tem
área negativa de $5{,}0625\text{ m}^2$. O balanço ocupado pelo veículo recebe
$q_{2,d}$, e o outro recebe $q_{1,d}$:

$$
\begin{aligned}
M_{q,\mathrm{mín},C}
&=239{,}36\,(-2{,}25-1{,}50-0{,}75)
 -10{,}60\cdot5{,}0625
 -34{,}53\cdot5{,}0625\\
&=-1\,077{,}12-53{,}66-174{,}81\\
&=-1\,305{,}59\text{ kN·m}.
\end{aligned}
$$

#### 3.2 Seção B

O pico da LI em B é $\eta_{\mathrm{máx}}=6{,}25\cdot18{,}75/25{,}00=4{,}6875\text{ m}$.

Para $M_{q,\mathrm{máx}}$, o primeiro eixo fica sobre B e os demais seguem
para o lado do trecho maior, com eixos em $10{,}75$, $12{,}25$ e
$13{,}75\text{ m}$. A área positiva da LI é $58{,}594\text{ m}^2$, e a área sob
o veículo, entre $9{,}25$ e $15{,}25\text{ m}$, é $24{,}75\text{ m}^2$:

$$
\begin{aligned}
M_{q,\mathrm{máx},B}
&=239{,}36\,(4{,}6875+4{,}3125+3{,}9375)
 +34{,}53\,(58{,}594-24{,}75)
 +10{,}60\cdot24{,}75\\
&=3\,096{,}72+1\,168{,}65+262{,}35\\
&=4\,527{,}72\text{ kN·m}.
\end{aligned}
$$

Para $M_{q,\mathrm{mín}}$, o veículo fica na extremidade do balanço esquerdo,
onde a LI vale $-3{,}375\text{ m}$. Na extremidade do balanço direito, a LI vale
$-1{,}125\text{ m}$. As áreas negativas são $7{,}594\text{ m}^2$ no balanço
esquerdo e $2{,}531\text{ m}^2$ no direito:

$$
\begin{aligned}
M_{q,\mathrm{mín},B}
&=239{,}36\,(-3{,}375-2{,}25-1{,}125)
 -10{,}60\cdot7{,}594
 -34{,}53\cdot2{,}531\\
&=-1\,615{,}68-80{,}49-87{,}40\\
&=-1\,783{,}57\text{ kN·m}.
\end{aligned}
$$

#### 3.3 Seção A

A LI de momento em A é $\eta=-(4{,}50-x)$ no balanço esquerdo e nula no
restante da viga. Logo, o trem-tipo só produz momento negativo em A:
$M_{q,\mathrm{máx},A}=0$.

Para $M_{q,\mathrm{mín}}$, o veículo fica na extremidade do balanço, com eixos
em $0$, $1{,}50$ e $3{,}00\text{ m}$. Como o veículo de $6{,}00\text{ m}$ cobre
todo o balanço, a multidão nesse trecho é $q_{2,d}$:

$$
\begin{aligned}
M_{q,\mathrm{mín},A}
&=239{,}36\,(-4{,}50-3{,}00-1{,}50)-10{,}60\cdot10{,}125\\
&=-2\,154{,}24-107{,}33\\
&=-2\,261{,}57\text{ kN·m}.
\end{aligned}
$$

```{warning}
Usar $q_{1,d}=34{,}53\text{ kN/m}$ em todo o balanço superestima o momento
negativo em A em cerca de $242\text{ kN·m}$. Sob o veículo, a multidão é
$q_{2,d}$.
```

Os valores calculados à mão coincidem com a envoltória do Ftool, com diferença
inferior a $0{,}1\text{ kN·m}$.

### 4. Combinação última (ELU)

A combinação última normal é:

$$
M_{sd}=\gamma_g\,M_g+\gamma_q\,M_q,
\qquad
\gamma_q=1{,}50,
\qquad
\gamma_g=
\begin{cases}
1{,}35 & \text{permanente desfavorável}\\
1{,}00 & \text{permanente favorável}
\end{cases}
$$

Para decidir o valor de $\gamma_g$, pergunta-se: **se a carga permanente
aumentasse, o esforço procurado ficaria pior?** Se sim, a permanente é
desfavorável e $\gamma_g=1{,}35$. Se não, ela é favorável e $\gamma_g=1{,}00$.

A carga permanente favorável não pode ser retirada da estrutura, pois sempre
existe; apenas não é majorada. Já a carga variável favorável simplesmente não
entra na combinação. Além disso, a permanente é tratada como uma única ação:
o mesmo $\gamma_g$ vale para toda a viga, sem usar $1{,}35$ no vão e $1{,}00$
nos balanços na mesma combinação.

| Seção | $M_{sd,\mathrm{máx}}$: $\gamma_g$ | $M_{sd,\mathrm{mín}}$: $\gamma_g$ |
|---|:---:|:---:|
| A | $1{,}00$ (favorável) | $1{,}35$ (desfavorável) |
| B | $1{,}35$ (desfavorável) | $1{,}00$ (favorável) |
| C | $1{,}35$ (desfavorável) | $1{,}00$ (favorável) |

#### 4.1 Seção C, $M_{sd,\mathrm{máx}}$

Procura-se o maior momento positivo. Como $M_{g,C}>0$, aumentar a permanente
aumenta o momento positivo. Logo, a permanente é desfavorável:

$$
M_{sd,\mathrm{máx},C}
=1{,}35\cdot4\,500{,}25+1{,}50\cdot6\,036{,}93
=6\,075{,}34+9\,055{,}39
=15\,130{,}73\text{ kN·m}.
$$

#### 4.2 Seção C, $M_{sd,\mathrm{mín}}$

Procura-se o menor momento. O trem-tipo nos balanços reduz o momento em C, e
a permanente positiva compensa essa redução. Logo, ela é favorável:

$$
M_{sd,\mathrm{mín},C}
=1{,}00\cdot4\,500{,}25+1{,}50\cdot(-1\,305{,}59)
=4\,500{,}25-1\,958{,}39
=2\,541{,}86\text{ kN·m}.
$$

```{warning}
Com $\gamma_g=1{,}35$, o resultado seria
$6\,075{,}34-1\,958{,}39=4\,116{,}95\text{ kN·m}$. Majorar a permanente
favorável faz o momento mínimo parecer maior do que é. Esse resultado é
contra a segurança.
```

#### 4.3 Seção B, $M_{sd,\mathrm{mín}}$

Esta é a seção mais sensível. O momento negativo do trem-tipo é grande em
relação ao momento da permanente, e a seção fica próxima da inversão de sinal:

$$
M_{sd,\mathrm{mín},B}
=1{,}00\cdot2\,925{,}59+1{,}50\cdot(-1\,783{,}57)
=2\,925{,}59-2\,675{,}36
=250{,}23\text{ kN·m}.
$$

Com $\gamma_g=1{,}35$, o resultado seria
$3\,949{,}55-2\,675{,}36=1\,274{,}19\text{ kN·m}$, cerca de cinco vezes maior.
A seção pareceria distante da inversão, quando está próxima dela.

#### 4.4 Seção A, $M_{sd,\mathrm{máx}}$

Em A, $M_{g,A}<0$ e $M_{q,\mathrm{máx},A}=0$. O momento máximo é o maior valor
algébrico, isto é, o menos negativo. A permanente negativa afasta o momento
desse máximo, portanto é favorável:

$$
M_{sd,\mathrm{máx},A}=1{,}00\cdot(-1\,614{,}69)+1{,}50\cdot0=-1\,614{,}69\text{ kN·m}.
$$

Mesmo nesse caso, o momento permanece negativo. Portanto, a fibra inferior
em A nunca é tracionada, e o dimensionamento à flexão dessa seção usa apenas
$M_{sd,\mathrm{mín}}$.

#### 4.5 Seção A, $M_{sd,\mathrm{mín}}$

Os dois momentos são negativos e se somam. Aumentar a permanente torna o
momento ainda mais negativo, então ela é desfavorável:

$$
M_{sd,\mathrm{mín},A}
=1{,}35\cdot(-1\,614{,}69)+1{,}50\cdot(-2\,261{,}57)
=-2\,179{,}83-3\,392{,}35
=-5\,572{,}18\text{ kN·m}.
$$

#### 4.6 Extensão da armadura negativa

A envoltória $M_{sd,\mathrm{mín}}$ troca de sinal dentro do vão. Até esse ponto,
a longarina precisa de armadura superior para momento negativo:

| $\gamma_g$ na combinação mínima | $M_{sd,\mathrm{mín}}=0$ em | Distância ao apoio A |
|---|---:|---:|
| $1{,}00$ (correto) | $x=10{,}34\text{ m}$ | $5{,}84\text{ m}$ |
| $1{,}35$ (incorreto) | $x=9{,}25\text{ m}$ | $4{,}75\text{ m}$ |

Com o coeficiente incorreto, a armadura negativa seria interrompida cerca de
$1{,}1\text{ m}$ antes do necessário. O comprimento final das barras ainda deve
incluir a ancoragem e a decalagem, tratadas no detalhamento.

### 5. Tabela de momentos nas seções de interesse

**Tabela 2.1.** Momentos fletores nas seções de interesse, em kN·m.

| Momento | A esq | A dir | B ($L/4$) | C ($L/2$) |
|---|---:|---:|---:|---:|
| $M_g$ | $-1\,614{,}7$ | $-1\,614{,}7$ | $2\,925{,}6$ | $4\,500{,}2$ |
| $M_{q,\mathrm{máx}}$ | $0{,}0$ | $0{,}0$ | $4\,527{,}7$ | $6\,036{,}9$ |
| $M_{q,\mathrm{mín}}$ | $-2\,261{,}6$ | $-2\,261{,}6$ | $-1\,783{,}6$ | $-1\,305{,}6$ |
| $M_{sd,\mathrm{máx}}$ | $-1\,614{,}7$ | $-1\,614{,}7$ | $10\,741{,}1$ | $15\,130{,}7$ |
| $M_{sd,\mathrm{mín}}$ | $-5\,572{,}2$ | $-5\,572{,}2$ | $250{,}2$ | $2\,541{,}9$ |

```{figure} ../../professor/solucao-trabalho/figuras/entrega2-envoltoria-momentos.png
:width: 100%

Momentos característicos e envoltória de cálculo no ELU, da extremidade do
balanço até o meio do vão. O momento positivo está desenhado para baixo,
como no Ftool.
```

### 6. Momentos para a verificação à fadiga

Para a verificação à fadiga, item 2.7, usa-se a combinação frequente com
$\psi_1=0{,}5$, valor adotado pela NBR 6118 para vigas de pontes rodoviárias.
Como o veículo passa e sai da ponte, cada seção oscila entre dois valores:

$$
M_{\mathrm{fad,máx}}=M_g+\psi_1\,M_{q,\mathrm{máx}}
\qquad\qquad
M_{\mathrm{fad,mín}}=M_g+\psi_1\,M_{q,\mathrm{mín}}
\qquad\qquad
\Delta M_{\mathrm{fad}}=M_{\mathrm{fad,máx}}-M_{\mathrm{fad,mín}} .
$$

Todos os momentos entram **com sinal** (positivo traciona a fibra inferior), e
máximo e mínimo são algébricos: num momento negativo, o "máximo" é o de menor
módulo. O sinal é o que permite identificar a **fadiga alternada**: se
$M_{\mathrm{fad,máx}}$ e $M_{\mathrm{fad,mín}}$ têm sinais opostos, a mesma barra
passa de tracionada a comprimida a cada passagem do veículo. Se têm o mesmo
sinal, a face tracionada é sempre a mesma.

#### 6.1 Seção A (apoio do balanço)

Da Tabela 2.1: $M_g=-1\,614{,}69\text{ kN·m}$,
$M_{q,\mathrm{máx}}=0$ e $M_{q,\mathrm{mín}}=-2\,261{,}57\text{ kN·m}$.

$$
\begin{aligned}
M_{\mathrm{fad,máx},A}&=-1\,614{,}69+0{,}5\cdot0=-1\,614{,}69\text{ kN·m}\\
M_{\mathrm{fad,mín},A}&=-1\,614{,}69+0{,}5\cdot(-2\,261{,}57)=-1\,614{,}69-1\,130{,}78=-2\,745{,}47\text{ kN·m}\\
\Delta M_{\mathrm{fad},A}&=(-1\,614{,}69)-(-2\,745{,}47)=1\,130{,}78\text{ kN·m}
\end{aligned}
$$

Os dois valores são negativos: **não há alternância**. A armadura superior fica
sempre tracionada, oscilando entre os efeitos de $-1\,614{,}69$ e
$-2\,745{,}47\text{ kN·m}$.

#### 6.2 Seção B ($L/4$)

Da Tabela 2.1: $M_g=+2\,925{,}59\text{ kN·m}$,
$M_{q,\mathrm{máx}}=+4\,527{,}70\text{ kN·m}$ e
$M_{q,\mathrm{mín}}=-1\,783{,}58\text{ kN·m}$.

$$
\begin{aligned}
M_{\mathrm{fad,máx},B}&=+2\,925{,}59+0{,}5\cdot(+4\,527{,}70)=2\,925{,}59+2\,263{,}85=+5\,189{,}44\text{ kN·m}\\
M_{\mathrm{fad,mín},B}&=+2\,925{,}59+0{,}5\cdot(-1\,783{,}58)=2\,925{,}59-891{,}79=+2\,033{,}80\text{ kN·m}\\
\Delta M_{\mathrm{fad},B}&=(+5\,189{,}44)-(+2\,033{,}80)=3\,155{,}64\text{ kN·m}
\end{aligned}
$$

Embora o trem-tipo produza momento negativo em B (veículo nos balanços), a carga
permanente mantém o momento de fadiga positivo nos dois extremos: **não há
alternância**. A armadura inferior fica sempre tracionada. Repare que, na fadiga,
a permanente entra sem majoração e a carga móvel com $\psi_1 = 0{,}5$; por isso
a seção fica mais longe da inversão do que no ELU ($M_{sd,\mathrm{mín}} = 250{,}2\text{ kN·m}$).

#### 6.3 Resumo

**Tabela 2.2.** Momentos da combinação de fadiga, em kN·m.

| Momento | A | B ($L/4$) | C ($L/2$) |
|---|---:|---:|---:|
| $M_g$ | $-1\,614{,}7$ | $+2\,925{,}6$ | $+4\,500{,}2$ |
| $M_{\mathrm{fad,máx}}=M_g+0{,}5\,M_{q,\mathrm{máx}}$ | $-1\,614{,}7$ | $+5\,189{,}4$ | $+7\,518{,}7$ |
| $M_{\mathrm{fad,mín}}=M_g+0{,}5\,M_{q,\mathrm{mín}}$ | $-2\,745{,}5$ | $+2\,033{,}8$ | $+3\,847{,}5$ |
| $\Delta M_{\mathrm{fad}}=M_{\mathrm{fad,máx}}-M_{\mathrm{fad,mín}}$ | $1\,130{,}8$ | $3\,155{,}6$ | $3\,671{,}3$ |
| Alternância de sinal? | não | não | não |
| Face tracionada | superior | inferior | inferior |

A variação $\Delta M_{\mathrm{fad}}$ é o que produz a variação de tensão
$\Delta\sigma_s$ na armadura tracionada, a ser comparada com os limites da
NBR 6118 no item 7.

### 7. Dimensionamento da armadura e verificação à fadiga

*Solução em preparação.*
