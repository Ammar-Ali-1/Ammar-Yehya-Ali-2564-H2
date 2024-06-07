import socket

def main():
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.connect(('127.0.0.1' , 44444))
    account_number = input("Enter your account number: ")
    client.send(account_number.encode())
    print(client.recv(1024).decode())

    while True:
        print("""Services:
        Press...1...Check Balance.
        Press...2...Deposit.
        Press...3...Withdraw From Balance.
        Press...4...Exit""")
        serviceNum = input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter the service number:")
        
        client.send(serviceNum.encode())
        if serviceNum == '1':
            print(client.recv(1024).decode())
        elif serviceNum == '2':
            amount = input("Enter amount: ")
            client.send(amount.encode())
            print(client.recv(1024).decode())
        elif serviceNum == '3':
            amount = input("Enter amount: ")
            client.send(amount.encode())
            print(client.recv(1024).decode())
        else :
            break
    print(client.recv(1024).decode())
    client.close()
if __name__ == "__main__":
    main()
