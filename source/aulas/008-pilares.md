# Aula 08: Pilares de pontes — flexo-compressão e efeitos de segunda ordem

```{admonition} Onde estamos?
:class: destaque-azul

1. Conceitos gerais sobre o projeto de pontes
2. Ações na superestrutura
3. Análise computacional com carga móvel
4. Dimensionamento da longarina
5. Dimensionamento do tabuleiro
6. Dimensionamento da transversina
7. Mesoestrutura: ações horizontais e distribuição entre os apoios
8. **Dimensionamento dos pilares (esta aula)**
9. Fundações em tubulão

Com as forças no topo de cada pilar determinadas na Aula 07, esta aula monta as combinações de cálculo, avalia os efeitos de segunda ordem e dimensiona a armadura do pilar à flexo-compressão.
```

## 1. Pilares de pontes

Nas pontes de duas longarinas, cada linha de apoio costuma ter **um pilar sob cada longarina**, geralmente de seção circular. Os pilares podem ser ligados no topo por uma travessa, formando um pórtico na direção transversal, ou ficar independentes, como na ponte de referência do trabalho prático, em que a transversina de apoio fica acima dos aparelhos de apoio.

Com aparelhos de elastômero no topo, o pilar trabalha como um **console**: engastado na fundação e livre para girar no topo. Ele é solicitado por:

- **força normal**: reações da superestrutura (permanente e carga móvel) e peso próprio;
- **momentos fletores**: forças horizontais no topo (frenagem, temperatura, retração, vento), multiplicadas pela altura, mais as ações aplicadas diretamente no fuste (vento, empuxo, água);
- **efeitos de segunda ordem**, importantes porque os pilares de ponte costumam ser esbeltos.

Seções circulares têm a mesma resistência em qualquer direção. Por isso, os momentos nas duas direções podem ser compostos na resultante:

$$
M_d=\sqrt{M_{d,x}^2+M_{d,y}^2} .
$$

## 2. Combinações de cálculo

