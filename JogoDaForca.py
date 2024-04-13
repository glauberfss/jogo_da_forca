import tkinter as tk
import random

class JogoDaForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")

        self.palavras = ["amizade", "programacao", "desafio", "sentimentos", "linguagem", "emocao", "sucesso"]
        self.palavra_secreta = random.choice(self.palavras)

        self.letras_corretas = []
        self.tentativas = 6

        self.label_palavra = tk.Label(self.master, text=self.mostrar_forca(), font=("Arial", 24))
        self.label_palavra.pack()

        self.label_tentativas = tk.Label(self.master, text=f"Tentativas restantes: {self.tentativas}", font=("Arial", 16))
        self.label_tentativas.pack()

        self.entry_letra = tk.Entry(self.master, font=("Arial", 16))
        self.entry_letra.pack()

        self.button_adivinhar = tk.Button(self.master, text="Adivinhar", command=self.adivinhar_letra, font=("Arial", 16))
        self.button_adivinhar.pack()

    def mostrar_forca(self):
        resultado = ""
        for letra in self.palavra_secreta:
            if letra in self.letras_corretas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado.strip()

    def adivinhar_letra(self):
        letra = self.entry_letra.get().lower()

        if letra in self.letras_corretas:
            tk.messagebox.showinfo("Adivinhar letra", "Você já tentou esta letra.")
        elif not letra.isalpha() or len(letra) != 1:
            tk.messagebox.showinfo("Adivinhar letra", "Por favor, insira apenas uma letra.")
        elif letra in self.palavra_secreta:
            self.letras_corretas.append(letra)
            self.atualizar_interface()
            if "_" not in self.mostrar_forca():
                tk.messagebox.showinfo("Parabéns!", "Você ganhou!")
                self.resetar_jogo()
        else:
            self.tentativas -= 1
            self.atualizar_interface()
            if self.tentativas == 0:
                tk.messagebox.showinfo("Game Over", f"Você perdeu! A palavra secreta era: {self.palavra_secreta}")
                self.resetar_jogo()

    def atualizar_interface(self):
        self.label_palavra.config(text=self.mostrar_forca())
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.entry_letra.delete(0, tk.END)

    def resetar_jogo(self):
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_corretas = []
        self.tentativas = 6
        self.atualizar_interface()

def main():
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()

if __name__ == '__main__':
    main()
