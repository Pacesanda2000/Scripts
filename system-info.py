import socket
import platform


def gather_data():
    #architecture
    platform.architecture()
    print("The architecture of this device is = ",platform.architecture([0]))

    #hostname
    socket.gethostname()
    print("The hostname of this device is = ",socket.gethostname())

    #os
    platform.system()
    print("The os of this device is = ",platform.system())

    #processor
    platform.processor()
    print("The processor of this device is = ",platform.processor())

    #ip_addresses  
    import socket   
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)    
    print("Your Computer IP Address is:", IPAddr)

gather_data()

#def storeln_file():

