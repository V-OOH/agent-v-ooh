import psutil, datetime
from datetime import datetime, timedelta

def boot_time() -> dict[str, timedelta]:
    """
    Retorna o tempo que a máquina está ligada

    Returns:
        Dicionário com data e hora
    """

    # Boot time do psutil
    boot_timestamp = datetime.fromtimestamp(psutil.boot_time())

    # Tempo ligado
    tempo_ligado = datetime.now() - boot_timestamp

    # Dados
    dados = {
        "boot_time": tempo_ligado
    }

    return dados
