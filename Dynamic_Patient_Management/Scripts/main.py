import network
import socket
import time

# Configuration Wi-Fi
ssid = "SSID_TO_CHANGE"
password = "PASSWORD_TO_CHANGE"

# Initialisation du Wi-Fi
station = network.WLAN(network.STA_IF)

print("Strating Network interface...")
time.sleep(1)
station.active(False)
time.sleep(1)
station.active(True)

if not station.isconnected():
    print(f"Try connect to SSID : {ssid}")
    station.connect(ssid, password)
    while not station.isconnected():
        print('.', end=" ")
        time.sleep_ms(500)

print("Wi-Fi connecté, adresse IP :", station.ifconfig()[0])

# HTML et CSS pour l'IHM web
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Simulation Patient Dynamique</title>
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
            padding: 30px 20px 20px 20px; /* Plus d'espace en haut */
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
            width: 380px; /* Légèrement plus large pour le logo */
            position: relative;
            min-height: 500px; /* Hauteur minimale pour éviter le chevauchement */
        }
        .logo-container {
            position: absolute;
            top: -15px;
            left: -15px;
            width: 120px;
            height: 120px;
            background-color: #1a1a1a;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        .logo {
            width: 100px;
            height: 100px;
        }
        .title {
            font-size: 24px;
            margin-bottom: 25px;
            color: #00ffff;
            margin-top: 100px; /* Plus d'espace en haut pour éviter le logo */
        }
        .value-display {
            font-size: 36px;
            margin: 15px 0;
            font-weight: bold;
        }
        .control-group {
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 8px;
        }
        .temp-group {
            background-color: rgba(100, 200, 255, 0.2);
            border: 1px solid rgba(100, 200, 255, 0.5);
        }
        .sys-group {
            background-color: rgba(150, 150, 200, 0.2);
            border: 1px solid rgba(150, 150, 200, 0.5);
        }
        .dia-group {
            background-color: rgba(100, 200, 150, 0.2);
            border: 1px solid rgba(100, 200, 150, 0.5);
        }
        .label {
            font-size: 18px;
            margin-bottom: 10px;
            display: block;
        }
        .button {
            width: 50px;
            height: 50px;
            border: none;
            border-radius: 50%;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            margin: 0 10px;
            transition: all 0.3s;
        }
        .minus-btn {
            background-color: #ff4444;
            color: white;
        }
        .plus-btn {
            background-color: #4CAF50;
            color: white;
        }
        .minus-btn:hover {
            background-color: #ff0000;
            transform: scale(1.05);
        }
        .plus-btn:hover {
            background-color: #00C851;
            transform: scale(1.05);
        }
        .button:active {
            transform: scale(0.98);
        }
        .controls-container {
            margin-top: 10px; /* Espace supplémentaire sous le titre */
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Logo officiel de la Croix-Rouge française -->
        <div class="logo-container">
            <svg class="logo" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <!-- Fond rouge avec bordure blanche (style officiel) -->
                <rect x="1" y="1" width="98" height="98" rx="15" fill="#E31837" stroke="#ffffff" stroke-width="1"/>

                <!-- Croix blanche officielle (proportions exactes) -->
                <rect x="33" y="10" width="34" height="80" fill="#ffffff"/>
                <rect x="10" y="33" width="80" height="34" fill="#ffffff"/>

                <!-- Texte "FRANCE" en petit (comme sur le logo officiel) -->
                <text x="50" y="95" font-size="4" text-anchor="middle" fill="#ffffff" font-weight="bold">FRANCE</text>
            </svg>
        </div>

        <h1 class="title">Simulation de Patient Dynamique</h1>

        <div class="controls-container">

        <div class="control-group temp-group">
            <span class="label">Température (°C)</span>
            <div class="value-display" id="temp">{temperature}°C</div>
            <div>
                <button class="button minus-btn" onclick="decrementTemp()">-</button>
                <button class="button plus-btn" onclick="incrementTemp()">+</button>
            </div>
        </div>

        <div class="control-group sys-group">
            <span class="label">Systolique (mmHg)</span>
            <div class="value-display" id="sys">{systolic} mmHg</div>
            <div>
                <button class="button minus-btn" onclick="decrementSys()">-</button>
                <button class="button plus-btn" onclick="incrementSys()">+</button>
            </div>
        </div>

        <div class="control-group dia-group">
            <span class="label">Diastolique (mmHg)</span>
            <div class="value-display" id="dia">{diastolic} mmHg</div>
            <div>
                <button class="button minus-btn" onclick="decrementDia()">-</button>
                <button class="button plus-btn" onclick="incrementDia()">+</button>
            </div>
        </div>
    </div>

    <script>
        let temperature = {temperature};
        let systolic = {systolic};
        let diastolic = {diastolic};

        function updateDisplay() {
            document.getElementById('temp').innerText = temperature + '°C';
            document.getElementById('sys').innerText = systolic + ' mmHg';
            document.getElementById('dia').innerText = diastolic + ' mmHg';
        }

        function sendUpdate() {
            fetch('/set_values?temp=' + temperature + '&sys=' + systolic + '&dia=' + diastolic);
        }

        // Temperature functions
        function incrementTemp() {
            temperature += 1;
            updateDisplay();
            sendUpdate();
        }

        function decrementTemp() {
            temperature -= 1;
            updateDisplay();
            sendUpdate();
        }

        // Systolic functions
        function incrementSys() {
            systolic += 1;
            updateDisplay();
            sendUpdate();
        }

        function decrementSys() {
            systolic -= 1;
            updateDisplay();
            sendUpdate();
        }

        // Diastolic functions
        function incrementDia() {
            diastolic += 1;
            updateDisplay();
            sendUpdate();
        }

        function decrementDia() {
            diastolic -= 1;
            updateDisplay();
            sendUpdate();
        }

        // Initialize display
        updateDisplay();
    </script>
</body>
</html>
"""

# Serveur web
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

# Valeurs initiales
temperature = 37
systolic = 120
diastolic = 80

print("Serveur démarré sur http://" + station.ifconfig()[0])

while True:
    cl, addr = s.accept()
    request = cl.recv(1024).decode()

    # Gestion des requêtes
    if "GET /set_values?" in request:
        # Parse all parameters
        params = request.split("?")[1].split(" ")[0].split("&")
        for param in params:
            if param.startswith("temp="):
                temperature = int(param.split("=")[1])
            elif param.startswith("sys="):
                systolic = int(param.split("=")[1])
            elif param.startswith("dia="):
                diastolic = int(param.split("=")[1])

        print(f"Nouveaux paramètres - Temp: {temperature}°C, Sys: {systolic}mmHg, Dia: {diastolic}mmHg")

    response = html.replace("{temperature}", str(temperature))
    response = response.replace("{systolic}", str(systolic))
    response = response.replace("{diastolic}", str(diastolic))

    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html; charset=UTF-8\r\n\r\n')
    cl.send(response)
    cl.close()

