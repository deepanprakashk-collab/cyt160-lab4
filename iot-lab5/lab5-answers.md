11. Analysis Questions:

Q1 – Answer:
3-visible items in plaintext
1.	the channel name “iot/lab/topic” is clearly visible
2.	the JSON output containing the sensor readings like “temp”: 20.5 is readable
3.	Packet headers, like CONNECT or PUBLISH are readable when the client sends the packets.
Attacker Implications: An attacker can eavesdrop and gather information by intercepting the traffic to plan out future attacks. TLS makes this information confidential making it useless for the interceptor.

Q2- Answer:
Testing: Running this command without certificate flag will throw an error message.
Error Message: openSSL Error: error:140890C7:SSL routines:ssl3_get_client_certificate:peer did not return a certificate.
Improvement:  allow_anonymous true can be sued to permit any device to connect. require_certificate true (mTLS) makes sure that there is a mutual authentication. This means that the broker will only talk to clients having a private key signed by our CA. This prevents unauthorized devices trying to connect to the network.

Q3- Answer:
Traffic Observations done by Suricata 
1.	Increase in traffic can indicate a DDoS attack or data exfiltration
2.	Heartbeat signatures can mean that command and control activity
3.	Server Name Indication and certificate validity/Issuer
Threat Detection: A suricata rule can written to alert if any unknown external IP attempts to connect with port 8883 or TLS handshake uses a deprecated weak version (eg: SSLv3) which can mean a downgrade attack.
