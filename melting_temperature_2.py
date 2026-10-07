"""
Bioinformatics Lab - Melting temperature (Tm), two formulas
1) Wallace rule:      Tm = 4 * (G + C) + 2 * (A + T)
2) Salt-adjusted:     Tm = 81.5 + 16.6 * log10([Na+]) + 0.41 * (%GC) - 600 / length
"""

import math

S = "ACGCGTGCCA"
Na = 0.05  # [Na+] in mol/L (50 mM, a typical PCR value)

A = S.count("A")
T = S.count("T")
C = S.count("C")
G = S.count("G")
length = len(S)

# Formula 1
Tm1 = 4 * (G + C) + 2 * (A + T)

# Formula 2
percent_GC = (G + C) / length * 100
Tm2 = 81.5 + 16.6 * math.log10(Na) + 0.41 * percent_GC - 600 / length

print("S =", S)
print("Length =", length)
print("A =", A, " T =", T, " C =", C, " G =", G)
print("%GC =", percent_GC, "%")
print()
print("Formula 1: Tm = 4 *", G + C, "+ 2 *", A + T, "=", Tm1, "°C")
print("Formula 2 ([Na+] =", Na, "M): Tm =", round(Tm2, 2), "°C")
