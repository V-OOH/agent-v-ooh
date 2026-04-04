import psutil, socket

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

def info_mac_ip_address()-> dict[str, str] | None:
    """
    Retorna o IP e o MacAddress

    Returns: Dicionário de informações da placa de rede

    """

    # Realiza uma chamada de conexão via socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Tenta se conectar ao IP público do Goolgle
        s.connect(("8.8.8.8", 80))
        ip1 = s.getsockname()[0]
    except Exception as erro:
        print("Ocorreu um erro:" + str(erro))

    # Lista as interfaces de IP
    interfaces = psutil.net_if_addrs()

    # IP e Mac
    ip_mac = {}

    # Percorre a lista de interfaces e endereços
    for nome_interface, addrs in interfaces.items():
        ip = None
        mac = None

        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip = addr.address
            elif addr.family == psutil.AF_LINK:
                mac = addr.address

        if ip1 == ip:

            ip_mac = {
                "ip": ip,
                "mac": mac
            }

            return ip_mac

    return None