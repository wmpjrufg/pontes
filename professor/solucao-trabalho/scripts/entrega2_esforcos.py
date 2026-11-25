"""
Entrega 2 - Momentos fletores nas seções de interesse da longarina.

Confere, por cálculo independente, os valores obtidos no Ftool:
  - CargasPermanentes.ftl  -> momento da carga permanente (Mg)
  - TremTipo-Long.ftl      -> envoltória do trem-tipo (Mq,max e Mq,min) via linhas de influência
(arquivos em source/_static/arquivos/entrega1/)
e monta a tabela de momentos (linhas = esforço, colunas = seção) com as combinações de ELU.

Unidades: kN, m, kN.m. Convenção: M > 0 traciona a fibra inferior.
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------ geometria
XA1, XA2, LTOT = 4.5, 29.5, 34.0          # apoios e comprimento total
L = XA2 - XA1                             # vão central = 25 m
DX = 0.001
XX = np.round(np.arange(0, LTOT + DX / 2, DX), 6)

SECOES = {                                # pontos de interesse (metade da ponte)
    "A esq": 4.5, "A dir": 4.5,           # apoio do balanço (momento contínuo)
    "B": 10.75,                           # 1/4 do vão
    "C": 17.0,                            # 1/2 do vão
}

# ------------------------------------------------------------------ cargas (Ftool)
G = 75.92                                 # kN/m, permanente distribuída (toda a viga)
F_PERM = [(0.0, 188.0),                   # F-BALANÇO (extremidade)
          (4.5, 39.19), (29.5, 39.19),    # F-APOIO (sobre os apoios)
          (17.0, 29.39),                  # F-VÃO (transversina do meio do vão)
          (34.0, 188.0)]

P = 239.36                                # kN por eixo, TB-450 com F_D (Entrega 1)
EIXOS = np.array([0.0, 1.5, 3.0])         # 3 eixos espaçados de 1,5 m
VEIC = (-1.5, 4.5)                        # veículo de 6 m (relativo ao 1º eixo)
Q_FORA = 34.53                            # kN/m, multidão fora do veículo
Q_SOB = 10.60                             # kN/m, multidão na região do veículo

GAMA_G_DESF, GAMA_G_FAV, GAMA_Q = 1.35, 1.00, 1.50   # NBR 8681 (pontes em geral)


def linha_influencia(xs):
    """LI de momento fletor na seção xs (carga unitária descendo ao longo de XX)."""
    rb = (XX - XA1) / L
    ra = 1.0 - rb
    m = np.zeros_like(XX)
    if xs >= XA1:
        m += ra * (xs - XA1)
    if xs >= XA2:
        m += rb * (xs - XA2)
    m -= np.where(XX < xs, xs - XX, 0.0)
    return m


def momento_permanente(xs):
    li = linha_influencia(xs)
    return G * np.trapezoid(li, XX) + sum(F * np.interp(x, XX, li) for x, F in F_PERM)


def envoltoria_trem_tipo(xs, passo=0.01):
    """Retorna {+1: (Mmax, x_1o_eixo), -1: (Mmin, x_1o_eixo)} varrendo o trem nos dois sentidos
    (o veículo é simétrico, então um sentido basta). A multidão é aplicada só onde a LI
    tem o sinal procurado: q' = Q_SOB na faixa do veículo e q = Q_FORA no restante."""
    li = linha_influencia(xs)
    x0 = np.round(np.arange(-6.0, LTOT + 6.0 + passo / 2, passo), 4)
    mp = sum(P * np.interp(x0 + e, XX, li, left=0.0, right=0.0) for e in EIXOS)
    out = {}
    for s in (+1, -1):
        f = np.where(s * li > 0, li, 0.0)                     # parte favorável da LI
        cum = np.concatenate([[0.0], np.cumsum((f[1:] + f[:-1]) / 2 * DX)])
        area_tot = cum[-1]
        a = np.interp(np.clip(x0 + VEIC[0], 0, LTOT), XX, cum)
        b = np.interp(np.clip(x0 + VEIC[1], 0, LTOT), XX, cum)
        area_veic = b - a
        tot = mp + Q_FORA * area_tot + (Q_SOB - Q_FORA) * area_veic
        i = np.argmax(s * tot)
        out[s] = (tot[i] if s * tot[i] > 0 else 0.0, x0[i])
    return out


def combinacoes(mg, mqmax, mqmin):
    g_max = GAMA_G_DESF if mg > 0 else GAMA_G_FAV
    g_min = GAMA_G_DESF if mg < 0 else GAMA_G_FAV
    return g_max * mg + GAMA_Q * mqmax, g_min * mg + GAMA_Q * mqmin


