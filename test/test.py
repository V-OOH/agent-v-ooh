import platform, subprocess

plataforma = platform.system()

if plataforma == "Linux":
    comando = subprocess.run(
        "cat /proc/cpuinfo | grep 'model name' | head -n 1",
        shell=True,
        capture_output=True,
        text=True
    )

    nome_cpu = comando.stdout.split(":")[1].strip()
    print(f"Resultado: {nome_cpu}")
elif plataforma == "Windows":
    comando = subprocess.run(
        "wmic cpu get name",
        shell=True,
        capture_output=True,
        text=True
    )

    nome_cpu = comando.stdout.split("=")[1].strip()
    print(f"Resultado: {nome_cpu}")