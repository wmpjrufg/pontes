import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
from placa import Placa
BLUE, ORANGE, AQUA, GRAY, INK, LIGHT = '#257de0', '#f47230', '#00b894', '#666666', '#191919', '#e5e5e5'
plt.rcParams.update({'font.size': 10, 'axes.edgecolor': '#999999', 'axes.labelcolor': INK,
                     'xtick.color': GRAY, 'ytick.color': GRAY, 'font.family': 'DejaVu Sans'})
def br(v, n=2):
    return f'{v:.{n}f}'.replace('.', ',')
def clean(ax):
    for s in ax.spines.values(): s.set_visible(False)

# ---------------- Aula 05: planta das lajes
fig, ax = plt.subplots(figsize=(9, 4.2))
W = 9.4; Lp = 28.0
ax.add_patch(Rectangle((0, 0), Lp, W, fc='#f6f6f6', ec=GRAY, lw=1))
for yv, lab in [(2.2, 'Longarina 1'), (7.2, 'Longarina 2')]:
    ax.add_patch(Rectangle((0, yv-0.2), Lp, 0.4, fc='#d9d9d9', ec=GRAY, lw=0.8))
    ax.text(0.3, yv+0.3, lab, fontsize=8, color=GRAY)
for xv, lab in [(4.0, 'T. apoio'), (14.0, 'T. vão'), (24.0, 'T. apoio')]:
    ax.add_patch(Rectangle((xv-0.15, 2.2), 0.3, 5.0, fc='#d9d9d9', ec=GRAY, lw=0.8))
    ax.text(xv, 7.55, lab, ha='center', fontsize=8, color=GRAY)
ax.add_patch(Rectangle((4.0, 2.2), 10.0, 5.0, fc=BLUE, alpha=0.18, ec=BLUE, lw=1.5))
ax.text(9.0, 4.7, 'L1 — laje central\n$\\ell_x$ = 5,00 m  ×  $\\ell_y$ = 10,00 m', ha='center', va='center', color=INK)
ax.add_patch(Rectangle((0, 7.4), Lp, 2.0, fc=ORANGE, alpha=0.18, ec=ORANGE, lw=1.5))
ax.add_patch(Rectangle((0, 0), Lp, 2.0, fc=ORANGE, alpha=0.18, ec=ORANGE, lw=1.5))
ax.text(19.0, 8.4, 'L2 — laje em balanço (bordo)', ha='center', va='center', color=INK)
ax.text(19.0, 1.0, 'L2 — laje em balanço (bordo)', ha='center', va='center', color=INK)
ax.annotate('', xy=(29.2, 0), xytext=(29.2, W), arrowprops=dict(arrowstyle='<->', color=GRAY))
ax.text(29.5, W/2, '9,40 m', va='center', color=GRAY, fontsize=9)
ax.annotate('tráfego', xy=(27, -0.9), xytext=(22, -0.9), arrowprops=dict(arrowstyle='->', color=INK), va='center', color=INK, fontsize=9)
ax.set_xlim(-0.5, 31); ax.set_ylim(-1.5, 10); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout(); fig.savefig('fig/tab-planta-lajes.png', dpi=160)

# ---------------- Aula 05: superfícies de influência
H = 0.05
pl = Placa(5.0, 10.0, H, dict(x0='E', x1='E', y0='S', y1='S'), nu=0.2)
X, Y = pl.coords()
fig, axs = plt.subplots(1, 2, figsize=(9.5, 5.6), sharey=True)
for ax, (x0, y0, tit, veh) in zip(axs, [(2.5, 5.0, '$m_x$ no centro (vão)', (3.45, 5.0)),
                                        (0.0, 5.0, '$m_x$ no engaste (borda x = 0)', (1.80, 5.0))]):
    eta = pl.superficie(x0, y0, 'mx')
    lim = np.max(np.abs(eta))
    cs = ax.contourf(X, Y, eta, levels=np.linspace(-lim, lim, 25), cmap='RdBu_r')
    ax.contour(X, Y, eta, levels=[0], colors=INK, linewidths=0.8)
    xc, yc = veh
    ax.add_patch(Rectangle((xc-1.5, yc-3.0), 3.0, 6.0, fill=False, ec=INK, ls='--', lw=1))
    for dx in (-1, 1):
        for dy in (-1.5, 0, 1.5):
            ax.add_patch(Rectangle((xc+dx-0.44, yc+dy-0.29), 0.88, 0.58, fc=ORANGE, ec=INK, lw=0.6))
    ax.plot([x0], [y0], marker='x', color=INK, ms=9, mew=2)
    ax.set_title(tit, loc='left', fontsize=10, color=INK)
    ax.set_xlim(0, 5); ax.set_ylim(0, 10); ax.set_aspect('equal'); ax.set_xlabel('x (m)')
