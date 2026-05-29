# ============================================================
#  Análisis de Compromiso de Sesiones de Clientes
# ============================================================

# --- Datos Iniciales ---
# Formato: [ID Cliente, Duración (segundos), Eventos Clics]
sesiones = [
    ["C001", 210, 12],
    ["C002", 45,  2],
    ["C003", 130, 6],
    ["C004", 190, 4],
    ["C005", 30,  1],
    ["C006", 200, 9],
    ["C007", 75,  10],
]


# --- Módulo: Clasificación de Compromiso ---
def clasificar_compromiso(duracion: int, clics: int) -> str:
    """
    Clasifica el nivel de compromiso de una sesión.

    Parámetros:
        duracion (int): Duración de la sesión en segundos.
        clics    (int): Número de eventos de clic registrados.

    Retorna:
        str: "Alto", "Medio" o "Bajo"
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# --- Generación del Informe ---
def generar_informe(datos: list) -> None:
    """Imprime el informe de compromiso para todas las sesiones."""

    print("=" * 45)
    print("   INFORME DE COMPROMISO DE SESIONES")
    print("=" * 45)
    print(f"{'ID Cliente':<12} {'Duración (s)':<14} {'Clics':<8} {'Nivel'}")
    print("-" * 45)

    conteo = {"Alto": 0, "Medio": 0, "Bajo": 0}

    for fila in datos:
        id_cliente, duracion, clics = fila
        nivel = clasificar_compromiso(duracion, clics)
        conteo[nivel] += 1
        print(f"{id_cliente:<12} {duracion:<14} {clics:<8} {nivel}")

    print("=" * 45)
    print("  RESUMEN")
    print("-" * 45)
    for nivel, cantidad in conteo.items():
        print(f"  {nivel:<8}: {cantidad} sesión(es)")
    print("=" * 45)


# --- Punto de Entrada ---
if __name__ == "__main__":
    generar_informe(sesiones)