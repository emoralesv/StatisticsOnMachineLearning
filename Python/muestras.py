# archivo: ejercicios_tamanio_muestra_fresas.py
import math

def n_media_sigma_conocida(Z, sigma, E):
    """Tamaño de muestra para media con sigma conocida (Z)."""
    return math.ceil(((Z * sigma) / E) ** 2)

def n_media_sigma_desconocida_con_t(t_crit, s, E):
    """
    Tamaño de muestra para media con sigma desconocida (usando t crítico de una muestra piloto).
    Nota: aquí se pasa t_crit (por ejemplo, t_{alpha/2, df}) como argumento.
    """
    return math.ceil(((t_crit * s) / E) ** 2)

def n_proporcion(Z, p, E):
    """Tamaño de muestra para proporción (Z)."""
    return math.ceil((Z**2 * p * (1 - p)) / (E**2))

def correccion_poblacion_finita(n, N):
    """Ajuste por población finita."""
    return math.floor((n * N) / (n + N - 1))

# =========================
# 1) Media (σ desconocida) con muestra piloto (t-Student)
# Piloto: n0 = 25 -> df = 24, s = 5 mm, t_crit ≈ 2.064 (95% dos colas)
t_crit = 2.064
s = 5.0        # mm
E1 = 1.0       # mm
n1 = n_media_sigma_desconocida_con_t(t_crit=t_crit, s=s, E=E1)

# =========================
# 2) Media (σ desconocida) usando rango/4 con Z
# Rango = 20 mm -> sigma ≈ 5 mm; 95% -> Z = 1.96; E = 1.5 mm
Z_95 = 1.96
sigma_aprox = 20.0 / 4.0
E2 = 1
n2 = n_media_sigma_conocida(Z=Z_95, sigma=sigma_aprox, E=E2)

# =========================
# 3) Proporción de frutas enfermas sin p previa (p = 0.5 conservador), Z
E3 = 0.05
p_conservador = 0.5
n3 = n_proporcion(Z=Z_95, p=p_conservador, E=E3)

# =========================
# (Opcional) Ejemplo de corrección por población finita para el caso 3
# Supón N = 10,000 fresas en el lote:
N = 10_000
n3_aj = correccion_poblacion_finita(n3, N)

# =========================
# Impresión de resultados
print("=== Tamaños de muestra (fresas) ===")
print(f"1) Media (σ desconocida, piloto t): n = {n1}  (t={t_crit}, s={s}, E={E1})")
print(f"2) Media (rango/4 con Z):          n = {n2}  (Z={Z_95}, σ≈{sigma_aprox}, E={E2})")
print(f"3) Proporción (p=0.5, Z):           n = {n3}  (Z={Z_95}, p={p_conservador}, E={E3})")
print(f"   Corrección población finita (N={N}): n_aj = {n3_aj}")
