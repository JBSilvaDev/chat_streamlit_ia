import os
from dotenv import load_dotenv
import httpx


# Carrega variáveis do .env
load_dotenv()


API_KEY = os.getenv("API_KEY")
VERIFY_SSL = httpx.Client(verify=False)

# Configurações do agente
AGENT_NAME = "JBot"
RESPONSE_STYLE = "Quando usuario der tal libertade, responda de forma descontraída e casual, caso contrario, mantenha um tom amigável"
