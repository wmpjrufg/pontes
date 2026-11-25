"""
Tubulão sob força horizontal e momento no topo (Aula 09 — Fundações em tubulão).

Modelo de Winkler com módulo de reação crescente com a profundidade (Es = nh * z),
resolvido por diferenças finitas. Base livre (sem restrição à rotação).

Uso: python winkler_tubulao.py   (edite os dados abaixo). Requer numpy.
"""
import numpy as np

# ---------------- dados (exemplo da Aula 09)
E = 26.84e6          # kN/m2
D = 1.40             # diâmetro do fuste (m)
L = 8.0              # comprimento do fuste abaixo do terreno (m)
nh = 17600.0         # kN/m3 (areia compacta, Terzaghi)
H0 = 42.0            # força horizontal no topo do tubulão (kN)
M0 = 293.7           # momento no topo do tubulão (kN.m)

EI = E*np.pi*D**4/64
T = (EI/nh)**0.2
n = 400; dz = L/n; z = np.linspace(0, L, n+1)
N = n+5; o = 2
A = np.zeros((N, N)); b = np.zeros(N)
for i in range(n+1):
    r = i+o
    A[r, r-2:r+3] += EI*np.array([1, -4, 6, -4, 1])/dz**4
    A[r, r] += nh*z[i]
A[0, o-1:o+2] = EI*np.array([1, -2, 1])/dz**2; b[0] = -M0
A[1, o-2:o+3] = EI*np.array([-1, 2, 0, -2, 1])/(2*dz**3); b[1] = -H0
r = n+o
A[N-2, r-1:r+2] = EI*np.array([1, -2, 1])/dz**2
A[N-1, r-2:r+3] = EI*np.array([-1, 2, 0, -2, 1])/(2*dz**3)
y = np.linalg.solve(A, b)
M = np.array([-EI*(y[i+o-1]-2*y[i+o]+y[i+o+1])/dz**2 for i in range(n+1)])
k = np.argmax(np.abs(M))
print(f"T = {T:.2f} m ; L/T = {L/T:.2f} ; engaste fictício Le = 1,8T = {1.8*T:.2f} m")
print(f"deslocamento no topo = {abs(y[o])*1000:.2f} mm")
print(f"momento máximo = {abs(M[k]):.1f} kN.m a {z[k]:.2f} m de profundidade")
for i in range(0, n+1, n//8):
    print(f"  z = {z[i]:5.2f} m   M = {M[i]:8.1f} kN.m   p = {nh*z[i]*abs(y[i+o]):7.1f} kN/m")
