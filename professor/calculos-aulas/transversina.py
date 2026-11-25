import numpy as np
phi = 1.35*1.25
l = 5.00; Lt = 10.0            # vão da transversina; distância entre transversinas
bw, h, hl = 0.30, 1.50, 0.22
g_laje = 25*hl + 24*0.08 + 2.0
pp = 25*bw*(h-hl)
q0 = 2*g_laje*(l/2)            # pico da carga triangular (bissetrizes, dois painéis)
Mg = pp*l**2/8 + q0*l**2/12
Vg = pp*l/2 + q0*l/4
print(f"pp={pp:.2f} kN/m ; q0={q0:.2f} kN/m ; Mg={Mg:.2f} ; Vg={Vg:.2f}")
# trem-tipo da transversina (LI longitudinal da reação na transversina)
eta = lambda y: max(0.0, 1-abs(y)/Lt)
sum_eta = sum(eta(y) for y in (-1.5, 0, 1.5))
Pt = 75*sum_eta
area_tot = Lt                      # 2 triângulos de base Lt e altura 1
area_veic = 2*3.0*(eta(0)+eta(3.0))/2
q_fora = 5*area_tot; q_sob = 5*(area_tot-area_veic)
print(f"sum eta={sum_eta:.3f} -> Pt={Pt:.1f} kN/roda ; q fora={q_fora:.1f} ; q sob veículo={q_sob:.2f} kN/m")
# varredura da posição do veículo na transversina (biapoiada 0..l)
xs = np.linspace(0, l, 2001)
def esforcos(xc, x_sec):
    """Momento na seção x_sec e reação em A para veículo centrado em xc (rodas xc±1, faixa xc±1.5)."""
    # cargas concentradas
    M = 0.0; RA = 0.0
    for xr in (xc-1.0, xc+1.0):
        if 0 <= xr <= l:
            ra = Pt*(l-xr)/l; RA += ra
            M += ra*x_sec - (Pt*(x_sec-xr) if xr < x_sec else 0)
    # distribuída
    q = np.where((xs >= xc-1.5) & (xs <= xc+1.5), q_sob, q_fora)
    ra = np.trapezoid(q*(l-xs)/l, xs); RA += ra
    m = ra*x_sec - np.trapezoid(np.where(xs < x_sec, q*(x_sec-xs), 0), xs)
    return M+m, RA
best = max(((esforcos(xc, xs_)[0], xc, xs_) for xc in np.arange(0.5, 4.51, 0.01) for xs_ in np.arange(1.5, 3.51, 0.05)))
print(f"Mq,máx (sem phi) = {best[0]:.1f} kNm com veículo centrado em {best[1]:.2f} m, seção {best[2]:.2f} m")
Vq = max(esforcos(xc, 0.0)[1] for xc in np.arange(1.0, 4.51, 0.01))
print(f"Vq,máx (sem phi) = {Vq:.1f} kN")
Mqd, Vqd = phi*best[0], phi*Vq
Md = 1.35*Mg + 1.5*Mqd; Vd = 1.35*Vg + 1.5*Vqd
print(f"Mq,phi={Mqd:.1f} Vq,phi={Vqd:.1f} ; Md={Md:.1f} kNm ; Vd={Vd:.1f} kN")
# comparação com a fórmula simplificada (um eixo, rodas simétricas)
Pd1 = 75*phi
print(f"um eixo simétrico: Mq,phi={Pd1*(l-2)/2:.1f} ; Barré um eixo: {Pd1*(l-1)**2/(2*l):.1f}")
# dimensionamento flexão (retangular, mesa colaborante ignorada p/ simplificar se LN na mesa)
fcd = 30/1.4*1000; fyd = 500/1.15*1000
d = h - 0.04 - 0.0125 - 0.02
bf = bw + 2*0.10*l   # largura colaborante, viga biapoiada (a = l)
x = 1.25*d*(1-np.sqrt(1-Md/(0.425*bf*d**2*fcd)))
As = Md/(fyd*(d-0.4*x))*1e4
print(f"d={d:.3f} bf={bf:.2f} x={x*100:.1f} cm (mesa {hl*100:.0f} cm) As={As:.2f} cm2 ; As,min={0.15/100*bw*h*1e4:.2f}")
# cisalhamento modelo I
fck=30; fctm=0.3*fck**(2/3); fctd=0.7*fctm/1.4*1000
av2=1-fck/250; VRd2=0.27*av2*fcd*bw*d; Vc=0.6*fctd*bw*d
asw=(Vd-Vc)/(0.9*d*435e3)*1e4 ; aswmin=0.2*fctm/500*bw*1e4
print(f"VRd2={VRd2:.0f} kN ; Vc={Vc:.0f} ; Asw/s={asw:.2f} cm2/m ; min={aswmin:.2f} cm2/m")
print(f"pele: 0,10% Ac,alma por face = {0.001*bw*(h-hl)*1e4:.2f} cm2/face")
# macaqueamento transversina de apoio
Rg = 900.0; nmac = 2; em = 0.60
F = 1.35*Rg/nmac; Mm = F*em
print(f"macaco: F={F:.1f} kN ; M (exc. {em} m) = {Mm:.1f} kNm")
