import psutil
      
def info_ram() -> dict:
    """
    Função para detectar capacidade de RAM do dispositivo

    Returns: Dicionário de informações da RAM
    """

    # Objeto de RAM do psutil
    ram = psutil.virtual_memory()

    # RAM total
    total = ram.total 

    # RAM disponível
    disponivel = ram.available 

    # RAM em uso (%)
    percentual = ram.percent

    # Informações da RAM
    info = {
        "total": total,
        "disponivel": disponivel,
        "percentual": percentual
    }

    # Retorna as informações
    return info