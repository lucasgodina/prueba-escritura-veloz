"""
Módulo con lista de frases provenientes de obras literarias clásicas.

Funciones:
- get_random_phrase: Devuelve una frase aleatoria de la lista.
"""

import random

phrases = [
    "Fue el mejor de los tiempos, fue el peor de los tiempos, fue la edad de la sabiduría, fue la edad de la necedad, fue la época de la fe, fue la época de la incredulidad, fue la estación de la Luz, fue la estación de la Oscuridad, fue la primavera de la esperanza, fue el invierno de la desesperación, todo lo teníamos ante nosotros, nada teníamos ante nosotros, íbamos todos directamente al Cielo, íbamos todos directamente en dirección contraria.",
    "En un agujero en el suelo vivía un hobbit. No un agujero húmedo, sucio, repugnante, con restos de gusanos y olor a fango, ni tampoco un agujero seco, arenoso, sin nada en que sentarse o que comer: era un agujero-hobbit, y eso significa comodidad.",
    "Es una verdad universalmente reconocida que un hombre soltero en posesión de una gran fortuna debe necesitar una esposa.",
    "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo.",
    "La primera vez que la vio, era una mañana soleada de primavera y el aire estaba lleno del dulce aroma de las lilas en flor, un olor que desde entonces asociaría para siempre con el amor perdido y la melancolía del recuerdo.",
    "El sol, a pesar de la distancia, continuaba su implacable danza sobre las dunas infinitas, tiñendo el horizonte con tonos de cobre y carmesí, mientras el viento, un mensajero incansable de secretos ancestrales, susurraba historias olvidadas a través de los juncos resecos.",
    "Todo lo que sé con mayor certeza sobre la moral y las obligaciones de los hombres, se lo debo al fútbol.",
    "Era el tipo de noche en que el viento aullaba como un lobo hambriento a través de los desolados páramos, llevando consigo el gélido aliento del invierno y prometiendo una tormenta inminente que envolvería el pequeño pueblo en una manta de nieve y silencio.",
    "A veces, el mero acto de mirar un mapa era suficiente para transportarlo a mundos inexplorados, a cumbres nevadas y valles profundos, a ciudades bulliciosas y aldeas remotas, sintiendo el ansia de aventura burbujear en sus venas como un río desbordado.",
    "La biblioteca era un laberinto de estantes llenos hasta el techo con volúmenes polvorientos, cada uno de ellos un portal a un universo distinto, a vidas pasadas y futuras, a sueños olvidados y realidades inexploradas, un refugio para el alma inquieta en busca de conocimiento.",
]


def obtener_frase_aleatoria():
    """Devuelve una frase aleatoria de la lista."""
    return random.choice(phrases)
