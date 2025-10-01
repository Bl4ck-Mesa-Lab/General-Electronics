import network
import socket

# Configuration Wi-Fi
ssid = "VOTRE_SSID"
password = "VOTRE_MOT_DE_PASSE"

# Initialisation du Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    time.sleep(0.5)

print("Wi-Fi connecté, adresse IP :", sta_if.ifconfig()[0])

# HTML et CSS pour l'IHM web
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Contrôle de Température</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000000;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
        }
        .temperature {
            font-size: 48px;
            margin: 20px 0;
        }
        .button {
            background-color: #333333;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #555555;
        }
        .button:active {
            background-color: #777777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contrôle de Température</h1>
        <div class="temperature" id="temp">{temperature}°C</div>
        <div>
            <button class="button" onclick="decrement()">-</button>
            <button class="button" onclick="increment()">+</button>
        </div>
    </div>
    <script>
        let temperature = {temperature};

        function updateTemperature() {{
            document.getElementById('temp').innerText = temperature + '°C';
            fetch('/set_temp?value=' + temperature);
        }}

        function increment() {{
            temperature += 1;
            updateTemperature();
        }}

        function decrement() {{
            temperature -= 1;
            updateTemperature();
        }}
    </script>
</body>
</html>
"""

# Serveur web
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Serveur démarré sur http://" + sta_if.ifconfig()[0])

while True:
    cl, addr = s.accept()
    request = cl.recv(1024).decode()

    # Gestion des requêtes
    if "GET /set_temp?value=" in request:
        new_temp = int(request.split("value=")[1].split(" ")[0])
        temperature = new_temp
        print(new_temp) # Met à jour l'OLED

    response = html.replace("{temperature}", str(temperature))
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()