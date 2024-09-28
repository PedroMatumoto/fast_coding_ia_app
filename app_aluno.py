#desafio 1
#Escreva aqui seu primeiro requisito
"""
MONTAR UM PLANEJAMENTO COMPLETO, CONTANDO COM SUGESTÕES DE PONTOS TURISTICOS E CUSTO DE REFEIÇÕES NO LOCAL
"""
#Escreva aqui seu segundo requisito
"""
"""
#Escreva aqui seu terceiro requisito


import webbrowser
from dotenv import load_dotenv
from openai import OpenAI
import tkinter as tk
load_dotenv()
client = OpenAI()

#desafio 2 - Exibir mensagem de boas vindas


#desafio 3 - Permitir que o usuário informe o tipo de viagem desejado e guardar em uma variável


#desafio 4 - Permitir que o usuário informe seu orçamento e guardar a sua representação numérica em uma variável


#desafio 5 - Em função do orçamento informado pelo usuário, dizer a ele se a recomendação será econômica ou premium



#desafio 6 montar o prompt para sugestâo
#se desejar, inclua uma localização, valor estimado para comer etc
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = tk.Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = tk.Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = tk.Label(self.primeiroContainer, text="Dados da viagem")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.destino_viagem_label = tk.Label(self.segundoContainer,text="Tipo de destino", font=self.fontePadrao)
        self.destino_viagem_label.pack()

        self.tipo_destino_tf = tk.Entry(self.segundoContainer)
        self.tipo_destino_tf["width"] = 30
        self.tipo_destino_tf["font"] = self.fontePadrao
        self.tipo_destino_tf.pack()

        self.orçamento_label = tk.Label(self.segundoContainer,text="Orçamento máximo", font=self.fontePadrao)
        self.orçamento_label.pack()

        self.orçamento_tf = tk.Entry(self.segundoContainer)
        self.orçamento_tf["width"] = 30
        self.orçamento_tf["font"] = self.fontePadrao
        self.orçamento_tf.pack()

        self.pessoas_label = tk.Label(self.segundoContainer,text="Quantas pessoas irão?", font=self.fontePadrao)
        self.pessoas_label.pack()

        self.pessoas_viagem = tk.Entry(self.segundoContainer)
        self.pessoas_viagem["width"] = 30
        self.pessoas_viagem["font"] = self.fontePadrao
        self.pessoas_viagem.pack()

        self.dias_viagem_label = tk.Label(self.segundoContainer,text="Quantos dias irá durar sua viagem?", font=self.fontePadrao)
        self.dias_viagem_label.pack()

        self.dias_viagem_df = tk.Entry(self.segundoContainer)
        self.dias_viagem_df["width"] = 30
        self.dias_viagem_df["font"] = self.fontePadrao
        self.dias_viagem_df.pack()

        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        self.prompt_request = tk.Button(self.widget1)
        self.prompt_request["text"] = "Pesquisar"
        self.prompt_request["font"] = ("Calibri", "9")
        self.prompt_request["width"] = 10
        self.prompt_request.bind("<Button-1>", self.mandar_prompt)
        self.prompt_request.pack ()

        self.tipo_destino = ''
        self.max_orc = ''
        self.tipo = ''
        self.quant_pessoas_viagem = ''
        self.dias_viagem = ''
        self.prompt = ''

    def create_prompt(self):
        self.tipo_destino  = self.tipo_destino_tf.get()
        self.max_orc = self.orçamento_tf.get()

        if int(self.max_orc) > 3000:
            self.tipo = "premium"
        else:
            self.tipo = "econômico"


        self.quant_pessoas_viagem = self.pessoas_viagem.get()
        self.dias_viagens = self.dias_viagem_df.get()

        self.prompt =  f'Planeje uma viagem com o seguinte tipo de destino: {self.tipo_destino}; tipo de viagem: {self.tipo}; número de pessoas: {self.quant_pessoas_viagem}; dias de viagem: {self.dias_viagens}.'
    
    def mandar_prompt(self,event):

        self.create_prompt()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f'{self.prompt}. max:100 tokens'}
            ]
        )        

        print(completion.choices[0].message.content)


    

        



root = tk.Tk()
Application(root)
root.mainloop()
prompt_sugestao = ""

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
#     ]
# )


#Remova esse comentário quando o professor pedir, ok? :)
#print(completion.choices[0].message.content)

#desafio 7 montar o prompt para imagem
#o que você quer ver? # Uma praia? Pessoas? Mochilas? Montanha? Um cachorro correndo atrás de uma bola? Seja criativo(a)!
# prompt_imagem = ""
# response = client.images.generate(
#     model="dall-e-3",
#     prompt=prompt_imagem,
#     n=1,
#     size="1024x1024"
# )

#Remova esse comentário quando o professor pedir, ok? :)
#webbrowser.open(response.data[0].url)