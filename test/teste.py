from src.monitor.software.processos import capturar_processos

processos = capturar_processos(5)

for p in processos:
    print(p)