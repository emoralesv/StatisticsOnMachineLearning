# gantt_poblacion_muestra_split_espaciado.py
import matplotlib.pyplot as plt

# --- Parámetros ---
poblacion_inicio, poblacion_duracion = 0, 100
muestra_inicio, muestra_duracion = 0, 45  # la muestra está dentro de la población
train_ratio, test_ratio = 0.8, 0.2         # 80% - 20% split

# Control del layout
altura_barra = 5    # grosor de cada barra (no lo cambiamos)
espaciado = 2       # <— reduce/crece el espacio vertical entre barras
y0 = 2              # posición de la barra inferior (partición)

# Posiciones verticales calculadas
y_part = y0
y_muestra = y_part + altura_barra + espaciado
y_pob = y_muestra + altura_barra + espaciado

# Centros (para etiquetas y yticks)
c_part = y_part + altura_barra/2
c_muestra = y_muestra + altura_barra/2
c_pob = y_pob + altura_barra/2

salida_png = "gantt_poblacion_muestra_split.png"
# ------------------

fig, ax = plt.subplots(figsize=(7, 2))

# --- Barras tipo Gantt ---
# Población
ax.broken_barh([(poblacion_inicio, poblacion_duracion)], (y_pob, altura_barra), facecolors="lightblue")

# Muestra
ax.broken_barh([(muestra_inicio, muestra_duracion)], (y_muestra, altura_barra), facecolors="orange")

# Particiones (80% train, 20% test)
train_w = muestra_duracion * train_ratio
test_w = muestra_duracion * test_ratio
splits = [(muestra_inicio, train_w), (muestra_inicio + train_w, test_w)]
colores = ["#99FF99", "#FF9999"]  # verde = train, rojo = test
labels = ["Partición 1 (80%)", "Partición 2 (20%)"]

for (start, width), color, label in zip(splits, colores, labels):
    ax.broken_barh([(start, width)], (y_part, altura_barra), facecolors=color)
    ax.text(start + width/2, c_part, label, ha="left", va="center", fontsize=9)

# --- Ejes y formato ---
ax.set_xlim(0, 100)
ax.set_ylim(0, y_pob + altura_barra + y0)   # ajuste automático del alto
ax.set_xlabel("Porcentaje de la población (%)")
ax.set_yticks([c_pob, c_muestra, c_part])
ax.set_yticklabels(["Población (N)", "Muestra (n)", "Partición (k)"])
ax.grid(axis="x", linestyle="--", alpha=0.6)

# --- Anotaciones (centradas) ---
ax.text(poblacion_inicio + 2, c_pob, "Todos los individuos", va="center")
ax.text(muestra_inicio + 2, c_muestra, "Subconjunto de la población", va="center")

plt.tight_layout()
plt.savefig(salida_png, dpi=200, bbox_inches="tight")
print(f"Guardado en: {salida_png}")
plt.show()
