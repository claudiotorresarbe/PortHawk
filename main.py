import sys
import socket

portas = [
    [20, "FTP - transferência de dados"],
    [21, "FTP - controle de transferência de arquivos"],
    [22, "SSH - acesso remoto seguro"],
    [23, "Telnet - acesso remoto sem criptografia"],
    [25, "SMTP - envio de e-mails entre servidores"],
    [53, "DNS - resolução de nomes de domínio"],
    [67, "DHCP - servidor de configuração de rede (UDP)"],
    [68, "DHCP - cliente de configuração de rede (UDP)"],
    [69, "TFTP - transferência simples de arquivos (UDP)"],
    [80, "HTTP - tráfego web sem criptografia"],
    [110, "POP3 - recebimento de e-mails"],
    [123, "NTP - sincronização de horário (UDP)"],
    [143, "IMAP - acesso a e-mails"],
    [161, "SNMP - gerenciamento de dispositivos de rede (UDP)"],
    [162, "SNMP Trap - notificações de dispositivos (UDP)"],
    [179, "BGP - roteamento entre sistemas autônomos"],
    [194, "IRC - comunicação por chat"],
    [389, "LDAP - serviço de diretório"],
    [443, "HTTPS - tráfego web criptografado"],
    [445, "SMB - compartilhamento de arquivos Windows"],
    [465, "SMTPS - envio de e-mails com TLS"],
    [500, "IKE - negociação de VPN IPsec (UDP)"],
    [514, "Syslog - envio de registros de sistemas (UDP)"],
    [587, "SMTP Submission - envio de e-mails por clientes"],
    [631, "IPP - impressão pela rede"],
    [636, "LDAPS - LDAP com TLS"],
    [993, "IMAPS - acesso seguro a e-mails"],
    [995, "POP3S - recebimento seguro de e-mails"],
    [1080, "SOCKS - proxy de rede"],
    [1194, "OpenVPN - VPN (frequentemente UDP)"],
    [1433, "Microsoft SQL Server - banco de dados"],
    [1521, "Oracle Database - banco de dados"],
    [2049, "NFS - compartilhamento de arquivos em rede"],
    [2375, "Docker API - acesso sem TLS"],
    [2376, "Docker API - acesso com TLS"],
    [3000, "Servidores de desenvolvimento e aplicações web"],
    [3306, "MySQL - banco de dados"],
    [3389, "RDP - acesso remoto à área de trabalho Windows"],
    [5432, "PostgreSQL - banco de dados"],
    [5672, "RabbitMQ - mensageria AMQP"],
    [5900, "VNC - acesso remoto à interface gráfica"],
    [6379, "Redis - banco de dados em memória"],
    [6443, "Kubernetes API Server - gerenciamento de cluster"],
    [8080, "HTTP alternativo - aplicações web e proxies"],
    [8443, "HTTPS alternativo - aplicações web"],
    [8888, "Jupyter Notebook e outros serviços web"],
    [9092, "Apache Kafka - mensageria e streaming"],
    [9200, "Elasticsearch - API HTTP"],
    [11211, "Memcached - cache em memória"],
    [27017, "MongoDB - banco de dados"]
]

def listen(host,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            resultado = s.connect_ex((host, port))
            if resultado == 0:
                return "aberto"
            else:
                return "fechada"
    except socket.timeout:
        return "Tempo limite excedido."
    except OSError as erro:
        return f"Erro: {erro}"

if __name__ == "__main__":
    l = sys.argv
    if 2 < len(l) < 6 and l[1] in {'-r','-p','-s'}:
        print(70 * '#')
        print(f"Address: {l[2]}")
        print(70 * '#')

    if len(l) == 5 and l[1] == '-r':
        for x in range(int(l[3]), int(l[4])+1):
            r = listen(l[2],x)
            print(f'Address/port: {l[2]}:{x}',r.rjust(40,'_'))
    elif len(l) == 4 and l[1] == '-s':
        r = listen(l[2],int(l[3]))
        print(f'Address/port: {l[2]}:{l[3]}',r.rjust(40,'_'))
    elif len(l) == 3 and l[1] == '-p':
        for x in portas:
            r = listen(l[2],x[0])
            print(f'Address/port: {l[2]}:{x[0]}',r.rjust(40,'_'))
    else:
        print("Uso:")
        print("  python -s main.py <IP> <PORTA>")
        print("  python -p main.py <IP:")
        print("  python -r main.py <IP> <PORTA_INICIAL> <PORTA_FINAL>")
        sys.exit(1)