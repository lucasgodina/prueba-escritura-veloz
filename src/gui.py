import tkinter as tk
from tkinter import messagebox
from timer import Timer
from utils import calcular_precision, palabras_por_minuto, comparar_palabra_a_palabra
from phrases import obtener_frase_aleatoria


class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de Velocidad de Escritura")
        self.timer = Timer()
        self.frase = obtener_frase_aleatoria()
        self.timer_started = False

        # Widgets
        self.label_frase = tk.Label(
            root, text=self.frase, wraplength=400, font=("Arial", 14)
        )
        self.label_frase.pack(pady=20)

        self.entry = tk.Entry(root, width=60, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self._on_keypress)

        self.boton_terminar = tk.Button(root, text="Terminar", command=self.terminar)
        self.boton_terminar.pack(pady=10)

        self.resultado = tk.Label(root, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def _on_keypress(self, event):
        if not self.timer_started:
            self.timer.start()
            self.timer_started = True

    def terminar(self):
        self.timer.stop()
        texto_usuario = self.entry.get()
        tiempo = self.timer.elapsed()
        precision = calcular_precision(self.frase, texto_usuario)
        wpm = palabras_por_minuto(texto_usuario, tiempo)
        correctas, total = comparar_palabra_a_palabra(self.frase, texto_usuario)

        resultado_texto = (
            f"Tiempo: {tiempo:.2f} s\n"
            f"Precisión: {precision:.2f}%\n"
            f"Palabras correctas: {correctas}/{total}\n"
            f"Palabras por minuto: {wpm:.2f}"
        )
        self.resultado.config(text=resultado_texto)
        self.boton_terminar.config(state=tk.DISABLED)
        self.entry.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
