import sys
import socket

# ponta passiva (servidor): ./dcc023c2 -s <port> <input> <output>
# ponta ativa (cliente):    ./dcc023c2 -c <IP> <port> <input> <output>

if __name__ == "__main__":
    if str(sys.argv[1]) == "c":
        # python client.py 127.0.0.1 1236
        # ip = "127.0.0.1"
        ip = str(sys.argv[2])
        # port = 1234
        port = int(sys.argv[3])

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, port))
        server.listen(5) # limite de conexoes

        while True:
            client, address = server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")
            # Dica: Verificar como montar sequências de bytes com dados específicos (p.ex., inteiros de 16 bits) na linguagem escolhida. 
            # # Por exemplo, no Python, use o pacote struct (funções pack e unpack).
            client.close()
            break

    elif (str(sys.argv[1]) == "s"):
        ip = "127.0.0.1"
        port = 1236

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((ip, port))
        server.close()
