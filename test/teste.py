from src.monitor.software.processos import capturar_processos
from src.monitor.hardware.disco import info_disco

# import time
#
# while True:
#     lista_processos = capturar_processos(3)
#
#     if lista_processos:
#         for p in lista_processos:
#             if float(p['uso_cpu']) > 0:
#                 print(f"Processo: {p['nome']} | PID: {p['pid']} | Usuário: {p['usuario']} | Uso CPU: {p['uso_cpu']} | Memória: {p['memoria']}")
#     time.sleep(5)

# disco = info_disco(plataforma="Linux")
#
# info = disco[0]
#
# print(info['total'])