if __name__ == "__main__":
    # ---------------- tabela
    linhas = {"Mg": [], "Mq,máx": [], "Mq,mín": [], "Md,máx": [], "Md,mín": []}
    for nome, xs in SECOES.items():
        mg = momento_permanente(xs)
        env = envoltoria_trem_tipo(xs)
        mdmax, mdmin = combinacoes(mg, env[1][0], env[-1][0])
        for k, v in zip(linhas, (mg, env[1][0], env[-1][0], mdmax, mdmin)):
            linhas[k].append(v)
        print(f"{nome:6s} x={xs:6.2f}  1o eixo p/ Mmax: {env[1][1]:6.2f}  p/ Mmin: {env[-1][1]:6.2f}")
    print("\n| Momento (kN.m) | " + " | ".join(SECOES) + " |")
    print("|---|" + "---:|" * len(SECOES))
    for k, vals in linhas.items():
        print(f"| {k} | " + " | ".join(f"{v:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".") for v in vals) + " |")

    # ---------------- diagramas (meia ponte, 0 a 17 m)
    xs_plot = np.round(np.arange(0, 17.0001, 0.25), 3)
    mg_p, mx_p, mn_p = [], [], []
    for xs in xs_plot:
        mg_p.append(momento_permanente(xs))
        e = envoltoria_trem_tipo(xs, passo=0.05)
        mx_p.append(e[1][0]); mn_p.append(e[-1][0])
    mg_p, mx_p, mn_p = map(np.array, (mg_p, mx_p, mn_p))
    mdmax_p = np.where(mg_p > 0, GAMA_G_DESF, GAMA_G_FAV) * mg_p + GAMA_Q * mx_p
    mdmin_p = np.where(mg_p < 0, GAMA_G_DESF, GAMA_G_FAV) * mg_p + GAMA_Q * mn_p

    plt.rcParams.update({"font.size": 10, "axes.edgecolor": "#999999",
                         "axes.labelcolor": "#191919", "xtick.color": "#666666", "ytick.color": "#666666"})
    fig, axs = plt.subplots(2, 1, figsize=(9, 8), sharex=True)
    pares = [
        (axs[0], "Momentos característicos", [(mg_p, "Mg (permanente)", "#666666", "--"),
                                              (mx_p, "Mq,máx (trem-tipo)", "#257de0", "-"),
                                              (mn_p, "Mq,mín (trem-tipo)", "#f47230", "-")]),
        (axs[1], "Envoltória de cálculo (ELU)", [(mdmax_p, "Md,máx", "#257de0", "-"),
                                                 (mdmin_p, "Md,mín", "#f47230", "-")]),
    ]
    for ax, titulo, series in pares:
        for y, lab, cor, ls in series:
            ax.plot(xs_plot, y, color=cor, lw=2, ls=ls, label=lab)
        ax.axhline(0, color="#191919", lw=1)
        ax.invert_yaxis()                     # M positivo desenhado para baixo (como no Ftool)
        ax.grid(True, color="#e5e5e5", lw=0.8)
        ax.set_title(titulo, loc="left", fontsize=11, color="#191919")
        ax.set_ylabel("M (kN·m)")
        for s in ax.spines.values():
            s.set_visible(False)
        for nome, x in (("A", 4.5), ("B", 10.75), ("C", 17.0)):
            ax.axvline(x, color="#cccccc", lw=0.8, zorder=0)
            ax.annotate(nome, (x, 0), xytext=(4, -12), textcoords="offset points", color="#191919", fontweight="bold")
        ax.legend(frameon=False, loc="lower left")
    axs[1].set_xlabel("x (m) — origem na extremidade do balanço; C = meio do vão (eixo de simetria)")
    fig.tight_layout()
    saida = Path(__file__).resolve().parent.parent / "figuras" / "entrega2-envoltoria-momentos.png"
    saida.parent.mkdir(exist_ok=True)
    fig.savefig(saida, dpi=160)
    print(f"\nfigura salva: {saida}")

    # ---------------- ponto de inversão de Md,mín e combinação de fadiga
    for gg in (GAMA_G_FAV, GAMA_G_DESF):
        md = gg * mg_p + GAMA_Q * mn_p
        md_vao = np.where(xs_plot >= XA1, md, np.nan)
        i = np.where(np.diff(np.sign(md_vao)) != 0)[0]
        i = [k for k in i if not np.isnan(md_vao[k]) and not np.isnan(md_vao[k + 1])]
        x0 = [xs_plot[k] - md[k] * (xs_plot[k + 1] - xs_plot[k]) / (md[k + 1] - md[k]) for k in i]
        print(f"gama_g = {gg:.2f}: Md,min = 0 em x = {', '.join(f'{v:.2f}' for v in x0)} m")
    PSI1 = 0.5                                 # NBR 6118: vigas de pontes rodoviárias
    print("\nFadiga (Mg + 0,5 Mq):")
    for nome in ("A dir", "B", "C"):
        j = list(SECOES).index(nome)
        fmax = linhas["Mg"][j] + PSI1 * linhas["Mq,máx"][j]
        fmin = linhas["Mg"][j] + PSI1 * linhas["Mq,mín"][j]
        print(f"  {nome:6s} Mfad,max = {fmax:9.1f}  Mfad,min = {fmin:9.1f}  dM = {fmax - fmin:8.1f}")
