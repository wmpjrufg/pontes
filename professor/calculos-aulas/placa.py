"""Placa de Kirchhoff por diferenças finitas: superfície de influência de momentos.
Bordas: 'S' (apoiada) ou 'E' (engastada). x transversal (lx), y longitudinal (ly)."""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

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

if __name__ == '__main__':
    # Verificação 1: placa quadrada apoiada, carga uniforme, nu=0.3 -> mx centro = 0.0479 q a^2
    p = Placa(1.0, 1.0, 0.02, dict(x0='S',x1='S',y0='S',y1='S'), nu=0.3)
    eta = p.superficie(0.5, 0.5)
    print('SSSS uniforme: mx/qa2 =', eta.sum()*p.h**2, '(Timoshenko 0.0479)')
    # Verificação 2: carga concentrada central - comparação Navier
    # Verificação 3: faixa engastada longa ly/lx=4: mx borda ~ -1/12, centro ~ 1/24
    p2 = Placa(1.0, 4.0, 0.02, dict(x0='E',x1='E',y0='S',y1='S'), nu=0.2)
    e = p2.superficie(0.0+0.0, 2.0) if False else None
    eta_c = p2.superficie(0.5, 2.0); 
    print('EESS 1x4 centro mx/ql2 =', eta_c.sum()*p2.h**2, '(faixa: 0.04167)')
    # momento na borda engastada: avaliar no nó de borda i=0 requer tratamento: usar w_xx com fantasma
