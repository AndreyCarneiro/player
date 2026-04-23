import tkinter as tk

janela = tk.Tk()
janela.title("Player")
janela.geometry("300x200")
janela.configure(bg= "#000000")

def play():
    print("Play")

btn = tk.Button(janela, text="Play", command=play, fg = "#962A2A",bg = "#000000" )
btn.pack()

txt = tk.Label(janela, text ="Teste", fg = "#962A2A",bg = "#000000",font= ("Arial",38,"bold"), padx = 14, pady = 14)
txt.pack()

janela.mainloop()