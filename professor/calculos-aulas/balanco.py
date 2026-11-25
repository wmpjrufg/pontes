import numpy as np
res = np.load('res_tab.npy', allow_pickle=True).item()
phi = 1.6875; P = 75.0; e_asf = 0.08
gc, gasf = 25.0, 24.0
# geometria do balanço (a partir da face da longarina)
lb = 2.00; h0, h1 = 0.30, 0.20; xbar_face = 1.60  # face interna da barreira
pbar, xb = 0.23*25, 1.83
# peso próprio (trapézio): resultante e braço
W_lp = gc*(h0+h1)/2*lb
x_lp = lb*(h0+2*h1)/(3*(h0+h1))
M_lp = W_lp*x_lp
g2 = gasf*e_asf + 2.0
M_pav = g2*xbar_face**2/2; V_pav = g2*xbar_face
M_bar = pbar*xb
Mg = M_lp + M_pav + M_bar; Vg = W_lp + V_pav + pbar
print(f"laje: W={W_lp:.2f} x={x_lp:.3f} M={M_lp:.2f} | pav M={M_pav:.2f} | barreira M={M_bar:.2f}")
print(f"Mg={Mg:.2f} kNm/m  Vg={Vg:.2f} kN/m")
x = xbar_face - 0.50
hx = h0 - (h0-h1)*x/lb
b1 = 0.20 + 2*e_asf + hx
bef = b1 + 2*x
print(f"roda a x={x:.2f} m; h(x)={hx:.3f}; b1={b1:.3f}; bef={bef:.3f} m (> 1,50 m => sobreposição)")
bt = 2*1.5 + bef
Mq1 = P*x/bef; Mq3 = 3*P*x/bt
Vq3 = 3*P/bt
print(f"1 roda: Mq={Mq1:.2f}; 3 rodas (largura conjunta {bt:.2f} m): Mq={Mq3:.2f} kNm/m ; Vq={Vq3:.2f} kN/m")
Mqd = phi*Mq3; Vqd = phi*Vq3
Md_b = 1.35*Mg + 1.5*Mqd
Vd_b = 1.35*Vg + 1.5*Vqd
print(f"balanço: Mq,phi={Mqd:.2f}  Md={Md_b:.2f}  Vd={Vd_b:.2f}")

mg_v, mq_v = res['mx_vao'][0], phi*res['mx_vao'][1]
mg_y, mq_y = res['my_vao'][0], phi*res['my_vao'][1]
mg_e, mq_e = res['mx_engaste'][0], phi*res['mx_engaste'][1]
Md_v = 1.35*mg_v + 1.5*mq_v
Md_y = 1.35*mg_y + 1.5*mq_y
Xd_c = 1.35*mg_e + 1.5*mq_e
print(f"central: Mx,d vão={Md_v:.2f} ; My,d={Md_y:.2f} ; X,d engaste={Xd_c:.2f}")
A, B = abs(Xd_c), abs(-Md_b)
media = (A+B)/2; oit = 0.8*max(A, B)
Xcomp = max(media, oit, B)
print(f"compat: média={media:.2f} 0,8max={oit:.2f} balanço={B:.2f} -> X={Xcomp:.2f}")
dM = (A - Xcomp)/2 if Xcomp < A else 0.0
print(f"correção positivo: +{dM:.2f} -> Mx,d vão corrigido={Md_v+dM:.2f}")

def As(Md, d, fck=30, fyk=500, bw=1.0):
    fcd = fck/1.4*1000; fyd = fyk/1.15*1000
    x = 1.25*d*(1-np.sqrt(1-Md/(0.425*bw*d**2*fcd)))
    return x, x/d, Md/(fyd*(d-0.4*x))*1e4
for nome, M, h in [('vão central x', Md_v+dM, 0.22), ('vão central y', Md_y, 0.22), ('apoio (negativo)', Xcomp, 0.30)]:
    phi_b = 0.0125 if 'apoio' in nome else 0.010
    d = h - 0.04 - phi_b/2 - (0.010 if nome.endswith('y') else 0)
    x_, xd, a = As(M, d)
    asmin = 0.15/100*h*1e4
    print(f"{nome:18s} Md={M:7.2f} d={d:.3f} x/d={xd:.3f} As={a:6.2f} cm2/m (min {asmin:.2f})")
# fadiga psi1=0.8
for nome, mg, mq in [('vão', mg_v, mq_v), ('engaste central', mg_e, mq_e)]:
    print(f"fadiga {nome}: Mmax={mg+0.8*mq:.2f} Mmin={mg:.2f} dM={0.8*mq:.2f}")
print(f"fadiga balanço: Mmax={Mg+0.8*Mqd:.2f} Mmin={Mg:.2f}")
