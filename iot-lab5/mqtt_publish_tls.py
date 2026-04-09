import paho.mqtt.client as mqtt
import ssl, time, json

# --- CONFIGURATION ---
BROKER = '13.220.69.89'  # Your AWS Public IP
PORT   = 8883            # TLS port
TOPIC  = 'iot/lab/topic'

# Adjusted paths for your specific Raspberry Pi username
CA   = '/home/deepan-raspberrypi5/mqtt-certs/ca.crt'
CERT = '/home/deepan-raspberrypi5/mqtt-certs/client.crt'
KEY  = '/home/deepan-raspberrypi5/mqtt-certs/client.key'

# Updated for Paho-MQTT 2.x compatibility
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id='rpi-tls-client')

# Configure TLS - Mutual Authentication - provide the CA to verify the broker, and our
# client certificate so the broker can verify us (mutual TLS)
client.tls_set(
    ca_certs=CA,
    certfile=CERT,
    keyfile=KEY,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# Required for this lab due to dynamic AWS IP addresses.
# IN PRODUCTION: This should be False to prevent Man-in-the-Middle attacks.
client.tls_insecure_set(True)

print('[*] Connecting to broker with TLS...')
client.connect(BROKER, PORT, 60)
print('[*] Connected.')

for i in range(10):
    payload = json.dumps({"device": "rpi-tls-client", "temp": 20 + i * 0.5, "unit": "C"})
    client.publish(TOPIC, payload)
    print(f' Sent: {payload}')
    time.sleep(1)

client.disconnect()
print('[*] Done.')
