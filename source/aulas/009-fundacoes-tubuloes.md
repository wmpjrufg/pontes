# Aula 09: Fundações de pontes — tubulões

```{admonition} Onde estamos?
:class: destaque-azul

1. Conceitos gerais sobre o projeto de pontes
2. Ações na superestrutura
3. Análise computacional com carga móvel
4. Dimensionamento da longarina
5. Dimensionamento do tabuleiro
6. Dimensionamento da transversina
7. Mesoestrutura: ações horizontais e distribuição entre os apoios
8. Dimensionamento dos pilares
9. **Fundações em tubulão (esta aula)**

Esta aula fecha o caminho das cargas: do pilar ao solo. São apresentados os tipos de fundação usados em pontes, as prescrições da NBR 6122 e da NR-18 para tubulões, a verificação da base, o dimensionamento do fuste e o comportamento sob forças horizontais.
```

## 1. Fundações de pontes

### 1.1 Rasas e profundas

A NBR 6122 [[1]](#ref-1) distingue:

- **fundação rasa (direta):** a carga é transmitida ao terreno pela base, a uma profundidade inferior a duas vezes a menor dimensão da fundação. Exemplos: sapatas e blocos;
- **fundação profunda:** a carga é transmitida pela base (resistência de ponta), pela superfície lateral (resistência de fuste) ou pelas duas. A ponta ou base fica a uma profundidade superior a oito vezes a sua menor dimensão em planta e de no mínimo $3{,}0\text{ m}$. Exemplos: estacas e tubulões.

Nas pontes, as fundações diretas só são viáveis quando há terreno resistente próximo à superfície, sem risco de erosão. O mais comum são as fundações profundas: estacas (cravadas ou escavadas, sob blocos de coroamento) e **tubulões**, em geral um sob cada pilar.

### 1.2 O que é um tubulão

A NBR 6122 [[1]](#ref-1) define o tubulão como um elemento de fundação profunda em que, pelo menos na etapa final da escavação, há descida de pessoal para alargar a base ou limpar o fundo. As cargas são resistidas essencialmente pela base. O tubulão tem três partes:

- **fuste:** trecho cilíndrico, que leva a carga do pilar até a base;
- **base alargada:** tronco de cone (ou de falsa elipse) que aumenta a área de contato com o solo resistente;
- **rodapé:** pequeno cilindro de no mínimo $20\text{ cm}$ de altura na parte inferior da base.

Os tubulões podem ser **a céu aberto**, escavados acima do nível d'água ou em solo estável com controle da água, ou **a ar comprimido**, em que uma campânula pressurizada impede a entrada de água.

### 1.3 Segurança do trabalho: a NR-18

A execução de tubulões envolve trabalho em espaço confinado e em profundidade, com risco de soterramento. A NR-18 [[2]](#ref-2) estabelece regras que afetam diretamente o projeto:

- é **proibida a execução de fundação por tubulão de ar comprimido**;
- é proibido o tubulão **escavado manualmente** com profundidade superior a $15\text{ m}$;
- o tubulão escavado manualmente deve ser **encamisado em toda a sua extensão**, ser precedido de sondagem ou estudo geotécnico quando tiver mais de $3\text{ m}$ e ter **diâmetro mínimo de $0{,}90\text{ m}$**;
- são proibidos o trabalho simultâneo em bases alargadas de tubulões adjacentes e a abertura simultânea de bases tangentes.

```{warning}
Muitos projetos antigos de pontes usaram tubulões a ar comprimido em leitos de rio. Hoje essa solução é proibida. Abaixo do nível d'água, a alternativa passa a ser estacas escavadas com fluido estabilizante, estacas-raiz, estacas cravadas ou tubulões escavados mecanicamente sem descida de pessoal abaixo do nível d'água.
```

## 2. Prescrições da NBR 6122 para tubulões

**Geometria da base** [[1]](#ref-1):

- altura da base $H_b \le 1{,}8\text{ m}$ (até $3{,}0\text{ m}$ nos tubulões a ar comprimido, hoje proibidos pela NR-18);
- base em tronco de cone (ou falsa elipse) sobre rodapé de no mínimo $20\text{ cm}$;
- ângulo da geratriz com a horizontal $\beta \ge 60^\circ$. Com esse ângulo, as tensões de tração no concreto da base são baixas e **a base dispensa armadura**.

Para uma base circular de diâmetro $D_b$ sob um fuste de diâmetro $D_f$:

$$
h_b=\frac{D_b-D_f}{2}\,\tan\beta
\qquad\qquad
H_b=h_b+0{,}20\le1{,}80\text{ m} .
$$

**Resistência lateral.** Nos tubulões, a carga é admitida resistida pela base. Quando o atrito lateral é considerado, despreza-se o trecho de fuste de comprimento igual ao diâmetro da base, imediatamente acima do alargamento [[1]](#ref-1).

**Grandeza fundamental.** Para tubulões, a grandeza de projeto é a **tensão admissível** (ou a tensão resistente de cálculo) na cota da base, como numa fundação direta [[1]](#ref-1).

## 3. Tensão admissível na base

### 3.1 Fatores de segurança

A tensão admissível é obtida dividindo a tensão de ruptura por um fator de segurança global. Para métodos teóricos ou semiempíricos, a NBR 6122 [[1]](#ref-1) exige $FS_g \ge 3{,}0$. Esse valor pode cair para $2{,}0$ quando há provas de carga.

### 3.2 Métodos

- **Teóricos:** fórmulas de capacidade de carga (Terzaghi, Vesic), com os parâmetros de resistência do solo na cota da base e o efeito do embutimento.
- **Semiempíricos:** correlações com o ensaio SPT [[3]](#ref-3). Uma estimativa inicial muito usada na prática brasileira, válida apenas na faixa em que as correlações foram calibradas, é $\sigma_{\mathrm{adm}} \approx 20\,N_{\mathrm{SPT}}\ (\text{kPa})$ na superfície do terreno, com $N_{\mathrm{SPT}}$ médio no bulbo de tensões sob a base. Para bases profundas, o confinamento aumenta a tensão admissível.
- **Prova de carga** sobre placa na cota da base.

Além da ruptura, é preciso verificar os **recalques**, que devem ser compatíveis com a estrutura. Em pontes hiperestáticas, recalques diferenciais entre apoios geram esforços na superestrutura.

## 4. Dimensionamento

### 4.1 Base

A área da base vem da carga vertical total na cota de apoio (incluindo o peso do tubulão):

$$
A_b=\frac{\pi\,D_b^2}{4}\ge\frac{N_{\mathrm{base}}}{\sigma_{\mathrm{adm}}} .
$$

Havendo momento na base, verifica-se:

$$
\sigma_{\max,\min}=\frac{N_{\mathrm{base}}}{A_b}\pm\frac{M_{\mathrm{base}}}{W_b}
\qquad\qquad
W_b=\frac{\pi\,D_b^3}{32} ,
$$

com $\sigma_{\max} \le \sigma_{\mathrm{adm}}$ e, de preferência, $\sigma_{\min} \ge 0$.

### 4.2 Fuste

O diâmetro do fuste deve respeitar a NR-18 ($\ge 0{,}90\text{ m}$ quando há escavação manual) e acomodar o pilar e suas armaduras de ligação.

Pela NBR 6122 [[1]](#ref-1) (item 8.6.3 e Tabela 4), estacas e tubulões comprimidos com tensões até os limites da Tabela 4 podem ser executados em **concreto não armado**, exceto a armadura de ligação com o bloco ou pilar. Para tubulões não encamisados, esse limite de tensão média é $5{,}0\text{ MPa}$. Acima dele, o fuste é dimensionado pela NBR 6118 com:

$$
f_{cd}=\frac{f_{ck}}{\gamma_c}
\qquad
\gamma_f=1{,}4
\qquad
\gamma_s=1{,}15 ,
$$

em que $\gamma_c$ é o da Tabela 4 da NBR 6122. Os valores são altos de propósito, para cobrir as incertezas da concretagem no solo. A classe do concreto depende da agressividade ambiental. Nas classes III e IV, por exemplo, exige-se C40 com $\gamma_c = 3{,}6$, o que dá $f_{cd} \approx 11\text{ MPa}$.

## 5. Tubulão sob forças horizontais

### 5.1 Modelo de Winkler

As forças horizontais no topo do pilar chegam ao tubulão como uma força $H_0$ e um momento $M_0$ no nível do terreno. O fuste é então uma viga apoiada no solo, representado por molas horizontais. Para solos granulares, a rigidez das molas cresce com a profundidade ($E_s = n_h\,z$), e a equação do fuste é:

$$
E\,I\,\frac{d^4y}{dz^4}+n_h\,z\,y=0 .
$$

O parâmetro que governa o problema é o **comprimento característico** $T = \sqrt[5]{E\,I/n_h}$ (Aula 07). Tubulões com comprimento enterrado $L \ge 4T$ se comportam como longos: o momento se anula antes da base e o trecho inferior praticamente não trabalha à flexão. Tubulões curtos ($L < 2T$) giram como corpo rígido e mobilizam a resistência da base. Soluções clássicas foram tabeladas por Matlock e Reese [[4]](#ref-4). O script {download}`winkler_tubulao.py <../_static/aulas/fundacoes/winkler_tubulao.py>` resolve o problema por diferenças finitas.

### 5.2 Verificações

- **Momento no fuste:** o fuste é verificado à flexo-compressão com o momento máximo do modelo de Winkler.
- **Reação lateral do solo:** a pressão horizontal $p = n_h\,z\,y$ deve ficar bem abaixo da resistência passiva. Para solos granulares, Broms [[5]](#ref-5) estima a resistência última por unidade de comprimento em $3\,K_p\,\gamma\,z\,D$.
- **Deslocamento no topo:** deve ser compatível com o funcionamento do aparelho de apoio e da estrutura.

O modelo do **engastamento fictício** a $L_e = 1{,}8\,T$, usado na Aula 07 para a rigidez e a esbeltez do pilar, é adequado para essas finalidades. Para o momento no fuste, porém, ele é conservador, como mostra o exemplo.

## 6. Exemplo resolvido: tubulão do pilar P2

```{admonition} Dados
:class: destaque-azul

Tubulão sob o pilar P2 das Aulas 07 e 08 (dados hipotéticos):

- fuste $D_f = 1{,}40\text{ m}$ com $8{,}00\text{ m}$ de comprimento abaixo do terreno, em areia compacta ($n_h = 17{,}6\text{ MN/m}^3$ [[6]](#ref-6), $\gamma = 19\text{ kN/m}^3$, $\varphi = 35^\circ$);
- base apoiada em camada com $N_{\mathrm{SPT}} \approx 30$; tensão admissível adotada $\sigma_{\mathrm{adm}} = 600\text{ kPa}$;
- classe de agressividade III: concreto C40, $\gamma_c = 3{,}6$ ($f_{cd} = 11{,}1\text{ MPa}$);
- esforços característicos no topo do tubulão: $N = 1\,097{,}9 + 650 = 1\,747{,}9\text{ kN}$; $H_0 = 42{,}0\text{ kN}$ (frenagem, temperatura, retração e vento compostos); $M_0 = 42{,}0\cdot7{,}00 = 293{,}7\text{ kN·m}$.
```

### 6.1 Base

O peso do fuste é $25\cdot1{,}539\cdot8{,}00 = 308\text{ kN}$. Para uma primeira estimativa:

$$
D_b\ge\sqrt{\frac{4\cdot(1\,748+308)}{\pi\cdot600}}=2{,}09\text{ m}\ \Rightarrow\ D_b=2{,}20\text{ m}
$$

$$
h_b=\frac{2{,}20-1{,}40}{2}\cdot\tan60^\circ=0{,}69\text{ m}
\qquad
H_b=0{,}69+0{,}20=0{,}89\text{ m}\le1{,}80\text{ m}
$$

Com o acréscimo de peso da base ($29\text{ kN}$):

$$
N_{\mathrm{base}}=1\,748+308+29=2\,085\text{ kN}
\qquad
\sigma=\frac{2\,085}{\pi\cdot2{,}20^2/4}=549\text{ kPa}\le600\text{ kPa}
$$

O momento que chega à base é praticamente nulo (seção 6.3). As forças horizontais são absorvidas pelo solo ao longo do fuste.

### 6.2 Fuste à compressão

$$
\sigma_{\mathrm{méd}}=\frac{1\,748}{1{,}539}=1{,}14\text{ MPa}<5{,}0\text{ MPa}
$$

Sob compressão centrada, o fuste poderia ser de concreto não armado, exceto a ligação com o pilar.

### 6.3 Fuste sob força horizontal

Com $E\,I = 26{,}84\times10^6\cdot0{,}1886 = 5{,}06\times10^6\text{ kN·m}^2$:

$$
T=\sqrt[5]{\frac{5{,}06\times10^6}{17\,600}}=3{,}10\text{ m}
\qquad\qquad
\frac{L}{T}=\frac{8{,}00}{3{,}10}=2{,}6 ,
$$

ou seja, um tubulão de comportamento intermediário. A solução do modelo de Winkler (Figura 6.1) fornece:

- momento máximo $M_{\max} = 343{,}7\text{ kN·m}$, a $1{,}9\text{ m}$ de profundidade, decaindo até zero na base;
- deslocamento no topo de $1{,}9\text{ mm}$;
- pressão lateral máxima de $73\text{ kN/m}$, cerca de $10\%$ da resistência de Broms ($3\,K_p\,\gamma\,z\,D$, com $K_p = 3{,}69$).

O modelo de engaste fictício daria $M = 293{,}7 + 42{,}0\cdot5{,}58 = 528\text{ kN·m}$, $54\%$ acima do valor do modelo de Winkler.

```{figure} ../_static/aulas/fundacoes/tub-geometria-momento.png
:alt: Geometria do tubulão do exemplo e momento fletor ao longo do fuste
:width: 100%
:align: center

**Figura 6.1** – Geometria do tubulão do exemplo e momento fletor ao longo do fuste pelo modelo de Winkler, comparado com o modelo de engaste fictício.
```

**Verificação do fuste à flexo-compressão** (com $\gamma_f = 1{,}4$):

$$
N_d=1{,}4\cdot1\,748=2\,447\text{ kN}
\qquad
M_d=1{,}4\cdot343{,}7=481\text{ kN·m}
$$

Com $f_{cd} = 11{,}1\text{ MPa}$, a seção circular de $1{,}40\text{ m}$ de concreto simples resiste a $M_{Rd} \approx 1\,240\text{ kN·m}$ para essa força normal. A flexão também não exige armadura, e o fuste recebe apenas a **armadura de ligação com o pilar**: as barras do pilar (24 Ø16) prolongadas no fuste pelo comprimento de ancoragem, com estribos.

## 7. Roteiro

```{admonition} Roteiro do projeto do tubulão
:class: destaque-verde

1. Interpretar as sondagens e escolher a cota de apoio da base e a tensão admissível ($FS_g \ge 3$).
2. Verificar a viabilidade executiva e as restrições da NR-18 (nível d'água, profundidade, diâmetro mínimo, encamisamento).
3. Dimensionar a base: $D_b$ pela tensão admissível, $H_b$ com $\beta \ge 60^\circ$ e rodapé de $20\text{ cm}$, $H_b \le 1{,}8\text{ m}$.
4. Verificar o fuste à compressão (limite da Tabela 4 da NBR 6122) e à flexo-compressão com os momentos do modelo de Winkler.
5. Verificar a reação lateral do solo, o deslocamento no topo e os recalques.
6. Detalhar a armadura de ligação com o pilar e, se necessária, a armadura do fuste.
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6122**: *Projeto e execução de fundações*. Rio de Janeiro: ABNT, 2019 (versão corrigida 2022).

(ref-2)=
**[2]** BRASIL. Ministério do Trabalho e Emprego. **NR-18**: *Segurança e saúde no trabalho na indústria da construção*. Brasília: MTE (redação da Portaria SEPRT nº 3.733/2020 e atualizações).

(ref-3)=
**[3]** VELLOSO, D. A.; LOPES, F. R. *Fundações*. São Paulo: Oficina de Textos, 2010 (v. 1: critérios de projeto, investigação do subsolo e fundações superficiais; v. 2: fundações profundas).

(ref-4)=
**[4]** MATLOCK, H.; REESE, L. C. Generalized solutions for laterally loaded piles. *Journal of the Soil Mechanics and Foundations Division*, ASCE, v. 86, n. SM5, p. 63-91, 1960.

(ref-5)=
**[5]** BROMS, B. B. Lateral resistance of piles in cohesionless soils. *Journal of the Soil Mechanics and Foundations Division*, ASCE, v. 90, n. SM3, p. 123-156, 1964.

(ref-6)=
**[6]** TERZAGHI, K. Evaluation of coefficients of subgrade reaction. *Géotechnique*, v. 5, n. 4, p. 297-326, 1955.