As combinações últimas normais seguem a NBR 8681 [[1]](#ref-1):

$$
F_d=\sum\gamma_g\,F_{g,k}+\gamma_{\varepsilon}\,F_{\varepsilon,k}+\gamma_q\left[F_{q1,k}+\sum_{j\ge2}\psi_{0j}\,F_{qj,k}\right],
$$

em que $F_{q1}$ é a ação variável principal e $F_{\varepsilon}$ são as deformações impostas permanentes (retração). Neste curso:

| Ação | Coeficiente |
|---|---|
| Permanentes | $\gamma_g = 1{,}35$ (ou $1{,}00$ se favorável) |
| Retração | $\gamma_\varepsilon = 1{,}20$ (ou $0$ se favorável) |
| Variáveis | $\gamma_q = 1{,}50$ |
| Carga móvel rodoviária (inclui a frenagem) | $\psi_0 = 0{,}7$ |
| Vento | $\psi_0 = 0{,}6$ |
| Temperatura | $\psi_0 = 0{,}6$ |

A frenagem é concomitante com a carga vertical do veículo: faz parte da mesma ação variável. Para os pilares, as combinações típicas são:

- **C1, tráfego principal:** $N_d = 1{,}35\,N_g + 1{,}5\,N_q$; momentos de frenagem com $\gamma_q$, vento e temperatura com $\gamma_q\,\psi_0$;
- **C2, vento principal:** vento com $\gamma_q$, carga móvel e frenagem com $\gamma_q\,\psi_0 = 1{,}5\cdot0{,}7$.

Quando uma ação permanente for favorável, como uma força normal que aumenta a resistência à flexão, verifica-se também a combinação com $\gamma_g = 1{,}0$.

## 3. Efeitos de segunda ordem

### 3.1 Esbeltez

O comprimento de flambagem de um console é o dobro do seu comprimento. Considerando o engastamento fictício da fundação (Aula 07), o comprimento do console vai do topo do pilar até a profundidade $L_e$:

$$
\ell=H+L_e
\qquad\qquad
\ell_e=2\,\ell
\qquad\qquad
\lambda=\frac{\ell_e}{i}
\qquad\qquad
i=\frac{D}{4}\ \text{(seção circular)} .
$$

### 3.2 Quando considerar

Pela NBR 6118 [[2]](#ref-2), os efeitos locais de segunda ordem podem ser desprezados quando $\lambda \le \lambda_1$:

$$
\lambda_1=\frac{25+12{,}5\,e_1/h}{\alpha_b}
\qquad
35\le\lambda_1\le90 .
$$

Para o console, $\alpha_b = 0{,}80 + 0{,}20\,M_C/M_A \ge 0{,}85$, com $M_A$ o momento no engaste e $M_C$ o momento no meio do comprimento. Com força horizontal no topo, $M_C = M_A/2$ e $\alpha_b = 0{,}90$.

O tratamento depende da esbeltez:

| Esbeltez | Método da NBR 6118 [[2]](#ref-2) |
|---|---|
| $\lambda \le \lambda_1$ | dispensa a segunda ordem local |
| $\lambda_1 < \lambda \le 90$ | pilar-padrão com curvatura aproximada ou com rigidez $\kappa$ aproximada |
| $90 < \lambda \le 140$ | pilar-padrão acoplado a diagramas $M$–$N$–$1/r$, considerando a fluência |
| $140 < \lambda \le 200$ | método geral, considerando a fluência |

```{note}
A NBR 7187 [[3]](#ref-3) trata especificamente da segunda ordem em pilares de pontes. Pilares altos, com tabuleiro deslocável ou com fundações muito flexíveis, exigem uma análise mais completa, com a não linearidade física e geométrica do conjunto pilar–fundação.
```

### 3.3 Pilar-padrão com curvatura aproximada

$$
\frac{1}{r}=\frac{0{,}005}{h\,(\nu+0{,}5)}\le\frac{0{,}005}{h}
\qquad\qquad
\nu=\frac{N_d}{A_c\,f_{cd}}
$$

$$
M_{d,\mathrm{tot}}=\alpha_b\,M_{1d,A}+N_d\,\frac{\ell_e^2}{10}\,\frac{1}{r}\ \ge\ M_{1d,A} .
$$

O momento de primeira ordem não pode ser menor que o mínimo, que cobre as imperfeições geométricas locais:

$$
M_{1d,\min}=N_d\,(0{,}015+0{,}03\,h)\qquad(h\text{ em metros}).
$$

## 4. Dimensionamento à flexo-compressão

### 4.1 Grandezas adimensionais

Com $N_d$ e $M_{d,\mathrm{tot}}$, a armadura é obtida por **ábacos de flexo-compressão para seção circular** ou pelo **diagrama de interação** da seção:

$$
\nu=\frac{N_d}{A_c\,f_{cd}}
\qquad
\mu=\frac{M_{d,\mathrm{tot}}}{A_c\,D\,f_{cd}}
\qquad
A_s=\omega\,\frac{A_c\,f_{cd}}{f_{yd}} .
$$

O diagrama de interação é construído impondo as deformações dos domínios da NBR 6118 (concreto com diagrama parábola-retângulo e aço CA-50 elastoplástico) e integrando as tensões na seção.

### 4.2 Disposições construtivas

Pela NBR 6118 [[2]](#ref-2):

- $A_{s,\min}=\max(0{,}15\,N_d/f_{yd};\ 0{,}4\%\,A_c)$ e $A_{s,\max} = 8\%\,A_c$, incluindo as regiões de emenda;
- no mínimo $6$ barras longitudinais em seção circular, com $\phi_\ell \ge 10\text{ mm}$;
- espaçamento entre barras longitudinais não superior a $40\text{ cm}$ nem a duas vezes a menor dimensão;
- estribos com $\phi_t \ge \max(5\text{ mm};\ \phi_\ell/4)$ e espaçamento $s \le \min(20\text{ cm};\ \text{menor dimensão};\ 12\,\phi_\ell)$ para CA-50.

## 5. Exemplo resolvido: pilar P2 da ponte-exemplo

```{admonition} Dados
:class: destaque-azul

Pilar P2 da Aula 07 (dados hipotéticos):

- $D = 1{,}20\text{ m}$, $H = 7{,}00\text{ m}$, $L_e = 5{,}58\text{ m}$; C30 ($f_{cd} = 21{,}43\text{ MPa}$), CA-50; $A_c = 1{,}131\text{ m}^2$;
- reação permanente da superestrutura $N_{g,\mathrm{sup}} = 900\text{ kN}$; reação máxima da carga móvel $N_{q} = 650\text{ kN}$;
- forças no topo (Aula 07): frenagem $32{,}2\text{ kN}$; temperatura $3{,}92\text{ kN}$; retração $3{,}92\text{ kN}$; vento $28{,}0\text{ kN}$.
```

### 5.1 Esforços característicos na base do pilar

$$
G_{\mathrm{pilar}}=25\cdot1{,}131\cdot7{,}00=197{,}9\text{ kN}
\qquad
N_g=900+197{,}9=1\,097{,}9\text{ kN}
$$

| Ação | Força no topo (kN) | Momento na base, $H\cdot7{,}00$ (kN·m) | Direção |
|---|---:|---:|---|
| Frenagem | $32{,}16$ | $225{,}1$ | longitudinal ($x$) |
| Temperatura | $3{,}92$ | $27{,}4$ | longitudinal ($x$) |
| Retração | $3{,}92$ | $27{,}4$ | longitudinal ($x$) |
| Vento | $28{,}04$ | $196{,}2$ | transversal ($y$) |

### 5.2 Combinações de primeira ordem

**C1, tráfego principal:**

$$
N_d=1{,}35\cdot1\,097{,}9+1{,}5\cdot650=2\,457\text{ kN}
$$

$$
M_{d,x}=1{,}5\cdot(225{,}1+0{,}6\cdot27{,}4)+1{,}2\cdot27{,}4=395{,}3\text{ kN·m}
\qquad
M_{d,y}=1{,}5\cdot0{,}6\cdot196{,}2=176{,}6\text{ kN·m}
$$

$$
M_{1d}=\sqrt{395{,}3^2+176{,}6^2}=433{,}0\text{ kN·m}
$$

**C2, vento principal:**

$$
N_d=1{,}35\cdot1\,097{,}9+1{,}5\cdot0{,}7\cdot650=2\,165\text{ kN}
$$

$$
M_{d,x}=1{,}5\cdot(0{,}7\cdot225{,}1+0{,}6\cdot27{,}4)+1{,}2\cdot27{,}4=294{,}0
\qquad
M_{d,y}=1{,}5\cdot196{,}2=294{,}4
\qquad
M_{1d}=416{,}1\text{ kN·m}
$$

### 5.3 Segunda ordem (C1)

$$
\ell=7{,}00+5{,}58=12{,}58\text{ m}
\qquad
\ell_e=25{,}17\text{ m}
\qquad
i=\frac{1{,}20}{4}=0{,}30\text{ m}
\qquad
\lambda=\frac{25{,}17}{0{,}30}=83{,}9
$$

$$
e_1=\frac{433{,}0}{2\,457}=0{,}176\text{ m}
\qquad
\lambda_1=\frac{25+12{,}5\cdot0{,}176/1{,}20}{0{,}90}=29{,}8\ \Rightarrow\ \lambda_1=35
$$

Como $35 < \lambda = 83{,}9 \le 90$, a segunda ordem deve ser considerada e o pilar-padrão com curvatura aproximada é aplicável.

$$
M_{1d,\min}=2\,457\cdot(0{,}015+0{,}03\cdot1{,}20)=125{,}3\text{ kN·m}<433{,}0\ \Rightarrow\ M_{1d,A}=433{,}0\text{ kN·m}
$$

$$
\nu=\frac{2\,457}{1{,}131\cdot21\,430}=0{,}101
\qquad
\frac{0{,}005}{1{,}20\cdot(0{,}101+0{,}5)}=0{,}00693>\frac{0{,}005}{1{,}20}=0{,}00417\ \Rightarrow\ \frac{1}{r}=0{,}00417\text{ m}^{-1}
$$

$$
M_{2d}=2\,457\cdot\frac{25{,}17^2}{10}\cdot0{,}00417=648{,}6\text{ kN·m}
$$

$$
M_{d,\mathrm{tot}}=0{,}90\cdot433{,}0+648{,}6=1\,038\text{ kN·m}
$$

O efeito de segunda ordem é maior que o de primeira ordem: o momento total é $2{,}4$ vezes o momento de primeira ordem. Para C2, o mesmo procedimento fornece $M_{d,\mathrm{tot}} = 946\text{ kN·m}$ com $N_d = 2\,165\text{ kN}$. A combinação C1 governa.

```{warning}
Se a fundação fosse considerada engastada no nível do terreno, o comprimento de flambagem cairia para $14{,}0\text{ m}$, com $\lambda = 47$ e $M_{2d} \approx 200\text{ kN·m}$. O efeito de segunda ordem seria subestimado em mais de três vezes. A flexibilidade da fundação deve entrar na análise do pilar.
```

### 5.4 Armadura

$$
\mu=\frac{1\,038}{1{,}131\cdot1{,}20\cdot21\,430}=0{,}036
\qquad\qquad
\nu=0{,}101
$$

Para esse par $(\nu, \mu)$, a própria seção de concreto, com a compressão de $2\,457\text{ kN}$, resiste a cerca de $1\,150\text{ kN·m}$ (Figura 5.1). Por isso, a armadura de cálculo é nula e **governa a armadura mínima**:

$$
A_{s,\min}=\max\left(\frac{0{,}15\cdot2\,457}{43{,}5};\ 0{,}004\cdot11\,310\right)=\max(8{,}5;\ 45{,}2)=45{,}2\text{ cm}^2
$$

Adotam-se **24 Ø16** ($48{,}3\text{ cm}^2$), com espaçamento de cerca de $14\text{ cm}$ no perímetro. A seção armada resiste a $M_{Rd} \approx 2\,020\text{ kN·m}$ para $N_d = 2\,457\text{ kN}$, com folga sobre $M_{d,\mathrm{tot}} = 1\,038\text{ kN·m}$.

**Estribos:** $\phi_t \ge \max(5;\ 16/4) = 5\text{ mm}$ e $s \le \min(20;\ 120;\ 12\cdot1{,}6 = 19{,}2)\text{ cm}$. Adotam-se estribos circulares Ø8 c/19.

```{figure} ../_static/aulas/pilares/pil-interacao.png
:alt: Diagrama de interação N-M da seção circular do pilar com os pontos de cálculo
:width: 75%
:align: center

**Figura 5.1** – Diagrama de interação da seção circular de $1{,}20\text{ m}$ com 24 Ø16 e da seção de concreto simples, com os pontos de cálculo das combinações C1 e C2.
```

## 6. Roteiro

```{admonition} Roteiro do dimensionamento do pilar
:class: destaque-verde

1. Reunir as cargas verticais (reações e peso próprio) e as forças horizontais no topo (Aula 07).
2. Montar as combinações últimas, alternando a ação variável principal.
3. Compor os momentos nas duas direções ($M_d = \sqrt{M_x^2 + M_y^2}$ para seção circular) e verificar o momento mínimo.
4. Calcular a esbeltez com o engastamento fictício da fundação e comparar com $\lambda_1$.
5. Calcular o momento de segunda ordem pelo método adequado à esbeltez.
6. Dimensionar a armadura por ábaco ou diagrama de interação e respeitar as armaduras mínima e máxima e as disposições construtivas.
```

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 8681**: *Ações e segurança nas estruturas — Procedimento*. Rio de Janeiro: ABNT.

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: *Projeto de estruturas de concreto*. Rio de Janeiro: ABNT, 2023 (Emenda 1: 2026).

(ref-3)=
**[3]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7187**: *Projeto de pontes, viadutos e passarelas de concreto*. Rio de Janeiro: ABNT, 2021.

(ref-4)=
**[4]** ARAÚJO, D. de L. *Projeto de ponte em concreto armado com duas longarinas*. 2. ed. Goiânia: UFG, 2018.

(ref-5)=
**[5]** MARCHETTI, O. *Pontes de concreto armado*. 2. ed. São Paulo: Blucher, 2018.
