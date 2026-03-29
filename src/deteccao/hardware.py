from colorama import Fore
from deteccao.processador import processador


def hardware(plataforma: str) -> dict:
    """
    Função para detectar as informações de hardware do dispositivo

    Obtém as informações de:
        - Nome do processador
        - Arquitetura
        - Quantidade de núcleos
        - Frequência mínima
        - Frequência máxima


    Returns: Dicionário de informações do hardware
    """

    # Obtém as informações do processador
    info_processador = processador(plataforma)

    # Informações


