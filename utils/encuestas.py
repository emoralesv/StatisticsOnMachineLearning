import matplotlib.pyplot as plt

# Datos de la encuesta
labels = ['Les gusta', 'Indiferente', 'No les gusta']
sizes = [70, 27, 3]
explode = (0, 0, 0.01)  # resalta el 3%

# Crear la figura
plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.0f%%',
    startangle=90,
    explode=explode,
    textprops={'fontsize': 19}
)
plt.title('')
plt.axis('equal')  # Pie como círculo perfecto


# Mostrar gráfico
salida_png = "encuesta.png"

plt.tight_layout()
plt.savefig(salida_png, dpi=200, bbox_inches="tight")
print(f"Guardado en: {salida_png}")
plt.show()