import requests

# Definir la URL a la que enviar el POST request
url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"

# Definir los datos que se enviarán en el cuerpo del request
data = {
    "name": "Javier vivanco",
    "mail": "j.vivanco.astorga@gmail.com",
    "github_url": "https://github.com/Javoopls/challenge_DE.git"
}

# Realizar el POST request
response = requests.post(url, json=data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print("¡El desafío ha sido enviado correctamente!")
else:
    print("Hubo un error al enviar el desafío. Código de estado:", response.status_code)