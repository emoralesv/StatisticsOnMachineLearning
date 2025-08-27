# venn_poblacion_muestra.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# --- Parámetros ---
r_poblacion = 2.5      # radio del círculo de la población
r_muestra = 1.2        # radio del círculo de la muestra
c_poblacion = (0, 0)   # centro de la población
c_muestra = (0.7, 0)   # centro de la muestra (dentro de población)
salida_png = "venn_poblacion_muestra.png"
# -------------------

fig, ax = plt.subplots(figsize=(6, 6))

# Círculo de Población
poblacion = Circle(c_poblacion, r_poblacion, alpha=0.3, color="skyblue")
ax.add_patch(poblacion)
ax.add_patch(Circle(c_poblacion, r_poblacion, fill=False, linewidth=2))

# Círculo de Muestra
muestra = Circle(c_muestra, r_muestra, alpha=0.5, color="orange")
ax.add_patch(muestra)
ax.add_patch(Circle(c_muestra, r_muestra, fill=False, linewidth=2))

# Etiquetas
ax.text(-2, 2.7, "Población (N)", fontsize=12, color="blue")
ax.text(c_muestra[0], c_muestra[1], "Muestra (n)", fontsize=12,
        color="darkorange", ha="center", va="center")

# Formato del gráfico
ax.set_aspect('equal', 'box')
ax.set_xlim(-3, 3.5)
ax.set_ylim(-3, 3)
ax.axis('off')
ax.set_title("Diagrama de Venn: Población y Muestra")

# Guardar y mostrar
plt.tight_layout()
plt.savefig(salida_png, dpi=200, bbox_inches="tight")
print(f"Guardado en: {salida_png}")
plt.show()
