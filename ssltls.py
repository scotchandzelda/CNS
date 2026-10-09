
import socket
import ssl

hostname = "www.python.org"
port = 443

context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
        print("Secure connection established")
        print("Server:", hostname)
        print("TLS Version:", secure_sock.version())
        print("Cipher Suite:", secure_sock.cipher())

        certificate = secure_sock.getpeercert()

        print("Certificate Subject:", certificate.get("subject"))
        print("Certificate Issuer:", certificate.get("issuer"))
