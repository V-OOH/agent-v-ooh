import psutil

def capturar_processos():
    processos = psutil.process_iter(['username','name','pid','status','memory_info','cpu_percent'])

    print(f"{'USUARIO':<10} | {'PID':<10}  | {'NOME':<15} | {'STATUS':<10}  | {'MEMÓRIA (MB)':<10} | {'UTILIZAÇÂO DE CPU(%)' :<10}") #formatação
    print("-" * 100) #formatação
    
    for proc in processos:  
        p = proc.info 

        usuario = p['username'] 
        if p['username'] != None:
            usuario = p['username'].split('\\')[0] #traz somente o usuario sem o dominio
        else:
            usuario = "Sistema"

        memoria = p['memory_info'].rss #RSS = Resident Set Size - o quanto esta ocupando na RAM naquele momento
        memoriaMB = memoria / (1024*1024) # transformando em MB
   
        print(f"{usuario:<10} | {p['pid']:<10} | {p['name']:<15} | {p['status']:<10} | {memoriaMB:<.2f} | {p['cpu_percent']:<10}")

    
   