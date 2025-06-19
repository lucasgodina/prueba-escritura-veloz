"""
Funciones para comparar textos y calcular precisión.
"""

from difflib import SequenceMatcher
from typing import Tuple


def calcular_precision(texto_objetivo: str, texto_usuario: str) -> float:
    """
    Calcula el porcentaje de precisión entre el texto objetivo y el texto del usuario.
    """

    matcher = SequenceMatcher(None, texto_objetivo, texto_usuario)
    return matcher.ratio() * 100


def palabras_por_minuto(texto_usuario: str, segundos: float) -> float:
    """
    Calcula las palabras por minuto (WPM) dadas el texto escrito y el tiempo en segundos.
    """
    palabras = len(texto_usuario.split())
    minutos = segundos / 60
    return palabras / minutos if minutos > 0 else 0.0


def comparar_palabra_a_palabra(
    texto_objetivo: str, texto_usuario: str
) -> Tuple[int, int]:
    """
    Compara palabra a palabra y retorna el (correctas, total) palabras.
    """
    objetivo = texto_objetivo.split()
    usuario = texto_usuario.split()
    correctas = sum(1 for o, u in zip(objetivo, usuario) if o == u)
    return correctas, len(objetivo)
