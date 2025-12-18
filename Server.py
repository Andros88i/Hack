import requests

# Tus datos
EMAIL = "androsgil527@gmail.com"
PASS = "rocaknrrolla1988"

def login_directo():
    session = requests.Session()
    url = "https://www.terabox.com/api/login" # URL simplificada de ejemplo
    
    payload = {
        "userName": EMAIL,
        "password": PASS
    }
    
    try:
        print("Intentando conectar con TeraBox...")
        response = session.post(url, data=payload)
        
        if response.status_code == 200:
            print("Conexión establecida.")
            return session
        else:
            print(f"Error de acceso: {response.status_code}")
    except Exception as e:
        print(f"Error de red: {e}")

if __name__ == "__main__":
    login_directo()
