#Data Science Academy - www.datascienceacademy.com.br
#Projeto 3 - Construindo Chatbot personalizado com GPT-4 e linguagem python

#import
import openai

#chave
openai.api_key = "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"

#função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    #obtém a resposta do modelo de linguagem
    response = openai.Completion.create(

        #modelo usado
		#outros modelos estão disponíveis em https://platform.openai.com/account/rate-limits
		engine = "text-davinci-003",

		#texto inicial da conversa com o chatbot
		prompt = texto,

		#comprimento da resposta gerada pelo modelo
		max_tokens = 150,

		#quantas conclusões gerar para cada prompt
		n = 5,

		#o texto retornado não conterá a sequência de parada
		stop = None,

		#uma medida de aleatoriedade de um texto gerado pelo modelo. seu valor está entre 0 e 1
		#valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a 0 significam que a saída é muito identificável.
		temperature = 0.8,
    )

    return response.choices[0].text.strip()


#função principal do programa em python
def main():

    print("\nBem-Vindo ao GPT-4 ChatBot (um pequeno projeto)!")
    print("(digite 'sair' a qualquer momento para encerrar o chat!)")

    #loop
    while True:

    	#coleta a pergunta digitada pelo usuário
    	user_message = input("\nVocê: ")

    	#se a mensagem for "sair" finaliza o programa
    	if user_message.lower() == "sair":
    		break

    	#coloca a mensagem digitada pelo usuário na variável python chamada gpt4_prompt
    	gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

    	#obtém a resposta do modelo executando a função gera_texto()
    	chatbot_response = gera_texto(gpt4_prompt)

    	#imprime a resposta do chatbot
    	print(f"\nChatbot: {chatbot_response}")

#execução do programa (block main) em python
if __name__ == "__main__":
	main()