axs[0].set_ylabel('y (m) — direção do tráfego')
cb = fig.colorbar(cs, ax=axs, shrink=0.8, label='ordenada (sinal: vermelho +, azul −)')
cb.set_ticks([])
fig.savefig('fig/tab-superficies-influencia.png', dpi=160, bbox_inches='tight')

# ---------------- Aula 05: balanço — distribuição a 45° e sobreposição
fig, ax = plt.subplots(figsize=(6.8, 6.2))
x = 1.10; bef = 2.805; b1r = 0.605; b2r = 0.88
ax.add_patch(Rectangle((0, -4.2), 2.0, 8.4, fc='#f6f6f6', ec='none'))
for k, yc in enumerate((-1.5, 0, 1.5)):
    ax.add_patch(Polygon([[x, yc-b1r/2], [x, yc+b1r/2], [0, yc+bef/2], [0, yc-bef/2]], closed=True,
                         fc=BLUE, alpha=0.13, ec=BLUE, lw=0.8))
    ax.add_patch(Rectangle((x-b2r/2, yc-b1r/2), b2r, b1r, fc=ORANGE, ec=INK, lw=0.6, alpha=0.9))
ax.plot([0, 0], [-4.2, 4.2], color=INK, lw=2.5)
ax.text(-0.08, 3.7, 'face da longarina\n(engaste)', ha='right', fontsize=8, color=GRAY)
ax.add_patch(Rectangle((1.6, -4.2), 0.4, 8.4, fc='#d9d9d9', ec=GRAY))
ax.text(1.8, 3.7, 'barreira', ha='center', fontsize=8, color=INK, rotation=90)
ax.annotate('', xy=(-0.25, -1.5-bef/2), xytext=(-0.25, 1.5+bef/2), arrowprops=dict(arrowstyle='<->', color=INK))
ax.text(-0.32, 0, 'largura conjunta\n2·1,50 + 2,81\n= 5,81 m', ha='right', va='center', fontsize=8, color=INK)
ax.annotate('', xy=(0, -3.6), xytext=(x, -3.6), arrowprops=dict(arrowstyle='<->', color=GRAY))
ax.text(x/2, -3.95, 'x = 1,10 m', ha='center', fontsize=8, color=GRAY)
ax.text(x+0.5, 0, 'rodas\n(área $b_2$ × $b_1$)', fontsize=8, color=INK, va='center')
ax.set_xlim(-1.6, 2.6); ax.set_ylim(-4.3, 4.3); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('Planta do balanço: alinhamento externo de rodas\ne distribuição a 45° até o engaste', loc='left', fontsize=10, color=INK)
fig.tight_layout(); fig.savefig('fig/tab-balanco-distribuicao.png', dpi=160)

# ---------------- Aula 06: áreas de influência + trem-tipo da transversina
fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw=dict(width_ratios=[1.3, 1]))
ax = axs[0]
ax.add_patch(Rectangle((0, 0), 20, 5, fc='#f6f6f6', ec=GRAY))
ax.plot([10, 10], [0, 5], color=INK, lw=3)
ax.add_patch(Polygon([[10, 0], [10, 5], [7.5, 2.5]], fc=AQUA, alpha=0.35, ec=AQUA))
ax.add_patch(Polygon([[10, 0], [10, 5], [12.5, 2.5]], fc=AQUA, alpha=0.35, ec=AQUA))
for (a, b) in [((0, 0), (2.5, 2.5)), ((0, 5), (2.5, 2.5)), ((20, 0), (17.5, 2.5)), ((20, 5), (17.5, 2.5)),
               ((10, 0), (7.5, 2.5)), ((10, 5), (7.5, 2.5)), ((10, 0), (12.5, 2.5)), ((10, 5), (12.5, 2.5))]:
    ax.plot([a[0], b[0]], [a[1], b[1]], color=GRAY, lw=0.8, ls='--')
