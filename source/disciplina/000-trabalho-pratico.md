# Trabalho Prático

## 1. Diretrizes de projeto

O trabalho prático do semestre consiste no dimensionamento de uma ponte de concreto armado com duas longarinas moldadas *in loco*. Será tomada como referência a ponte que consta na bibliografia de Marchetti [[1]](#ref-1), cujo corte longitudinal é apresentado na [Figura 1](#fig-1).

(fig-1)=
```{figure} ../_static/aulas/ponte-referencia.png
:alt: Corte longitudinal da ponte de referência
:width: 80%

**Figura 1** – Corte longitudinal da ponte de referência, com vão central de 25,00 m, balanços de 4,50 m, pilares de 12,00 m e tubulões com base alargada de 3,00 m de diâmetro (altura da base de 1,35 m).
```

O projeto de fôrma completo da ponte de referência (plantas, cortes e detalhamento) está disponível para download nos seguintes formatos:

- Planta em PDF: {download}`projeto_completo.pdf <../_static/arquivos/projeto_completo.pdf>`
- Desenho em AutoCAD: {download}`projeto_completo.dwg <../_static/arquivos/projeto_completo.dwg>`
- Modelo BIM em Revit: {download}`projeto_completo.rvt <../_static/arquivos/projeto_completo.rvt>`
- Modelo 3D em SketchUp: {download}`projeto_completo_3d.skp <../_static/arquivos/projeto_completo_3d.skp>`

### 1.1 Parâmetros base do projeto

- Vão principal (central): $25{,}00\text{ m}$
- Balanços: $4{,}50\text{ m}$
- Altura dos pilares: $12{,}00\text{ m}$ (diâmetro/largura de $1{,}20\text{ m}$)
- Fundação em Tubulão de Concreto Armado
- Concreto: $f_{ck} = 30\text{ MPa}$
- Aço: CA-50 ($f_{yk} = 500\text{ MPa}$)
- Cobrimento nominal: $c_{\text{nom}} = 4\text{ cm}$
- Classe de agressividade ambiental: CAA III (forte / industrial ou marinha)

## 2. Roteiro de etapas e entregas do semestre

```{admonition} Como enviar as entregas pelo Google Classroom
:class: destaque-azul

Cada entrega deve ser enviada em **um único arquivo ZIP**, por um integrante do grupo, nomeado com o número da entrega seguido do **nome e sobrenome de cada integrante**, sem espaços, acentos ou caracteres especiais:

`entregaN_NomeSobrenome1NomeSobrenome2.zip`

Exemplos: `entrega1_JoaoSilvaMariaSouza.zip`, `entrega2_JoaoSilvaMariaSouza.zip` e assim por diante, seguindo o mesmo padrão nas demais entregas. Arquivos fora desse padrão poderão não ser avaliados.
```

### 2.1 Desenho da estrutura e das seções transversais em CAD

- Lançamento da geometria da ponte em CAD: Corte longitudinal, Corte B, Corte C, Detalhe 1 e Detalhe 5.

```{admonition} Detalhe 5: Barreira New Jersey
:class: destaque-vermelho

Para o Detalhe 5, a barreira tipo New Jersey deverá ser representada conforme os detalhes do *Manual de projeto de obras-de-arte especiais*, do DNER, Publicação IPR 698 [[3]](#ref-3), substituindo a configuração apresentada no desenho de referência.
```

### 2.2 Levantamento de carregamentos permanentes

- Peso próprio das longarinas, laje do tabuleiro, mísulas e transversinas ($\gamma_c = 25\text{ kN/m}^3$).
- Peso da pavimentação em CBUQ: considerar peso específico de $\gamma_{\text{asf}} = 24\text{ kN/m}^3$ e espessura média inicial de $8\text{ cm}$, acrescido de uma carga permanente de $2\text{ kN/m}^2$ sobre a área pavimentada para previsão de recapeamento futuro.
- Peso das barreiras de proteção tipo New Jersey (Detalhe 5) e guarda-corpos metálicos com peso linear de $0,10\text{ kN/m}$.

### 2.3 Cálculo dos esforços permanentes

- Determinação da carga permanente distribuída $g_{\text{long}}$ por metro linear em cada longarina.
- Modelo estrutural contínuo/isostático considerando a geometria longitudinal (vão central de $25\text{ m}$ e balanços/extensões de $4{,}5\text{ m}$ e $3{,}0\text{ m}$).
- Obtenção dos diagramas de momentos fletores ($M_g$) e esforços cortantes ($V_g$) ao longo do comprimento das vigas para a carga permanente.

````{admonition} Entrega 1: Desenhos e carregamentos permanentes
:class: destaque-verde

A **Entrega 1** contempla os itens **2.1, 2.2 e 2.3** do roteiro de projeto.

**Item 2.1 - Desenhos em AutoCAD:** desenvolver as seções transversais e os detalhes necessários para determinar o peso das peças de concreto da ponte de referência.

**Item 2.2 - Carregamentos permanentes:** determinar as áreas e os volumes das peças desenhadas em AutoCAD e calcular os carregamentos permanentes que atuam sobre a ponte, incluindo os demais componentes previstos neste item.

**Item 2.3 - Análise de esforços no Ftool:** representar o sistema estrutural da ponte, aplicar os carregamentos permanentes calculados e determinar os diagramas de momentos fletores e esforços cortantes na longarina.

**Apresentação e arquivos obrigatórios:**

- Entregar os desenhos em arquivo **DWG compatível com o AutoCAD 2020**, com layouts e **viewports configuradas para plotagem**, escalas definidas e enquadramento adequado.
- Entregar também as **versões em PDF de todas as pranchas**, correspondentes aos layouts do DWG, com textos, cotas e detalhes legíveis no tamanho de impressão previsto.
- Entregar a **memória de cálculo em PDF**, com áreas, volumes, pesos específicos, carregamentos e resultados da análise, e o **arquivo editável do modelo no Ftool**.
- Identificar todas as pranchas e a memória de cálculo com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto.
- Numerar as pranchas em sequência, indicando o número da prancha e o total, por exemplo, **01/03, 02/03 e 03/03**.
- Incluir **notas de projeto quando necessárias**, esclarecendo unidades, materiais, hipóteses, convenções e informações necessárias à interpretação dos desenhos e cálculos.
- Organizar e nomear os arquivos conforme o **modelo de ZIP** apresentado abaixo, de modo que seja possível identificar o grupo, o conteúdo e a prancha correspondente. Conferir se todos os arquivos abrem e se as referências externas necessárias estão incluídas.

**Estrutura do arquivo ZIP da Entrega 1:** o ZIP deve ter o nome `entrega1_NomeSobrenome1NomeSobrenome2.zip` (um nome e um sobrenome por integrante) e conter uma pasta com o mesmo nome, organizada da seguinte forma:

```text
entrega1_NomeSobrenome1NomeSobrenome2.zip
└── entrega1_NomeSobrenome1NomeSobrenome2/
    ├── 01_desenhos/
    │   ├── entrega1_NomeSobrenome1NomeSobrenome2.dwg
    │   ├── prancha_01de03.pdf
    │   ├── prancha_02de03.pdf
    │   └── prancha_03de03.pdf
    ├── 02_memoria_calculo/
    │   └── memoria_calculo_entrega1_NomeSobrenome1NomeSobrenome2.pdf
    └── 03_ftool/
        └── modelo_longarina_entrega1_NomeSobrenome1NomeSobrenome2.ftl
```

O número de pranchas depende do projeto de cada grupo; o DWG deve conter todos os layouts, e cada layout deve ter o PDF correspondente. Referências externas (xrefs, imagens e fontes) devem estar incluídas na pasta `01_desenhos`.

**Critérios de avaliação da Entrega 1 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Organização das pranchas | Distribuição dos desenhos, alinhamento, uso do espaço e organização do carimbo. | 1,0 |
| Numeração das pranchas | Sequência completa, indicação do total e correspondência entre DWG e PDF. | 0,5 |
| Legibilidade e plotagem | Leitura de textos, cotas e detalhes; escalas, espessuras de linha e viewports; ausência de cortes e sobreposições no PDF. | 1,5 |
| Identificação e notas de projeto | Nome completo e matrícula de todos os integrantes, identificação do projeto e notas necessárias à compreensão. | 1,0 |
| Arquivos entregues | DWG compatível com AutoCAD 2020, PDFs de todas as pranchas, memória de cálculo em PDF e modelo editável do Ftool, completos e acessíveis. | 1,0 |
| Desenhos e detalhes técnicos | Atendimento ao item 2.1, geometria, cotas e adequação do Detalhe 5 ao manual indicado. | 2,0 |
| Carregamentos permanentes | Áreas, volumes, unidades, pesos específicos e determinação dos carregamentos previstos no item 2.2. | 1,5 |
| Modelo e esforços no Ftool | Geometria, apoios, aplicação dos carregamentos e diagramas de momentos fletores e esforços cortantes na longarina. | 1,5 |
| **Total** | | **10,0** |

**Regra de pontuação:** cada critério recebe 100% dos pontos quando atendido integralmente, 50% quando atendido parcialmente e zero quando ausente, incorreto ou impossível de verificar. A falta de identificação completa de todos os integrantes zera o critério de identificação e notas. Arquivos ausentes ou que não abrem não pontuam no conteúdo que depender deles para ser verificado. A ausência de notas de projeto não gera desconto quando elas não forem necessárias. A nota final corresponde à soma dos critérios.
````

### 2.4 Levantamento de carregamentos variáveis

**Ações variáveis ($q$):**

- Veículo-tipo normativo TB-450 (ABNT NBR 7188:2024 [[2]](#ref-2)): 3 eixos de $150\text{ kN}$ ($75\text{ kN}$ por roda) espaçados em $1{,}50\text{ m}$.
- Carga distribuída de multidão: $q = 5{,}0\text{ kN/m}^2$ na pista de rolamento.
- Carga nos passeios para pedestres: $3{,}0\text{ kN/m}^2$ concomitante ou $5{,}0\text{ kN/m}^2$ para dimensionamento local.

**Coeficientes dinâmicos:**

- Coeficiente de Impacto Vertical (CIV) — conforme ABNT NBR 7188:2024 [[2]](#ref-2).
- Coeficiente de Número de Faixas (CNF) — conforme ABNT NBR 7188:2024 [[2]](#ref-2).
- Coeficiente de Impacto Adicional ($CIA = 1{,}25$ para estruturas de concreto).
- Fator dinâmico combinado: $F_D = CIV \cdot CNF \cdot CIA$.

### 2.5 Cálculo dos esforços do trem-tipo

- Construção das linhas de influência (LI) para momentos fletores e esforços cortantes nas seções críticas ($L/8$, $L/4$, $3L/8$, $L/2$ e sobre os apoios).
- Determinação do trem-tipo transversal simplificado (método da alavanca ou grelha) para definir a parcela de carga transferida para a longarina mais solicitada.
- Posicionamento longitudinal do veículo TB-450 e da carga de multidão sobre as LI para obter os esforços máximos e mínimos.
- Majoração de todos os esforços móveis pelo fator dinâmico $F_D$.

### 2.6 Envoltória final de esforços

- Combinação de ações no Estado Limite Último (ELU), conforme NBR 7187 e NBR 6118, utilizando $\gamma_g = 1{,}35$ para ações permanentes e $\gamma_q = 1{,}50$ para ações variáveis.
- Traçado dos diagramas envoltórios de flexão ($M_{sd,\text{máx}}$ e $M_{sd,\text{mín}}$) e de cortante ($V_{sd,\text{máx}}$).

### 2.7 Dimensionamento da longarina com verificação à fadiga

**Dimensionamento à flexão (ELU):**

- Cálculo da armadura longitudinal $A_s$ para atender aos momentos $M_{sd,\text{máx}}$ ao longo da viga.
- Verificação da capacidade resistente da seção em "T" ou retangular.

**Dimensionamento ao cisalhamento (ELU):**

- Verificação da compressão diagonal do concreto ($V_{sd} \le V_{rd2}$).
- Cálculo dos estribos $A_{sw}/s$ (modelo de cálculo I ou II da NBR 6118).

**Verificação à fadiga (ELS-FAT):**

- Determinação da variação da tensão no aço ($\Delta \sigma_s$) decorrente da passagem do veículo-tipo.
- Verificação da tensão máxima no concreto sob a combinação de fadiga ($\sigma_c \le 0{,}45 \cdot f_{ck}$).

### 2.8 Dimensionamento do tabuleiro (laje)

O tabuleiro é a parte da superestrutura que recebe diretamente as ações do tráfego e as transmite às longarinas e transversinas. Neste trabalho ele é uma laje maciça de concreto armado, e seu dimensionamento é **local**: avalia-se uma faixa de $1{,}00\text{ m}$ de laje, na direção transversal ao tráfego, submetida às ações permanentes e às cargas das rodas do veículo-tipo TB-450.

```{warning}
Material em preparação. O cálculo dos momentos móveis na laje central (tabelas de Rüsch/Pucher ou método das faixas equivalentes) ainda será detalhado em aula; o roteiro abaixo apresenta a sequência de cálculo e o desenvolvimento completo da laje em balanço.
```

#### 2.8.1 Regiões da laje e modelo estrutural

A laje é dividida em duas regiões, que se comportam de maneira distinta:

- **Laje central:** painel compreendido entre as longarinas. Como as longarinas possuem rigidez à torção, a laje fica parcialmente engastada nelas; por simplicidade, o modelo adotado é de uma faixa contínua, apoiada nas longarinas, com vão efetivo $\ell_x$ determinado conforme a NBR 6118 [[4]](#ref-4). Se a relação $\ell_y/\ell_x$ entre os vãos nas duas direções (distância entre transversinas e distância entre longarinas) for maior que $2$, a laje é armada em **uma direção** — como ocorre na ponte de referência, em que as transversinas estão espaçadas de $12{,}50\text{ m}$. Caso contrário, é armada em **duas direções**.
- **Laje em balanço:** trecho que se projeta além das longarinas até a borda do tabuleiro. É modelada como uma **viga em balanço engastada na longarina**, sendo, em geral, a região mais solicitada à flexão e ao cisalhamento por conta do braço de alavanca da barreira e das rodas.

#### 2.8.2 Ações na laje

**Ações permanentes (por metro quadrado ou por metro linear):**

$$
g_1 = \gamma_c \cdot h
\qquad\qquad
g_2 = \gamma_{\text{asf}} \cdot e_{\text{asf}} + 2{,}0
\qquad\qquad
p_{\text{barr}} = A_{\text{barr}} \cdot \gamma_c
$$

em que $g_1$ é o peso próprio da laje ($\text{kN/m}^2$); $h$, a espessura da laje (m); $g_2$, a carga de pavimentação mais a reserva de recapeamento ($\text{kN/m}^2$); $e_{\text{asf}}$, a espessura do pavimento (m); e $p_{\text{barr}}$, a carga linear da barreira New Jersey ($\text{kN/m}$), obtida com a área $A_{\text{barr}}$ da seção desenhada no Detalhe 5. O guarda-corpo metálico entra como carga linear adicional de $0{,}10\text{ kN/m}$.

**Ações variáveis:** cargas das rodas do TB-450 ($P = 75\text{ kN}$ por roda), com área de contato de $0{,}20\text{ m} \times 0{,}50\text{ m}$ e carga de multidão nas regiões não ocupadas pelo veículo. Nos elementos transversais ao tráfego (lajes e transversinas) **não se aplica o CNF** [[2]](#ref-2); a majoração dinâmica é, portanto:

$$
\varphi = CIV \cdot CIA
\qquad\qquad
Q_{\text{roda}} = P \cdot \varphi
$$

Para vãos inferiores a $10{,}0\text{ m}$, $CIV = 1{,}35$; com $CIA = 1{,}25$ para estruturas de concreto, resulta $\varphi = 1{,}35 \cdot 1{,}25 = 1{,}6875$.

**Difusão da carga da roda:** a carga se espalha a $45^\circ$ através do pavimento e até o plano médio da laje, de modo que a área carregada na superfície média passa a ter dimensões:

$$
b_1 = 0{,}20 + 2\,e_{\text{asf}} + h
\qquad\qquad
b_2 = 0{,}50 + 2\,e_{\text{asf}} + h
$$

em que $b_1$ é a dimensão na direção do tráfego e $b_2$, na direção transversal ao tráfego (m).

#### 2.8.3 Esforços solicitantes

**Laje em balanço.** Com o balanço $\ell_b$ medido da face da longarina até a borda, os momentos fletores característicos no engaste, por metro de laje, são:

$$
M_{g,k} = \frac{(g_1 + g_2)\,\ell_b^{\,2}}{2} + p_{\text{barr}}\cdot x_{\text{barr}}
$$

em que $x_{\text{barr}}$ é a distância do centro de gravidade da barreira até o engaste (m). Para a roda posicionada a uma distância $x$ do engaste, admite-se a distribuição da carga a $45^\circ$ em direção ao apoio, de modo que a largura efetiva no engaste é $b_{\text{ef}} = b_1 + 2x$:

$$
M_{q,k} = \frac{Q_{\text{roda}}\cdot x}{b_{\text{ef}}}
\qquad\qquad
V_{q,k} = \frac{Q_{\text{roda}}}{b_{\text{ef}}}
$$

O posicionamento crítico é com a roda o mais próximo possível da barreira, respeitando a distância mínima entre a roda e o guarda-rodas. Os esforços de cálculo no ELU são:

$$
M_d = 1{,}35\,M_{g,k} + 1{,}50\,M_{q,k}
\qquad\qquad
V_d = 1{,}35\,V_{g,k} + 1{,}50\,V_{q,k}
$$

**Laje central.** Para as ações permanentes, adotando a faixa de $1{,}00\text{ m}$ com engastamento nas longarinas como hipótese simplificadora, os momentos são $M^{-} = -g\,\ell_x^2/12$ nos apoios e $M^{+} = g\,\ell_x^2/24$ no vão. Para as rodas do TB-450, os momentos $m_x$ e $m_y$ ($\text{kNm/m}$) são obtidos por tabelas de Rüsch ou Pucher, ou pelo método das faixas equivalentes (modelo de viga contínua no Ftool, com a roda na posição mais desfavorável e a largura efetiva de distribuição). Os valores obtidos são majorados por $\varphi$ e combinados com $\gamma_g = 1{,}35$ e $\gamma_q = 1{,}50$.

#### 2.8.4 Dimensionamento da armadura (ELU)

A seção é retangular, com $b_w = 100\text{ cm}$, altura útil $d = h - c_{\text{nom}} - \phi/2$ e $f_{cd} = 30/1{,}4 = 21{,}43\text{ MPa}$. A posição da linha neutra e a armadura de flexão são:

$$
x = 1{,}25\,d\left[1 - \sqrt{1 - \frac{M_d}{0{,}425\,b_w\,d^{2}\,f_{cd}}}\,\right]
\qquad\qquad
A_s = \frac{M_d}{f_{yd}\,(d - 0{,}4\,x)}
$$

com $f_{yd} = 500/1{,}15 = 434{,}78\text{ MPa}$ e a verificação do domínio ($x/d \le 0{,}45$). A armadura não pode ser inferior à mínima, $A_{s,\min} = 0{,}15\%\,b_w\,h$ para $f_{ck} = 30\text{ MPa}$. A armadura de distribuição (longitudinal ao tráfego) deve respeitar:

$$
A_{s,\text{dist}} \ge \max\left(0{,}20\,A_{s,\text{princ}};\ 0{,}9\text{ cm}^2/\text{m};\ 0{,}5\,A_{s,\min}\right)
$$

O espaçamento da armadura principal não deve ser superior a $20\text{ cm}$ nem a $2h$ (o menor valor).

**Cisalhamento.** Lajes sem armadura transversal devem atender a $V_d \le V_{Rd1}$ (NBR 6118, item 19.4.1 [[4]](#ref-4)):

$$
V_{Rd1} = \tau_{Rd}\,k\,(1{,}2 + 40\,\rho_1)\,b_w\,d
\qquad
\tau_{Rd} = 0{,}25\,f_{ctd}
\qquad
k = |1{,}6 - d| \ge 1
\qquad
\rho_1 = \frac{A_{s1}}{b_w\,d} \le 0{,}02
$$

com $d$ em metros no cálculo de $k$ e $f_{ctd} = 0{,}7 \cdot 0{,}3\,f_{ck}^{2/3}/1{,}4 = 1{,}45\text{ MPa}$. Por se tratar de estrutura sujeita a cargas repetidas, a armadura da laje deve ainda ser verificada à **fadiga**, conforme a NBR 6118 [[4]](#ref-4).

```{admonition} Exemplo ilustrativo: laje em balanço
:class: destaque-azul

Os dados abaixo são **hipotéticos** e não correspondem à ponte de referência; servem apenas para mostrar a sequência de cálculo.

**Dados:** $\ell_b = 1{,}50\text{ m}$; $h = 25\text{ cm}$; $e_{\text{asf}} = 8\text{ cm}$; barreira com $p_{\text{barr}} = 0{,}23 \cdot 25 = 5{,}75\text{ kN/m}$ e $x_{\text{barr}} = 1{,}30\text{ m}$; roda a $x = 1{,}00\text{ m}$ do engaste; $c_{\text{nom}} = 4\text{ cm}$ e $\phi = 12{,}5\text{ mm}$, logo $d = 20{,}4\text{ cm}$.

**Ações permanentes:** $g_1 = 0{,}25 \cdot 25 = 6{,}25\text{ kN/m}^2$ e $g_2 = 24 \cdot 0{,}08 + 2 = 3{,}92\text{ kN/m}^2$.

$$
M_{g,k} = \frac{(6{,}25 + 3{,}92)\cdot 1{,}50^2}{2} + 5{,}75 \cdot 1{,}30 = 18{,}92\text{ kNm/m}
\qquad
V_{g,k} = (6{,}25 + 3{,}92)\cdot 1{,}50 + 5{,}75 = 21{,}01\text{ kN/m}
$$

**Carga da roda:** $b_1 = 0{,}20 + 2 \cdot 0{,}08 + 0{,}25 = 0{,}61\text{ m}$; $b_{\text{ef}} = 0{,}61 + 2 \cdot 1{,}00 = 2{,}61\text{ m}$; $Q_{\text{roda}} = 75 \cdot 1{,}6875 = 126{,}56\text{ kN}$.

$$
M_{q,k} = \frac{126{,}56 \cdot 1{,}00}{2{,}61} = 48{,}49\text{ kNm/m}
\qquad
V_{q,k} = \frac{126{,}56}{2{,}61} = 48{,}49\text{ kN/m}
$$

**Esforços de cálculo:** $M_d = 1{,}35 \cdot 18{,}92 + 1{,}50 \cdot 48{,}49 = 98{,}27\text{ kNm/m}$ e $V_d = 1{,}35 \cdot 21{,}01 + 1{,}50 \cdot 48{,}49 = 101{,}09\text{ kN/m}$.

**Flexão:** $x = 3{,}56\text{ cm}$ ($x/d = 0{,}17 \le 0{,}45$) e $A_s = 11{,}93\text{ cm}^2/\text{m}$, maior que $A_{s,\min} = 3{,}75\text{ cm}^2/\text{m}$. Adota-se $\phi 12{,}5\text{ c/10}$ ($12{,}27\text{ cm}^2/\text{m}$). A armadura de distribuição mínima é $0{,}20 \cdot 11{,}93 = 2{,}39\text{ cm}^2/\text{m}$, adotando-se $\phi 8\text{ c/20}$ ($2{,}51\text{ cm}^2/\text{m}$).

**Cisalhamento:** $k = 1{,}6 - 0{,}204 = 1{,}40$ e $\rho_1 = 11{,}93/(100 \cdot 20{,}4) = 0{,}0059$, logo $V_{Rd1} = 0{,}362 \cdot 1{,}40 \cdot (1{,}2 + 40 \cdot 0{,}0059) \cdot 1000 \cdot 204 \cdot 10^{-3} \approx 148\text{ kN/m} > V_d = 101{,}09\text{ kN/m}$. A laje dispensa armadura transversal.
```

### 2.9 Dimensionamento da transversina

As transversinas são as vigas transversais que ligam as longarinas. Na ponte de referência existem dois tipos, conforme os detalhes do projeto de fôrma: a **transversina de apoio**, localizada sobre os pilares, e a **transversina de vão**, localizada no meio do vão. Suas funções são:

- **travar as longarinas**, impedindo a distorção da seção transversal e o tombamento das vigas durante a construção;
- **distribuir as cargas** entre as longarinas, colaborando com a laje na repartição transversal da carga móvel;
- **servir de ponto de apoio** do tabuleiro durante o macaqueamento (elevação para a substituição dos aparelhos de apoio).

**Tabela 2.1 — Dimensões das transversinas lidas no desenho de referência** (conferir no projeto de fôrma).

| Transversina | Largura $b_w$ | Altura total (com a laje) | Função principal no dimensionamento |
|---|---:|---:|---|
| De vão | $30\text{ cm}$ | $175\text{ cm}$ | Travamento e cargas das rodas sobre ela |
| De apoio | $40\text{ cm}$ | $200\text{ cm}$ | Macaqueamento e travamento sobre os pilares |

#### 2.9.1 Transversina de vão

O modelo é de uma **viga biapoiada nas longarinas**, com vão teórico igual à distância entre eixos das longarinas e seção em T (a laje atua como mesa colaborante). As ações são o peso próprio da alma e as cargas das rodas do TB-450 posicionadas diretamente sobre a transversina, o que é uma hipótese a favor da segurança (modelos de grelha mostram que parte da carga é absorvida pela laje). Com duas rodas de eixo, afastadas de $e = 2{,}00\text{ m}$, e vão $\ell$, os esforços máximos para a carga de roda $P_d = \gamma_q\,Q_{\text{roda}}$ são:

$$
M_{d,\max} = M_{g,d} + \frac{P_d\,(\ell - e)}{2}
\qquad\qquad
V_{d,\max} = V_{g,d} + P_d\left(2 - \frac{e}{\ell}\right)
$$

O momento é obtido com as rodas simétricas em relação ao meio do vão; o cortante, com uma das rodas sobre o apoio. A majoração é feita com $\varphi = CIV \cdot CIA$, sem o CNF, como nas lajes [[2]](#ref-2).

#### 2.9.2 Transversina de apoio e macaqueamento

A transversina de apoio é solicitada, além de seu peso próprio, pelos esforços da **operação de macaqueamento**. Admite-se o tráfego interrompido, de modo que a força de elevação por macaco é:

$$
F_{\text{mac},d} = \frac{\gamma_g \cdot R_{g,k}}{n_{\text{mac}}}
$$

em que $R_{g,k}$ é a reação permanente característica da linha de apoio considerada e $n_{\text{mac}}$, o número de macacos. A transversina é modelada como viga em T apoiada nos macacos e carregada pelas reações das longarinas e pelo peso próprio. Se os macacos estão alinhados com as longarinas, a transferência é praticamente direta e o dimensionamento é governado pelo cisalhamento, pela armadura de suspensão e pelo esmagamento do concreto sob os macacos; se existe excentricidade $e_m$ entre o macaco e a longarina, surge o momento $M = F_{\text{mac},d}\cdot e_m$ na transversina.

#### 2.9.3 Dimensionamento da armadura

**Flexão.** Seção T ou retangular, com as mesmas expressões do item 2.8.4 e a largura $b_w$ da transversina. Para alturas superiores a $60\text{ cm}$ é necessária **armadura de pele** em cada face da alma, com $A_{s,\text{pele}} = 0{,}10\%\,A_{c,\text{alma}}$ por face, espaçada de no máximo $20\text{ cm}$ e $d/3$.

**Cisalhamento** (modelo de cálculo I, NBR 6118 [[4]](#ref-4)):

$$
V_{Rd2} = 0{,}27\,\alpha_{v2}\,f_{cd}\,b_w\,d
\qquad
\alpha_{v2} = 1 - \frac{f_{ck}}{250}
\qquad
V_{c} = 0{,}6\,f_{ctd}\,b_w\,d
$$

$$
\frac{A_{sw}}{s} = \frac{V_{sd} - V_c}{0{,}9\,d\,f_{ywd}}
\qquad\qquad
\left(\frac{A_{sw}}{s}\right)_{\min} = 0{,}2\,\frac{f_{ctm}}{f_{ywk}}\,b_w
$$

com $V_{sd} \le V_{Rd2}$ e $f_{ywd}$ limitado a $435\text{ MPa}$.

**Torção.** Nas transversinas, a torção decorre da rotação das longarinas, ou seja, é uma torção de **compatibilidade**. Ela pode ser desprezada nos esforços de cálculo desde que se respeite a armadura mínima de torção e se controle a fissuração (NBR 6118, item 17.5 [[4]](#ref-4)); adotam-se, portanto, estribos fechados e armadura longitudinal mínima ao longo do perímetro da seção.

```{admonition} Roteiro do dimensionamento da transversina
:class: destaque-verde

1. Definir geometria, vão e modelo estrutural (vão: biapoiada nas longarinas; apoio: viga sobre macacos).
2. Calcular as ações: peso próprio, carga das rodas majorada por $\varphi$ e força de macaqueamento.
3. Obter $M_d$ e $V_d$ e conferir $V_d \le V_{Rd2}$.
4. Dimensionar $A_s$ (superior e inferior), os estribos $A_{sw}/s$, a armadura de pele e a armadura mínima de torção.
5. Detalhar a armadura na prancha e conferir os cobrimentos ($c_{\text{nom}} = 4\text{ cm}$, CAA III).
```

### 2.10 Forças horizontais

- **Frenagem e aceleração:** maior valor entre 25% do peso do veículo-tipo ($0{,}25 \times 450\text{ kN} = 112{,}5\text{ kN}$) ou 5% da carga total de multidão na pista utilizável.
- **Ação do vento:** pressão característica do vento aplicada à área projetada lateral da superestrutura (com e sem tráfego).
- **Variação térmica e retração/fluência:** avaliação do deslocamento horizontal de origem térmica ($\Delta T$) transmitido aos apoios e ao topo dos pilares.

### 2.11 Dimensionamento dos pilares e infraestrutura

Na ponte de referência, cada linha de apoio possui **dois pilares circulares** de $\phi = 1{,}20\text{ m}$ e $H = 12{,}00\text{ m}$, um sob cada longarina, com aparelho de apoio de neoprene no topo e fundação em tubulão. Cada pilar é dimensionado à **flexo-compressão**, com a seção de concreto $A_c = \pi D^2/4 = 1{,}131\text{ m}^2$.

#### 2.11.1 Modelo estrutural

Como o neoprene não impede o deslocamento horizontal do topo, o pilar é modelado como um **console engastado na base** (tubulão) e livre no topo. A força horizontal total pode ser distribuída entre os apoios proporcionalmente à rigidez dos aparelhos de neoprene, $K = G\,A/h_n$, em que $G$ é o módulo de elasticidade transversal, $A$ a área em planta e $h_n$ a altura do aparelho. Para o console, o comprimento de flambagem é $\ell_e = 2H = 24{,}00\text{ m}$.

#### 2.11.2 Solicitações

**Força normal:** reação máxima da longarina (permanente mais trem-tipo majorado) mais o peso próprio do pilar, $G_{\text{pil}} = \gamma_c\,A_c\,H = 25 \cdot 1{,}131 \cdot 12{,}00 = 339{,}3\text{ kN}$.

$$
N_d = \gamma_g\,(N_{g,k} + G_{\text{pil}}) + \gamma_q\,N_{q,k}
$$

**Momento fletor na base:** produzido pelas forças horizontais do item 2.10 (frenagem, vento e variação térmica), aplicadas no topo do pilar:

$$
M_{1d} = \gamma_q \cdot \left(H_{\text{fren}} + H_{\text{vento}} + H_{\text{térm}}\right) \cdot H
$$

Devem ser verificadas pelo menos duas combinações: **$N_{\max}$ com o momento associado** e **$M_{\max}$ com $N_{\min}$** (somente ações permanentes, $\gamma_g = 1{,}0$), pois a menor compressão pode ser a mais desfavorável para a armadura. As ações variáveis secundárias são combinadas com os fatores $\psi_0$ da NBR 8681/NBR 7187.

#### 2.11.3 Esbeltez e efeitos de 2ª ordem

Para a seção circular, o raio de giração é $i = D/4 = 0{,}30\text{ m}$ e o índice de esbeltez é:

$$
\lambda = \frac{\ell_e}{i} = \frac{4\,\ell_e}{D} = \frac{4 \cdot 24{,}00}{1{,}20} = 80
$$

Os efeitos locais de 2ª ordem podem ser desprezados se $\lambda \le \lambda_1$, com:

$$
\lambda_1 = \frac{25 + 12{,}5\,e_1/h}{\alpha_b}, \qquad 35 \le \lambda_1 \le 90
$$

em que $e_1 = M_{1d}/N_d$ é a excentricidade de 1ª ordem, $h = D$ e $\alpha_b = 1{,}0$ (valor a favor da segurança para pilar em balanço). Como $\lambda = 80 > \lambda_1$, os efeitos de 2ª ordem precisam ser considerados. Para $\lambda \le 90$, pode-se utilizar o **método do pilar-padrão com curvatura aproximada** (NBR 6118, item 15.8.3.3.2 [[4]](#ref-4)):

$$
M_{d,\text{tot}} = \alpha_b\,M_{1d} + N_d\,\frac{\ell_e^{\,2}}{10}\,\frac{1}{r} \ge M_{1d}
\qquad
\frac{1}{r} = \frac{0{,}005}{h\,(\nu + 0{,}5)} \le \frac{0{,}005}{h}
\qquad
\nu = \frac{N_d}{A_c\,f_{cd}}
$$

O momento de 1ª ordem também deve respeitar o mínimo $M_{1d,\min} = N_d\,(0{,}015 + 0{,}03\,h)$, com $h$ em metros.

#### 2.11.4 Armadura longitudinal e transversal

Com os esforços de cálculo, determina-se a armadura por **ábacos de flexo-compressão reta para seção circular**, entrando com:

$$
\nu = \frac{N_d}{A_c\,f_{cd}}
\qquad\qquad
\mu = \frac{M_{d,\text{tot}}}{A_c\,D\,f_{cd}}
\qquad\qquad
A_s = \omega\,\frac{A_c\,f_{cd}}{f_{yd}}
$$

Os limites da NBR 6118 [[4]](#ref-4) são $A_{s,\min} = \max(0{,}15\,N_d/f_{yd};\ 0{,}4\%\,A_c)$ e $A_{s,\max} = 8\%\,A_c$ (incluindo regiões de emenda), com no mínimo $6$ barras na seção circular. Os estribos (ou espiral) devem ter $\phi_t \ge \max(5\text{ mm};\ \phi_l/4)$, e espaçamento $s \le \min(20\text{ cm};\ \text{menor dimensão};\ 12\,\phi_l)$ para o aço CA-50.

```{admonition} Exemplo ilustrativo: pilar em balanço
:class: destaque-azul

Os dados abaixo são **hipotéticos** e não correspondem à ponte de referência.

**Dados:** $N_{g,k} = 900\text{ kN}$; $N_{q,k} = 700\text{ kN}$ (já majorado); $H_k = 150\text{ kN}$ (resultante de frenagem, vento e temperatura no topo); $D = 1{,}20\text{ m}$; $H = 12{,}00\text{ m}$; $f_{cd} = 21{,}43\text{ MPa}$; $A_c f_{cd} = 24\,235\text{ kN}$.

**Esforços de 1ª ordem:**

$$
N_d = 1{,}35 \cdot (900 + 339{,}3) + 1{,}50 \cdot 700 = 2\,723\text{ kN}
\qquad
M_{1d} = 1{,}50 \cdot 150 \cdot 12{,}00 = 2\,700\text{ kNm}
$$

**Esbeltez:** $\lambda = 80$; $e_1 = 2700/2723 = 0{,}99\text{ m}$ e $\lambda_1 = 25 + 12{,}5 \cdot (0{,}99/1{,}20) = 35{,}3$. Como $80 > 35{,}3$, há 2ª ordem. O momento mínimo é $M_{1d,\min} = 2723 \cdot 0{,}051 = 139\text{ kNm} < M_{1d}$.

**2ª ordem (pilar-padrão):** $\nu = 2723/24\,235 = 0{,}112$; o cálculo da curvatura dá $0{,}005/[1{,}20 \cdot (0{,}112 + 0{,}5)] = 0{,}0068$, maior que o limite $0{,}005/1{,}20 = 0{,}0042\text{ m}^{-1}$, que passa a valer.

$$
M_{2d} = 2723 \cdot \frac{24^2}{10} \cdot 0{,}00417 = 653\text{ kNm}
\qquad
M_{d,\text{tot}} = 2\,700 + 653 = 3\,353\text{ kNm}
$$

**Armadura:** $\mu = 3353/(24\,235 \cdot 1{,}20) = 0{,}115$ e $\nu = 0{,}112$. Pelo equilíbrio da seção circular (compatibilidade de deformações), $\omega \approx 0{,}22$ e $A_s \approx 123\text{ cm}^2$ ($\rho = 1{,}1\%$). Como $A_{s,\min} = \max(9{,}4;\ 45{,}2) = 45{,}2\text{ cm}^2$ e $A_{s,\max} = 905\text{ cm}^2$, adotam-se $40\,\phi 20$ ($125{,}7\text{ cm}^2$) distribuídos no perímetro, com estribos $\phi 8\text{ c/20}$. A resistência da seção adotada, $M_{Rd}(N_d) \approx 3\,390\text{ kNm}$, supera $M_{d,\text{tot}}$.
```

#### 2.11.5 Verificação da fundação

A fundação do pilar é em **tubulão com base alargada** de $\phi = 3{,}00\text{ m}$ e altura de base de $1{,}35\text{ m}$, conforme o corte longitudinal. Na cota da base, as tensões no solo são verificadas com:

$$
\sigma_{\max,\min} = \frac{N_{\text{base}}}{A_b} \pm \frac{M_{\text{base}}}{W_b} \le \sigma_{\text{adm}}
\qquad
A_b = \frac{\pi D_b^{2}}{4}
\qquad
W_b = \frac{\pi D_b^{3}}{32}
$$

em que $N_{\text{base}}$ inclui o peso do fuste e da base, e $M_{\text{base}}$ acrescenta ao momento na base do pilar o efeito da força horizontal ao longo do fuste. Para $D_b = 3{,}00\text{ m}$, $A_b = 7{,}07\text{ m}^2$ e $W_b = 2{,}65\text{ m}^3$. Deve-se ainda verificar o ângulo de abertura da base do tubulão e, quando necessário, o fuste e a armadura da base conforme a NBR 6122.

## Referências

(ref-1)=
**[1]** MARCHETTI, Osvaldemar. *Pontes de Concreto Armado*. 2. ed. São Paulo: Blucher, 2018. 246 p. ISBN 978-85-212-1278-2.

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *ABNT NBR 7188: Ações devido ao tráfego de veículos rodoviários e de pedestres em pontes, viadutos e passarelas*. Rio de Janeiro: ABNT, 2024.

(ref-3)=
**[3]** BRASIL. Departamento Nacional de Estradas de Rodagem. Diretoria de Desenvolvimento Tecnológico. Divisão de Capacitação Tecnológica. *Manual de projeto de obras-de-arte especiais*. Rio de Janeiro: DNER, 1996. 225 p. (Publicação IPR, 698). Disponível em: [acervo de manuais do DNIT](https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/ipr/coletanea-de-manuais/vigentes/698_manual_de_projeto_de_obras_de_arte_especiais.pdf). Acesso em: 8 set. 2026.

(ref-4)=
**[4]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: *Projeto de estruturas de concreto — Procedimento*. Rio de Janeiro: ABNT, 2014.
