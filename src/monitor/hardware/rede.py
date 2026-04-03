import psutil

def info_rede()-> dict:
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

    # Informações
    info = {
        "upload": upload,
        "download": download
    }
    return info

def info_mac_address()-> dict:
    """
    Função para verificar o endereço macaddress

    """

    interfaces = psutil.net_if_addrs()
    
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                print(f"Interface: {interface}, MAC: {addr.address}")

   # Informações
    info = {
        "interface": interface,
        "mac": addr.address
    }
    # Retorna as informações
    return info

