import numpy as np
np.set_printoptions(precision=3, suppress=True)
Ec = 26.84e6          # kN/m2 (Ecs C30)
alpha = 1e-5
# ---------------- geometria ponte-exemplo
L_total = 28.0; x_ap = {'P1': 4.0, 'P2': 24.0}
Hp = {'P1': 6.0, 'P2': 7.0}; Dp = 1.20
Df = 1.40; nh = 17600.0   # kN/m3 (areia compacta, Terzaghi)
G_neo = 1000.0; A_neo = 0.40*0.50; t_neo = 0.050
B_pista = 8.60
Ip = np.pi*Dp**4/64; It = np.pi*Df**4/64
EIp, EIt = Ec*Ip, Ec*It
T = (EIt/nh)**0.2; Le = 1.8*T
print(f"Ip={Ip:.4f} It={It:.4f} T={T:.2f} m Le=1,8T={Le:.2f} m")
K_neo = G_neo*A_neo/t_neo
def flex_pilar(H):
    # console com dois trechos: pilar (H, EIp) sobre trecho fictício do tubulão (Le, EIt)
    a, b = H, Le
    return a**3/(3*EIp) + (b**3 + 3*b**2*a + 3*b*a**2)/(3*EIt)
K = {}
for p in Hp:
    fp = flex_pilar(Hp[p]); f0 = Hp[p]**3/(3*EIp)
    K[p] = 1/(fp + 1/K_neo)
    print(f"{p}: H={Hp[p]} K_pilar(engaste fictício)={1/fp:.0f} (engaste no topo do tubulão: {1/f0:.0f}) K_neo={K_neo:.0f} K_conj={K[p]:.0f} kN/m")
# 2 pilares por apoio
Ksum = 2*sum(K.values())
Hf = max(0.25*B_pista*L_total*1.0, 135.0)
print(f"Hf = max(0,25*{B_pista}*{L_total}={0.25*B_pista*L_total:.1f}; 135) = {Hf:.1f} kN")
Hfren = {p: Hf*K[p]/Ksum for p in K}
x0 = sum(2*K[p]*x_ap[p] for p in K)/Ksum
print("frenagem por pilar:", {p: round(v, 2) for p, v in Hfren.items()}, f"; ponto indeslocável x0={x0:.2f} m")
Htemp = {p: K[p]*alpha*15*abs(x_ap[p]-x0) for p in K}
Hret = Htemp  # retração equivalente a -15 °C
for p in K:
    print(f"{p}: dist={abs(x_ap[p]-x0):.2f} m desloc={alpha*15*abs(x_ap[p]-x0)*1000:.2f} mm H_temp={Htemp[p]:.2f} kN H_ret={Hret[p]:.2f} kN")
# vento transversal (processo simplificado tradicional)
h_sup, h_barr = 1.80, 0.87
w_desc = 1.5*(h_sup+h_barr); w_carr = 1.0*(h_sup+2.0)
w = max(w_desc, w_carr)
W_tot = w*L_total
print(f"vento: descarregada {w_desc:.2f} kN/m ; carregada {w_carr:.2f} kN/m -> W total={W_tot:.1f} kN")
Hv_trans = {p: W_tot*K[p]/Ksum for p in K}
e = L_total/2 - x0
Mt = W_tot*e
Ikx = sum(2*K[p]*(x_ap[p]-x0)**2 for p in K)
dH = {p: Mt*K[p]*(x_ap[p]-x0)/Ikx for p in K}
Hvento = {p: Hv_trans[p] + dH[p] for p in K}
print(f"vento: translação {Hv_trans} ; e={e:.2f} m ; Mt={Mt:.1f} kNm ; sum K x2={Ikx:.0f} ; dH={dH}")
print("vento por pilar (translação + rotação):", {p: round(v, 2) for p, v in Hvento.items()})
np.save('meso.npy', dict(K=K, Hfren=Hfren, Htemp=Htemp, Hvento=Hvento, Le=Le, T=T, x0=x0, Hf=Hf, w=w, w_desc=w_desc, w_carr=w_carr, Kneo=K_neo), allow_pickle=True)
