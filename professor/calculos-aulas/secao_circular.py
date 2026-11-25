import numpy as np
def NM_resist(D, As, x, fcd, fyd=500/1.15*1000, Es=210e6, c=0.05, nb=40, ncam=200):
    """Esforços resistentes (N compressão +, M) de seção circular com LN a profundidade x (domínios NBR 6118, fck<=50)."""
    R = D/2; rs = R - c
    ecu, ec2 = 0.0035, 0.002
    d = R + rs
    # deformação no bordo comprimido: domínios 2/3/4/5 (pivôs)
    if x <= 0: return None
    if x < 0.259*d:     # domínio 2: aço mais tracionado = 10‰
        ec = 0.010*x/(d-x)
    elif x <= D:
        ec = ecu
    else:               # domínio 5: pivô C a 3/7 h
        ec = ec2*x/(x-3/7*D)
    kappa = ec/x
    # concreto por faixas
    ys = np.linspace(-R, R, ncam+1); yc = (ys[1:]+ys[:-1])/2; dy = ys[1]-ys[0]
    b = 2*np.sqrt(np.maximum(R**2-yc**2, 0))
    eps = kappa*(yc - (R - x))      # y medido do centro, positivo para o bordo comprimido
    sig = np.where(eps <= 0, 0, np.where(eps < ec2, 0.85*fcd*(1-(1-eps/ec2)**2), 0.85*fcd))
    Nc = np.sum(sig*b*dy); Mc = np.sum(sig*b*dy*yc)
    th = np.linspace(0, 2*np.pi, nb, endpoint=False)
    yb = rs*np.cos(th); Ab = As/nb
    eb = kappa*(yb - (R - x))
    sb = np.clip(Es*eb, -fyd, fyd)
    return Nc + np.sum(sb*Ab), Mc + np.sum(sb*Ab*yb)

def MRd(D, As, Nd, fcd, **kw):
    lo, hi = 1e-4, 20*D
    for _ in range(100):
        x = (lo+hi)/2
        N, M = NM_resist(D, As, x, fcd, **kw)
        if N > Nd: hi = x
        else: lo = x
    return NM_resist(D, As, (lo+hi)/2, fcd, **kw)[1]

def As_nec(D, Nd, Md, fcd, **kw):
    if MRd(D, 0.0, Nd, fcd, **kw) >= Md: return 0.0
    lo, hi = 0.0, 0.08*np.pi*D**2/4
    for _ in range(60):
        a = (lo+hi)/2
        if MRd(D, a, Nd, fcd, **kw) >= Md: hi = a
        else: lo = a
    return hi
