from openai import OpenAI
from config.settings import API_KEY, VERIFY_SSL, AGENT_NAME, RESPONSE_STYLE


class ChatBot:
    def __init__(self):
        # Inicializa o cliente OpenAI com a chave de API e configuração SSL
        self.model = OpenAI(
            api_key=API_KEY,
            http_client=VERIFY_SSL,
        )
        self.name = AGENT_NAME
        self.response_style = RESPONSE_STYLE

    def get_response(self, messages: list) -> str:
        try:
            # Adiciona uma mensagem de sistema para personalizar o comportamento do agente
            system_message = {
                "role": "system",
                "content": f"Você é {self.name}. Responda de forma {self.response_style}.",
            }
            messages.insert(0, system_message)

            response = self.model.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo-0125",
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Erro ao obter resposta do modelo: {e}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação."
