# Chat Streamlit IA

Este é um projeto de chatbot interativo desenvolvido com Streamlit e integrado à API da OpenAI. O objetivo é fornecer uma interface amigável para interagir com um agente de IA personalizável.

## Funcionalidades

- **Chatbot Personalizável**: Configure o nome e o estilo de resposta do agente no arquivo `settings.py`.
- **Interface Gráfica**: Desenvolvida com Streamlit para uma experiência de usuário simples e intuitiva.
- **Integração com OpenAI**: Utilize modelos avançados como `gpt-3.5-turbo` para gerar respostas.

## Estrutura do Projeto

```
chat_streamlit_ia/
├── app/
│   ├── chatbot.py         # Lógica principal do chatbot
│   ├── interface.py       # Interface do usuário com Streamlit
│   └── __pycache__/       # Arquivos compilados
├── config/
│   ├── settings.py        # Configurações do projeto (API Key, nome do agente, etc.)
│   └── __pycache__/       # Arquivos compilados
├── main.py                # Arquivo principal para execução
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/JBSilvaDev/chat_streamlit_ia.git
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No Linux/Mac
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   - Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API da OpenAI:
     ```env
     API_KEY=your_openai_api_key
     ```

5. **Personalize o agente** (opcional):
   - No arquivo `config/settings.py`, ajuste as variáveis:
     ```python
     AGENT_NAME = "Assistente IA"
     RESPONSE_STYLE = "amigável e profissional"
     ```

## Execução

Para iniciar o chatbot, execute o seguinte comando:
```bash
streamlit run main.py
```

Acesse o aplicativo no navegador em: [http://localhost:8501](http://localhost:8501)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).