import numpy as np
from secao_circular import As_nec, MRd
m = np.load('meso.npy', allow_pickle=True).item()
Ec = 26.84e6; nh = 17600.0
Df = 1.40; If = np.pi*Df**4/64; EI = Ec*If; Af = np.pi*Df**2/4
Lt = 8.0; Hp = 7.0
T = (EI/nh)**0.2
# esforços característicos no topo do tubulão (P2), combinação característica: tráfego principal
Hx = m['Hfren']['P2'] + 0.6*m['Htemp']['P2'] + m['Htemp']['P2']
Hy = 0.6*m['Hvento']['P2']
H0 = np.hypot(Hx, Hy); M0 = H0*Hp
N_top = 900 + 25*np.pi*0.6**2*Hp + 650
print(f"T={T:.2f} m ; Lt/T={Lt/T:.2f} ; H0={H0:.1f} kN ; M0={M0:.1f} kNm ; N topo={N_top:.1f} kN")
# viga de Winkler por diferenças finitas: EI y'''' + nh z y = 0, topo: M=-EI y''=M0 (sinal), V=H0 ; base livre
n = 400; dz = Lt/n; z = np.linspace(0, Lt, n+1)
N = n+1+4  # 2 fantasmas em cada extremidade
A = np.zeros((N, N)); b = np.zeros(N)
o = 2
for i in range(n+1):
    r = i+o
    A[r, r-2:r+3] += EI*np.array([1, -4, 6, -4, 1])/dz**4
    A[r, r] += nh*z[i]
# condições de contorno no topo (i=0): EI y'' = -M0 ; EI y''' = -H0 (convenção: y positivo no sentido de H)
A[0, o-1:o+2] = EI*np.array([1, -2, 1])/dz**2; b[0] = -M0
A[1, o-2:o+3] = EI*np.array([-1, 2, 0, -2, 1])/(2*dz**3); b[1] = -H0
# base livre (M=0, V=0)
r = n+o
A[N-2, r-1:r+2] = EI*np.array([1, -2, 1])/dz**2
A[N-1, r-2:r+3] = EI*np.array([-1, 2, 0, -2, 1])/(2*dz**3)
y = np.linalg.solve(A, b)
yy = y[o:n+1+o]
Mz = np.array([-EI*(y[i+o-1]-2*y[i+o]+y[i+o+1])/dz**2 for i in range(n+1)])
k = np.argmax(np.abs(Mz))
print(f"desloc. topo={yy[0]*1000:.2f} mm ; |M|max={abs(Mz[k]):.1f} kNm a z={z[k]:.2f} m ; M base={Mz[-1]:.2f}")
print("M(z) amostras:", [(round(z[i],1), round(Mz[i],1)) for i in range(0, n+1, 50)])
np.save('tub_M.npy', np.vstack([z, Mz, yy]))
# verificação: modelo de engaste fictício a Le=1,8T -> momento no engaste
Le = 1.8*T
print(f"engaste fictício: M = M0 + H0*Le = {M0 + H0*Le:.1f} kNm (Winkler: {abs(Mz[k]):.1f})")
# ---------- geotecnia: base
sig_adm = 600.0
W_f = 25*Af*Lt
for Db in [2.10, 2.20, 2.30]:
    hb = (Db-Df)/2*np.tan(np.radians(60)); Hb = hb + 0.20
    Vb = np.pi*hb/3*((Db/2)**2 + (Db/2)*(Df/2) + (Df/2)**2) + np.pi*Db**2/4*0.20 - Af*Hb
    Wb = 25*Vb
    Nb = N_top + W_f + Wb
    Ab = np.pi*Db**2/4; Wm = np.pi*Db**3/32
    s = Nb/Ab
    print(f"Db={Db:.2f}: hb={hb:.3f} Hb={Hb:.3f} m ; peso fuste={W_f:.0f} base(acresc.)={Wb:.0f} ; N base={Nb:.0f} kN ; sigma={s:.0f} kPa (adm {sig_adm:.0f}) ; Mbase/W = {abs(Mz[-1])/Wm:.1f}")
# ---------- estrutural do fuste (NBR 6122: C40, gama_c=3,6 para CAA III ; gama_f=1,4)
fck = 40e3; gc = 3.6; fcd = fck/gc
Nd = 1.4*N_top; Md = 1.4*abs(Mz[k])
print(f"fcd={fcd/1000:.2f} MPa ; tensão média caract.={N_top/Af/1000:.2f} MPa (limite p/ dispensa de armadura 5,0 MPa)")
print(f"Nd={Nd:.0f} ; Md={Md:.0f} ; MRd concreto simples={MRd(Df,0,Nd,fcd):.0f} ; As_nec={As_nec(Df,Nd,Md,fcd)*1e4:.1f} cm2")
