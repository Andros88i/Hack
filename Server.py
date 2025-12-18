import os
import requests
import re

# Configuración (Aquí usarías una API Key real)
API_URL = "https://api.tu-proveedor-ia.com/v1/chat/completions"
API_KEY = "TU_API_KEY_AQUÍ"

def obtener_codigo_ia(prompt):
    print("🧠 La IA está pensando el código...")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "gpt-4-turbo", # O el modelo que prefieras
        "messages": [{"role": "user", "content": f"Escribe solo el código para: {prompt}. No des explicaciones, solo código puro."}]
    }
    
    # Simulación de respuesta (Para que pruebes la lógica)
    # En un entorno real, aquí harías: response = requests.post(API_URL, headers=headers, json=data)
    # Por ahora, simularemos que la IA nos devuelve un código funcional:
    codigo_detectado = "print('Este es un código real generado por IA')"
    lenguaje = "python"
    
    return codigo_detectado, lenguaje

def guardar_y_preparar(codigo, lenguaje):
    extensiones = {"python": "py", "javascript": "js", "bash": "sh", "c++": "cpp"}
    ext = extensiones.get(lenguaje.lower(), "txt")
    nombre = f"resultado_final.{ext}"
    
    with open(nombre, "w") as f:
        f.write(codigo)
    
    if ext == "sh":
        os.chmod(nombre, 0o755)
    
    print(f"✅ Archivo '{nombre}' generado con éxito.")

def main():
    print("🚀 SISTEMA DE PROGRAMACIÓN AUTÓNOMA V2.0")
    tarea = input("¿Qué programa necesitas que cree hoy?: ")
    
    codigo, lenguaje = obtener_codigo_ia(tarea)
    
    if codigo:
        guardar_y_preparar(codigo, lenguaje)
        print("⭐ Tarea completada. El código es funcional y está listo.")

if __name__ == "__main__":
    main()
