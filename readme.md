# PortRadar 🔎

Scanner de portas TCP desenvolvido em Python para verificar quais portas estão abertas em um endereço IP ou domínio.

O **PortRadar** permite testar uma porta específica, verificar uma lista de portas conhecidas e realizar uma varredura em um intervalo de portas.

## 🚀 Funcionalidades

- **Porta específica (`-s`):** verifica se uma porta TCP está aberta ou fechada.
- **Portas conhecidas (`-p`):** verifica uma lista de portas associadas a serviços comuns.
- **Intervalo de portas (`-r`):** verifica todas as portas TCP dentro de um intervalo definido.
- **Timeout de conexão:** limita o tempo de espera para cada tentativa de conexão.
- **Tratamento de erros:** informa falhas de conexão e outros erros de socket.

## 🛠️ Tecnologias

- Python 3
- Biblioteca `socket`
- Biblioteca `sys`

Não é necessário instalar dependências externas.

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/claudiotorresarbe/PortHawk.git
```

Entre na pasta do projeto:

```bash
cd PortHawk
```

Execute o programa com Python 3.

## 💻 Como utilizar

### 1. Verificar portas conhecidas

Utilize o parâmetro `-p` para verificar as portas presentes na lista interna do projeto.

```bash
python main.py -p tcpbin.com
```

### 2. Verificar uma porta específica

Utilize o parâmetro `-s`, seguido do endereço e da porta desejada.

```bash
python main.py -s tcpbin.com 4242
```

### 3. Verificar um intervalo de portas

Utilize o parâmetro `-r`, seguido do endereço, da porta inicial e da porta final.

```bash
python main.py -r tcpbin.com 4240 4242
```

Nesse exemplo, serão verificadas as portas `4240`, `4241` e `4242`.

## 📋 Exemplos de saída

A saída depende do estado da porta e da disponibilidade do servidor remoto.

```text
######################################################################
Address: tcpbin.com
######################################################################
Address/port: tcpbin.com:4242 _____________________________aberto
```

Quando a conexão não é aceita, o programa pode retornar:

```text
Address/port: tcpbin.com:4240 ____________________________fechada
```

Os resultados variam conforme a disponibilidade do destino, as regras de firewall e as condições da rede.

## 📚 Portas verificadas

O projeto inclui uma lista de portas frequentemente associadas a serviços de rede, incluindo:

| Porta | Serviço |
|---:|---|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 445 | SMB |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 8080 | HTTP alternativo |
| 27017 | MongoDB |

A lista completa está definida na variável `portas` do código-fonte.

**Importante:** embora a lista contenha serviços que utilizam TCP e UDP, a implementação atual verifica somente conexões TCP.

## ⚙️ Parâmetros disponíveis

| Parâmetro | Descrição | Exemplo |
|---|---|---|
| `-p` | Verifica as portas conhecidas | `python main.py -p tcpbin.com` |
| `-s` | Verifica uma porta específica | `python main.py -s tcpbin.com 4242` |
| `-r` | Verifica um intervalo de portas | `python main.py -r tcpbin.com 4240 4242` |

## ⚠️ Limitações

- O scanner realiza conexões TCP, não uma detecção completa de serviços.
- Uma porta identificada como aberta indica que a conexão TCP foi aceita; isso não confirma qual serviço está sendo executado.
- Uma porta considerada fechada pode estar filtrada, inacessível ou bloqueada pela rede.
- O timeout atual é de cinco segundos por tentativa, o que pode tornar intervalos grandes demorados.
- Os resultados para domínios dependem da resolução DNS e do endereço IP retornado.

## 🔐 Uso responsável

Utilize o PortRadar somente em sistemas, servidores e redes próprios ou para os quais você tenha autorização explícita para realizar testes.

Respeite as políticas dos serviços de terceiros e evite varreduras que possam causar sobrecarga ou violar regras de uso.

## 📄 Licença

Este projeto pode receber uma licença de código aberto, como MIT, caso o autor opte por distribuí-lo nesses termos.