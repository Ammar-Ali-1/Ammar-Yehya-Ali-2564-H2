import socket
import threading

def startServer():
    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server.bind(('127.0.0.1' , 44444))
    server.listen(5)
    print("Listening on port 44444")

    while True:
        client_socket, address = server.accept()
        print("Connection from" , address , " is established.")
        client_thread = threading.Thread(target = serveClient , args = (client_socket,))
        client_thread.start()
        
def serveClient(client_socket):
    customer_number = client_socket.recv(1024).decode()

    if customer_number in customers:
        client_socket.send(b"Access complete.")
    else:
        client_socket.sentb(b"Your Account Number is invalid. Connection will be terminated.")
        client_socket.close()
        return
    
    while True :
        serviceNum = client_socket.recv(1024).decode()

        if serviceNum == '1':
            balance = customers[customer_number]
            msg = "YOUR BALANCE IS NOW:  " + str(balance)
            client_socket.send(msg.encode())

        elif serviceNum == '2':
            amount = int(client_socket.recv(1024).decode())
            customers[customer_number] += amount
            msg = "DEPOSIT SUCCESSFUL. YOUR BALANCE IS NOW:  " + str(customers[customer_number])
            client_socket.send(msg.encode())

        elif serviceNum == '3':
            amount = int(client_socket.recv(1024).decode())
            if customers[customer_number] >= amount:
                customers[customer_number] -= amount
                msg = "WITHDRAWAL SUCCESSFUL. YOUR BALANCE IS NOW:  " + str(customers[customer_number])
                client_socket.send(msg.encode())
            else:
                msg = "INSUFFICIENT FUNDS, PROCCESS CAN'T BE DONE."
                client_socket.send(msg.encode())
        else:
            break
        
    finalbalance = "THE FINAL BALANCE IS:  " + str(customers[customer_number])
    client_socket.send(finalbalance.encode())
    client_socket.close()


customers = {'00001': 2500 , '00002': 3600 , '00003' : 1800 , '00004' : 6300 , '00005' : 5000}
startServer()