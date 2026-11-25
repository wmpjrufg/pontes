"""
Superfície de influência de momentos em lajes de ponte (Aula 05 — Tabuleiro).

Calcula, por diferenças finitas (placa de Kirchhoff, D = 1), a superfície de influência
de m_x ou m_y num ponto da laje e procura a posição mais desfavorável do TB-450
(rodas distribuídas até a superfície média e multidão fora do veículo).

Uso: python superficie_influencia.py
Edite a seção "dados da ponte-exemplo" para a sua laje.
Bordas: 'E' = engastada, 'S' = simplesmente apoiada.
Requer numpy e scipy.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.ndimage import uniform_filter

class Placa:
    def __init__(self, lx, ly, h, bordas=dict(x0='E', x1='E', y0='S', y1='S'), nu=0.2):
        self.lx, self.ly, self.h, self.nu = lx, ly, h, nu
        self.nx, self.ny = int(round(lx/h)), int(round(ly/h))
        self.b = bordas
        n = (self.nx-1)*(self.ny-1)
        self.idx = -np.ones((self.nx+1, self.ny+1), int)
        k = 0
        for i in range(1, self.nx):
            for j in range(1, self.ny):
                self.idx[i, j] = k; k += 1
        self.n = n
        self.K = self._montar()
        self.lu = spla.splu(self.K.tocsc())
        self.KT = None

    def _ref(self, i, j):
        """Retorna lista de (indice, fator) para o ponto (i,j) que pode ser fantasma ou de borda."""
        nx, ny = self.nx, self.ny
        fat = 1.0
        # borda: w = 0
        if i in (0, nx) or j in (0, ny):
            if 0 <= i <= nx and 0 <= j <= ny:
                return []
        # fantasma além da borda x
        if i < 0:
            fat *= -1 if self.b['x0'] == 'S' else 1; i = -i
        if i > nx:
            fat *= -1 if self.b['x1'] == 'S' else 1; i = 2*nx - i
        if j < 0:
            fat *= -1 if self.b['y0'] == 'S' else 1; j = -j
        if j > ny:
            fat *= -1 if self.b['y1'] == 'S' else 1; j = 2*ny - j
        if i in (0, nx) or j in (0, ny):
            return []
        return [(self.idx[i, j], fat)]

    def _montar(self):
        st = {(0,0):20, (1,0):-8,(-1,0):-8,(0,1):-8,(0,-1):-8,
              (1,1):2,(1,-1):2,(-1,1):2,(-1,-1):2,
              (2,0):1,(-2,0):1,(0,2):1,(0,-2):1}
        r, c, v = [], [], []
        for i in range(1, self.nx):
            for j in range(1, self.ny):
                row = self.idx[i, j]
                for (di, dj), a in st.items():
                    for col, f in self._ref(i+di, j+dj):
                        r.append(row); c.append(col); v.append(a*f)
        return sp.csr_matrix((v, (r, c)), shape=(self.n, self.n)) / self.h**4

    def w(self, q):
        """q: carga por área nos nós internos (array nx-1 x ny-1). D=1."""
        return self.lu.solve(q.ravel())

    def vetor_momento(self, x, y, comp='mx'):
        """Vetor c tal que m = -D(w_xx + nu w_yy) = c.w (D=1)."""
        i, j = int(round(x/self.h)), int(round(y/self.h))
        c = np.zeros(self.n)
        nu = self.nu
        a, b = (1, nu) if comp == 'mx' else (nu, 1)
        terms = {(1,0):-a,(-1,0):-a,(0,0):2*a+2*b,(0,1):-b,(0,-1):-b}
        for (di, dj), val in terms.items():
            for col, f in self._ref(i+di, j+dj):
                c[col] += val*f/self.h**2
        return c

    def superficie(self, x, y, comp='mx'):
        """Superfície de influência (momento por carga unitária concentrada) em grade (nx-1, ny-1)."""
        c = self.vetor_momento(x, y, comp)
        if self.KT is None:
            self.KT = spla.splu(self.K.T.tocsc())
        eta = self.KT.solve(c) / self.h**2   # carga concentrada unitária = 1/h^2 por área no nó
        return eta.reshape(self.nx-1, self.ny-1)

    def coords(self):
        xs = np.arange(1, self.nx)*self.h
        ys = np.arange(1, self.ny)*self.h
        return np.meshgrid(xs, ys, indexing='ij')





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
    return (tot, mq, mp, (float(round((ic-pad+1)*H, 2)), float(round((jc-pad+1)*H, 2))))

res = {}
for nome, (x, y, comp, sinal) in {'mx_vao': (2.5, 5.0, 'mx', +1), 'my_vao': (2.5, 5.0, 'my', +1),
                                  'mx_engaste': (0.0, 5.0, 'mx', -1)}.items():
    eta = placa.superficie(x, y, comp)
    mg = g*eta.sum()*H*H
    tot, mq, mp, pos = tb450(eta, sinal)
    res[nome] = (mg, tot, mq, mp, pos)
    print(f"{nome:11s} Mg={mg:7.2f}  Mq(sem phi)={tot:7.2f} [rodas {mq:7.2f} + multidão {mp:6.2f}]  centro veículo={pos}  Mq*phi={phi*tot:7.2f} kNm/m")