ax.plot([2.5, 7.5], [2.5, 2.5], color=GRAY, lw=0.8, ls='--'); ax.plot([12.5, 17.5], [2.5, 2.5], color=GRAY, lw=0.8, ls='--')
ax.text(10.2, 5.25, 'transversina de vão', fontsize=8, color=INK)
ax.text(5, -0.6, '$\\ell_y$ = 10,00 m', ha='center', fontsize=8, color=GRAY); ax.text(15, -0.6, '$\\ell_y$ = 10,00 m', ha='center', fontsize=8, color=GRAY)
ax.set_title('Área de influência por bissetrizes', loc='left', fontsize=10, color=INK)
ax.set_xlim(-0.5, 20.5); ax.set_ylim(-1.2, 6); ax.set_aspect('equal'); ax.axis('off')
ax = axs[1]
yy = np.linspace(-10, 10, 201); eta = np.maximum(0, 1-np.abs(yy)/10)
ax.fill_between(yy, 0, eta, color=BLUE, alpha=0.15); ax.plot(yy, eta, color=BLUE, lw=2)
for yv in (-1.5, 0, 1.5):
    e = 1-abs(yv)/10
    ax.annotate('', xy=(yv, e), xytext=(yv, e+0.45), arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
    ax.text(yv, e+0.5, br(e), ha='center', fontsize=8, color=INK)
ax.axvspan(-3, 3, color=ORANGE, alpha=0.08)
ax.text(0, -0.15, 'veículo (6 m)', ha='center', fontsize=8, color=GRAY)
ax.set_title('LI longitudinal da reação na transversina', loc='left', fontsize=10, color=INK)
ax.set_xlabel('y (m) — distância à transversina'); ax.set_ylim(-0.25, 1.75); ax.set_yticks([0, 1]); clean(ax)
fig.tight_layout(); fig.savefig('fig/tra-areas-trem-tipo.png', dpi=160)

# ---------------- Aula 07: modelo pilar + neoprene + engaste fictício e distribuição
m = np.load('meso.npy', allow_pickle=True).item()
fig, axs = plt.subplots(1, 2, figsize=(10, 4.6), gridspec_kw=dict(width_ratios=[1, 1.4]))
ax = axs[0]
ax.add_patch(Rectangle((-0.6, 0), 1.2, 7.0, fc='#d9d9d9', ec=GRAY))
ax.add_patch(Rectangle((-0.7, -m['Le']), 1.4, m['Le'], fc='#eeeeee', ec=GRAY, ls='--'))
ax.add_patch(Rectangle((-0.45, 7.0), 0.9, 0.25, fc='#333333', ec=INK))
ax.plot([-2.2, 2.2], [0, 0], color='#8a6d3b', lw=2); ax.text(1.0, 0.15, 'terreno', fontsize=8, color='#8a6d3b')
ax.plot([-1.1, 1.1], [-m['Le'], -m['Le']], color=INK, lw=3)
for xh in np.linspace(-1.0, 1.0, 9):
    ax.plot([xh, xh-0.2], [-m['Le'], -m['Le']-0.3], color=INK, lw=0.8)
ax.annotate('', xy=(0.45, 7.35), xytext=(2.0, 7.35), arrowprops=dict(arrowstyle='<-', color=ORANGE, lw=2))
ax.text(2.05, 7.35, 'H', va='center', color=ORANGE)
ax.text(0.75, 3.5, '$H_p$ = 7,00 m\n(pilar Ø 1,20 m)', fontsize=8, color=INK)
ax.text(0.8, -m['Le']/2, "$L_e$ = 1,8T = "+br(m['Le'])+" m\n(tubulão Ø 1,40 m)", fontsize=8, color=INK)
ax.text(-0.45, 7.45, 'neoprene', fontsize=8, color=GRAY, ha='right')
ax.set_xlim(-2.5, 3.2); ax.set_ylim(-m['Le']-0.8, 8.2); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('Modelo de cálculo do apoio elástico', loc='left', fontsize=10, color=INK)
ax = axs[1]
ax.plot([0, 28], [0, 0], color=INK, lw=4)
for p, xp in [('P1', 4.0), ('P2', 24.0)]:
    ax.plot([xp, xp], [0, -2.2 if p == 'P1' else -2.6], color=GRAY, lw=6, solid_capstyle='butt')
    ax.text(xp, -3.1, f"{p}\nK = {m['K'][p]:.0f} kN/m\n(por pilar)", ha='center', va='top', fontsize=8, color=INK)
ax.plot([m['x0']], [0], marker='v', color=ORANGE, ms=11)
ax.text(m['x0'], 0.45, "ponto indeslocável\n$x_0$ = "+br(m['x0'])+" m", ha='center', fontsize=8, color=ORANGE)
ax.annotate('', xy=(4.0, 1.6), xytext=(m['x0'], 1.6), arrowprops=dict(arrowstyle='<-', color=BLUE))
ax.annotate('', xy=(24.0, 1.6), xytext=(m['x0'], 1.6), arrowprops=dict(arrowstyle='<-', color=BLUE))
ax.text(9, 1.8, 'encurtamento (−ΔT, retração)', fontsize=8, color=BLUE, ha='center')
ax.set_xlim(-1, 29); ax.set_ylim(-6, 3); ax.axis('off')
ax.set_title('Rigidez dos apoios e centro de rigidez longitudinal', loc='left', fontsize=10, color=INK)
fig.tight_layout(); fig.savefig('fig/meso-modelo-rigidez.png', dpi=160)

# ---------------- Aula 08: curva de interação da seção do pilar
from secao_circular import NM_resist
D = 1.2; fcd = 30/1.4*1000
fig, ax = plt.subplots(figsize=(6.8, 5))
for As, cor, lab in [(48.3e-4, BLUE, '24 Ø16 (48,3 cm²)'), (0.0, GRAY, 'concreto simples')]:
    pts = [NM_resist(D, As, x, fcd) for x in np.linspace(0.02, 6.0, 400)]
    N = [p_[0] for p_ in pts]; M = [p_[1] for p_ in pts]
    ax.plot(M, N, color=cor, lw=2, label=lab)
ax.plot([1038.3], [2457.2], 'o', color=ORANGE, ms=8, label='C1: $N_d$ = 2457 kN; $M_{d,tot}$ = 1038 kN·m')
ax.plot([945.9], [2164.7], 's', color=AQUA, ms=8, label='C2: $N_d$ = 2165 kN; $M_{d,tot}$ = 946 kN·m')
ax.set_xlabel('$M_{Rd}$ (kN·m)'); ax.set_ylabel('$N_{Rd}$ (kN, compressão +)')
ax.set_xlim(0, None); ax.set_ylim(0, None); ax.grid(color=LIGHT); clean(ax)
ax.legend(frameon=False, fontsize=8, loc='upper right')
ax.set_title('Diagrama de interação N–M da seção circular Ø 1,20 m', loc='left', fontsize=10, color=INK)
fig.tight_layout(); fig.savefig('fig/pil-interacao.png', dpi=160)

# ---------------- Aula 09: tubulão geometria + M(z)
z, Mz, yz = np.load('tub_M.npy')
fig, axs = plt.subplots(1, 2, figsize=(10, 5.4), gridspec_kw=dict(width_ratios=[1, 1.1]))
ax = axs[0]
Df, Db, hb = 1.40, 2.20, 0.693
ax.add_patch(Polygon([[-Df/2, 0], [Df/2, 0], [Df/2, -8+0.2+hb], [Db/2, -8+0.2], [Db/2, -8], [-Db/2, -8], [-Db/2, -8+0.2], [-Df/2, -8+0.2+hb]],
                     closed=True, fc='#d9d9d9', ec=GRAY))
ax.plot([-3, 3], [0, 0], color='#8a6d3b', lw=2)
ax.annotate('', xy=(Db/2+0.35, -8), xytext=(Db/2+0.35, -8+0.2), arrowprops=dict(arrowstyle='<->', color=GRAY))
ax.text(Db/2+0.45, -7.95, 'rodapé 20 cm', fontsize=8, color=GRAY)
ax.text(Df/2+0.15, -7.4+0.2, 'β = 60°', fontsize=8, color=INK)
ax.text(0, -8.45, '$D_b$ = '+br(Db)+' m', ha='center', fontsize=8, color=INK)
ax.text(Df/2+0.15, -3.5, '$D_f$ = 1,40 m\nfuste', fontsize=8, color=INK)
ax.annotate('', xy=(-Db/2-0.4, -8), xytext=(-Db/2-0.4, -8+0.2+hb), arrowprops=dict(arrowstyle='<->', color=GRAY))
ax.text(-Db/2-0.5, -7.55, '$H_b$ = 0,89 m\n(≤ 1,80 m)', ha='right', fontsize=8, color=GRAY)
ax.set_xlim(-3.2, 3.2); ax.set_ylim(-8.8, 0.6); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('Geometria do tubulão do exemplo', loc='left', fontsize=10, color=INK)
ax = axs[1]
ax.plot(Mz, -z, color=BLUE, lw=2, label='Winkler ($E_s = n_h z$)')
Le = 1.8*((26.84e6*np.pi*1.4**4/64)/17600)**0.2
H0, M0 = 42.0, 293.7
zz = np.linspace(0, Le, 50)
ax.plot(M0 + H0*zz, -zz, color=ORANGE, lw=2, ls='--', label='engaste fictício ($L_e$ = '+br(Le)+' m)')
ax.axvline(0, color=INK, lw=0.8)
ax.set_xlabel('M (kN·m)'); ax.set_ylabel('profundidade (m)'); ax.grid(color=LIGHT); clean(ax)
ax.legend(frameon=False, fontsize=8, loc='lower right')
ax.set_title('Momento fletor ao longo do fuste (valores característicos)', loc='left', fontsize=10, color=INK)
fig.tight_layout(); fig.savefig('fig/tub-geometria-momento.png', dpi=160)
print('ok')
