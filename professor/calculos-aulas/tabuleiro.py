import numpy as np
from scipy.ndimage import uniform_filter
from placa import Placa

H = 0.05
# ---------------- dados da ponte-exemplo
lx, ly = 5.00, 10.00          # laje central: entre eixos de longarinas x entre transversinas
h_laje, e_asf = 0.22, 0.08
g1 = 25*h_laje; g2 = 24*e_asf + 2.0; g = g1 + g2
P = 75.0; p = 5.0
CIV = 1.35; CIA = 1.25; phi = CIV*CIA
b1 = 0.20 + 2*e_asf + h_laje     # direção do tráfego (y)
b2 = 0.50 + 2*e_asf + h_laje     # transversal (x)
print(f"g1={g1:.2f} g2={g2:.2f} g={g:.2f} kN/m2 ; phi={phi:.4f} ; b1={b1:.2f} b2={b2:.2f}")

placa = Placa(lx, ly, H, dict(x0='E', x1='E', y0='S', y1='S'), nu=0.2)
X, Y = placa.coords()

def tb450(eta, sinal):
    """Máximo (sinal=+1) ou mínimo (-1) do momento devido ao TB-450 (P=75 kN, p=5) sem impacto.
    Retorna (M_rodas, M_multidao, posição)."""
    nx, ny = eta.shape
    # média da superfície sobre a área de contato distribuída (b2 em x, b1 em y)
    kx, ky = int(round(b2/H)), int(round(b1/H))
    eta_p = uniform_filter(eta, size=(kx, ky), mode='constant')
    fav = np.where(sinal*eta > 0, eta, 0.0)
    fav_tot = fav.sum()*H*H
    fx, fy = int(round(3.0/H)), int(round(6.0/H))
    fav_fp = uniform_filter(fav, size=(fx, fy), mode='constant')*fx*fy*H*H  # integral no retângulo centrado
    # rodas relativas ao centro do veículo: x = ±1.0 ; y = 0, ±1.5
    offs = [(dx, dy) for dx in (-1.0, 1.0) for dy in (-1.5, 0.0, 1.5)]
    pad = 160
    E = np.pad(eta_p, pad); F = np.pad(fav_fp, pad)
    NX, NY = E.shape
    S = np.zeros_like(E)
    for dx, dy in offs:
        S += np.roll(np.roll(E, -int(round(dx/H)), axis=0), -int(round(dy/H)), axis=1)
    TOT = P*S + p*(fav_tot - F)
    k = np.argmax(sinal*TOT)
    ic, jc = np.unravel_index(k, TOT.shape)
    tot = TOT[ic, jc]; mq = P*S[ic, jc]; mp = p*(fav_tot - F[ic, jc])
    return (tot, mq, mp, (round((ic-pad+1)*H, 2), round((jc-pad+1)*H, 2)))

res = {}
for nome, (x, y, comp, sinal) in {'mx_vao': (2.5, 5.0, 'mx', +1), 'my_vao': (2.5, 5.0, 'my', +1),
                                  'mx_engaste': (0.0, 5.0, 'mx', -1)}.items():
    eta = placa.superficie(x, y, comp)
    mg = g*eta.sum()*H*H
    tot, mq, mp, pos = tb450(eta, sinal)
    res[nome] = (mg, tot, mq, mp, pos)
    print(f"{nome:11s} Mg={mg:7.2f}  Mq(sem phi)={tot:7.2f} [rodas {mq:7.2f} + multidão {mp:6.2f}]  centro veículo={pos}  Mq*phi={phi*tot:7.2f} kNm/m")
np.save('res_tab.npy', res, allow_pickle=True)
