from borracho import BorrachoTradicional, BorrachoMuyMareado, BorrachoNoIzquierda
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    
    coordenadas = []
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        coord = campo.obtener_coordenada(borracho)
        coordenadas.append(coord)
    
    return (inicio.distancia(campo.obtener_coordenada(borracho)), coordenadas)

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []
    coordenadas = []
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata, coord = caminata(campo, borracho, pasos)
        coordenadas += coord
        distancias.append(round(simulacion_caminata, 1))
        
    return (distancias, coordenadas)

def graficar(x, y, grafica, tipo_borracho, color):
    grafica.line(x, y, legend_label=f'distancia media {tipo_borracho}', line_color = color)

def graficar_camino(x, y, grafica, tipo_borracho, color):
    grafica.line(x, y, legend_label=f'Camino {tipo_borracho}', line_color = color)


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    grafica_caminos = figure(title='Grafica caminos', x_axis_label="x", y_axis_label="y")

    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias, coordenadas = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)

        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

        x = []
        y = []
        for coord in coordenadas:
            x.append(coord.x)
            y.append(coord.y)

        graficar_camino(x, y, grafica_caminos, "borracho", "#ff0000")
        show(grafica_caminos)


    return (distancias_de_caminata, distancias_media_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    grafica = figure(title='Camino aleatorio', x_axis_label="pasos", y_axis_label="distancia")
    
    distancias_de_caminata, distancias_media_por_caminata = main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
    graficar(distancias_de_caminata, distancias_media_por_caminata, grafica, "borracho normal", "#ff0000")

    distancias_de_caminata, distancias_media_por_caminata = main(distancias_de_caminata, numero_de_intentos, BorrachoMuyMareado)
    graficar(distancias_de_caminata, distancias_media_por_caminata, grafica, "borracho muy mareado", "#0000ff")

    distancias_de_caminata, distancias_media_por_caminata = main(distancias_de_caminata, numero_de_intentos, BorrachoNoIzquierda)
    graficar(distancias_de_caminata, distancias_media_por_caminata, grafica, "borracho no izquierda", "#00ff00")

    show(grafica)

    
