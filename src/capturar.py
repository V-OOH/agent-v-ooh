import sys

import psutil
import time
from colorama import Fore, Style

from src.monitor.hardware.disco import info_disco
from src.monitor.hardware.processador import info_processador
from src.monitor.hardware.ram import info_ram
from src.monitor.hardware.rede import info_rede
from src.monitor.hardware.rede import info_mac_address
from src.util.salvar import salvar

# Captura os dados com base num componente e numa frequência
def captura(frequencia: int, plataforma: str):
    """
    Faz a captura de dados de um componente de hardware da máquina

    Args:
        frequencia: O valor da frequência.
        plataforma: Windows ou Linux
    """

    # Atribui o tipo correto de partição root do sistema (Windows 'C:\\' e Linux: '/')
    if plataforma == "Linux":
        root = '/'
    elif plataforma == "Windows":
        root = 'C:\\'
    else:
        print("Plataforma não suportada")
        sys.exit()

    # Loop
    while True:
        info_processador(),
        info_ram(),
        info_rede(),
        info_disco(),
        info_mac_address()

    disco = info_disco(plataforma=plataforma)
    d = disco[0]
    total_disco = d["total"]
    disco_usado = d["usado"]
    disco_livre = d["livre"]
    disco_percentual = d["percentual"]

    processdor = info_processador(plataforma=plataforma)
    p = processador[0]
    processador_nome = p["processador"]
    nucleos_fisicos = p["nucleos_fisicos"]
    nucleos_totais = p["nucleos_totais"]
    frequencia_min = p["freq_min"]
    frequencia_max = p["freq_max"]

    ram = info_ram()
    r = ram
    ram_total = r["total"]
    ram_disponivel = r["disponivel"]
    ram_percentual = r["percentual"]

    rede = info_rede()
    n = rede
    upload = n["upload"]
    download= n["download"]

    mac = info_mac_address()
    m = mac
    interface = m["interface"]
    mac = m["mac"]

    cabecalho = [
        "data_hora",
        "total_disco",
        "disco_usado",
        "disco_livre",
        "disco_percentual",
        "processador_nome",
        "nucleos_fiscos",
        "nucleos_totais",
        "frequencia_min",
        "frequencia_max",
        "ram_total",
        "ram_disponivel",
        "ram_percentual",
        "upload",
        "download",
        "interface",
        "mac"
    ]

    dados = {
      "data_hora":time.strftime('%d-%m-%Y %H:%M:%S'),
      "total_disco": total_disco,
      "disco_usado": disco_usado,
      "disco_livre": disco_livre,
      "disco_percentual": disco_percentual,
      "processador_nome": processador_nome,
      "nucleos_fiscos": nucleos_fisicos,
      "nucleos_totais": nucleos_totais,
      "frequencia_min": frequencia_min,
      "frequencia_max": frequencia_max,
      "ram_total": ram_total,
      "ram_disponivel": ram_disponivel,
      "ram_percentual": ram_percentual,
      "upload": upload,
      "download": download,
      "interface": interface,
      "mac": mac
    }

    salvar("data/dados.csv", cabecalho, dados)

    time.sleep(frequencia)


        