import os

def generar_codigo(instruccion):
    if "hola mundo" in instruccion.lower():
        return (
            "print('Hola mundo desde Termux')\n"
        ), "python"

    if "bash" in instruccion.lower():
        return (
            "#!/bin/bash\n"
            "echo 'Hola desde un script bash'\n"
        ), "bash"

    return None, None

def guardar_archivo(codigo, lenguaje):
    if lenguaje == "python":
        nombre = "programa.py"
    elif lenguaje == "bash":
        nombre = "programa.sh"
    else:
        return

    with open(nombre, "w") as f:
        f.write(codigo)

    if lenguaje == "bash":
        os.chmod(nombre, 0o755)

    print(f"[✓] Código generado en {nombre}")

def main():
    print("🤖 IA Programadora (Modo educativo)")
    instruccion = input("Describe el programa que quieres: ")

    codigo, lenguaje = generar_codigo(instruccion)

    if codigo:
        guardar_archivo(codigo, lenguaje)
        print("✨ Listo. Puedes revisarlo o ejecutarlo.")
    else:
        print("⚠️ No entendí la instrucción.")

if __name__ == "__main__":
    main()
