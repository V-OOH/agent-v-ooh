import psutil
from colorama import Fore, Style

def info_temperatura() -> dict[str, float | None]:
    """
    Obtém informações da temperatura do processador (Package).
    """

    # Dados
    dados = {}

    try:
        temperaturas = psutil.sensors_temperatures()

        # Verifica se o driver da Intel (coretemp) está presente
        if "coretemp" in temperaturas:
            # Percorre os sensores dentro de 'coretemp'
            for s in temperaturas["coretemp"]:
                # Procura especificamente pelo "Package id 0"
                if s.label == "Package id 0":
                    dados = {
                        "atual": s.current,
                        "alta": s.high,
                        "critica": s.critical
                    }
                    break  # Parar o loop

            # Caso não encontre o label exato, pegamos a primeira entrada como backup
            if not dados and temperaturas["coretemp"]:
                s = temperaturas["coretemp"][0]
                dados = {"atual": s.current, "alta": s.high, "critica": s.critical}

        return dados

    except Exception as erro:
        print(Fore.RED + f"Erro ao verificar temperatura: {erro}" + Style.RESET_ALL)
        return {}