import numpy as np
from secao_circular import As_nec, MRd
m = np.load('meso.npy', allow_pickle=True).item()
Le = m['Le']
fcd = 30/1.4*1000; fyd = 500/1.15*1000
D = 1.20; Ac = np.pi*D**2/4; Hp = 7.0
Ng_sup, Nq = 900.0, 650.0
Wp = 25*Ac*Hp
Hfr, Ht, Hv = m['Hfren']['P2'], m['Htemp']['P2'], m['Hvento']['P2']
Mfr, Mt, Mv = Hfr*Hp, Ht*Hp, Hv*Hp
print(f"Wpilar={Wp:.1f} ; Mfren={Mfr:.1f} Mtemp={Mt:.1f} Mret={Mt:.1f} Mvento={Mv:.1f}")
combs = {}
Nd1 = 1.35*(Ng_sup+Wp) + 1.5*Nq
Mx1 = 1.5*(Mfr + 0.6*Mt) + 1.2*Mt; My1 = 1.5*0.6*Mv
Nd2 = 1.35*(Ng_sup+Wp) + 1.5*0.7*Nq
Mx2 = 1.5*(0.7*Mfr + 0.6*Mt) + 1.2*Mt; My2 = 1.5*Mv
for nome, Nd, Mx, My in [('C1 tráfego principal', Nd1, Mx1, My1), ('C2 vento principal', Nd2, Mx2, My2)]:
    M1 = np.hypot(Mx, My)
    l = Hp + Le; le = 2*l; i = D/4; lam = le/i
    e1 = M1/Nd; ab = 0.9
    lam1 = min(max((25+12.5*e1/D)/ab, 35), 90)
    M1min = Nd*(0.015+0.03*D)
    M1A = max(M1, M1min)
    nu = Nd/(Ac*fcd)
    r1 = min(0.005/(D*(nu+0.5)), 0.005/D)
    M2 = Nd*le**2/10*r1
    Mtot = max(ab*M1A + M2, M1A)
    As = As_nec(D, Nd, Mtot, fcd)
    print(f"{nome}: Nd={Nd:.1f} Mx={Mx:.1f} My={My:.1f} M1d={M1:.1f} | l={l:.2f} le={le:.2f} lam={lam:.1f} lam1={lam1:.1f} e1={e1:.3f} M1min={M1min:.1f} nu={nu:.4f} 1/r={r1:.6f} M2d={M2:.1f} Mtot={Mtot:.1f} mu={Mtot/(Ac*D*fcd):.4f} As_nec={As*1e4:.1f} cm2")
Asmin = max(0.15*Nd1/fyd, 0.004*Ac)*1e4
print(f"As,min={Asmin:.1f} cm2 ; As,max={0.08*Ac*1e4:.0f} cm2")
for nb, ph in [(24, 0.016), (20, 0.020)]:
    As = nb*np.pi*ph**2/4
    print(f"{nb} phi{ph*1000:.0f}: As={As*1e4:.1f} cm2 ; MRd(Nd1)={MRd(D, As, Nd1, fcd):.0f} kNm")
