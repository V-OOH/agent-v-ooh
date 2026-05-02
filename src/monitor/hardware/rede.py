import psutil, socket, colorama
from colorama import Fore, Style

def info_rede()-> dict[str, str]:
    """
    Função para verificar conectividade com a rede

    Returns: True caso tenha rede e False caso contrário
    """

    # Captura de rede
    rede = psutil.net_io_counters()

    # Upload
    upload = rede.bytes_sent

    # Download
    download = rede.bytes_recv

    # Mac e IP da máquina
    i = info_mac_ip_address()

    # Informações
    info = {
        "ip": i['ip'],
        "mac": i['mac'],
        "upload": upload,
        "download": download,
    }

    return info

def info_mac_ip_address()-> dict[str, str]:
    """
    Retorna o IP e o MacAddress

    Returns: Dicionário de informações da placa de rede

    """

    # IP Mac Inicial
    ip_mac = {
        "ip": "0.0.0.0",
        "mac": "00:00:00:00:00:00"
    }

    # Variável de IP local inicial
    ip_local_detectado = None

    # Socket de conexão
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define o tempo de tentativa de conexão
    s.settimeout(2)

    try:
        # Tenta se conectar ao IP público do Google
        s.connect(("8.8.8.8", 80))
        ip_local_detectado = s.getsockname()[0]

    except Exception as erro:
        # Aviso de erro na leitura do IP e MAC
        print(Fore.YELLOW + f"Aviso: Rede indisponível ({erro})" + Style.RESET_ALL)

        # Lista as interfaces de IP
        interfaces = psutil.net_if_addrs()

    finally:
        # Fecha a conexão
        s.close()

    # Caso não encontre IP, retorna o IP e Mac Padrão
    if not ip_local_detectado:
        return ip_mac

    # Interface de rede
    interfaces = psutil.net_if_addrs()

    # Percorre a lista de interfaces e endereços
    for nome_interface, addrs in interfaces.items():
        temp_ip = None
        temp_mac = None

        for addr in addrs:
            if addr.family == socket.AF_INET:
                temp_ip = addr.address
            elif addr.family == psutil.AF_LINK:
                temp_mac = addr.address

        if temp_ip == ip_local_detectado:
            ip_mac["ip"] = temp_ip
            ip_mac["mac"] = temp_mac if temp_mac else "MAC não encontrado"
            break

    return ip_mac
