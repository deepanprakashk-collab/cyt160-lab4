11. Analysis Questions:

Q1 – Answer:

I saw a total of 1 alert event each time I executed the command.
Explanation: The type threshold sets a threshold of 100 counts, so within 60 second window of time, for 150 messages that was sent, the threshold was met only once. Instead of creating alerts all the time the threshold keyword only triggers an alert after a specific volume of traffic is detected – this stops unnecessary alert messages from low volume legitimate traffic.

Q2 – Answer:

Inspection: Suricata can inspect the payload on the port 1883 because it is unencrypted and it is in plaintext. It cannot read the payload on the port 8883 due to TLS encryption – the payload will be in ciphertext format. Without a decryption key, Suricata cannot see the payload.
Trade-offs: Testing on plaintext is faster and easier for validating the rules and debugging, but its less secure. Testing on TLS suits for more realistic scenarios but it needs complex certificate management, and it is slow because of encryption and decryption.

Q3 – Answer:

No, it will not fire. Because the depth is only 100 byes. If the text pattern starts only at 200th byte then it is out of bounds for the rule to detect. 
Changes that can be made: We can increase the depth to 300 or 400 bytes or we can add an offset value – say 150 – to make Suricata look after the150th byte.

Q4 – Answer:

Changes that can be done to switch from IDS to IPS:
1.	We can change the alert keyword to drop keyword in the rule file (eg: drop mqtt any any -> any any…)
2.	We can change the mode from af-packet (passive sniffing) to NFQ (Netfilter Queue) mode  or  we can set the af-packet configuration to copy-mode: ips within the suricata.yml file. This will block the packets.
