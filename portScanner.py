import socket
import optparse

class PortScanner:
    def __init__(self):
        pass

    def getValues(self):
        opt = optparse.OptionParser()
        opt.add_option('-p', '--ports', dest='ports', help='port range')
        opt.add_option('-i', '--ip', dest='ip', help='ip address')
        (options, args) = opt.parse_args()

        if not options.ip or not options.ports:
            print("Enter required values or run -h")
            exit(1)
        try:
            start_port, end_port = map(int, options.ports.split(','))
        except ValueError:
            opt.error("Port range is invalid. e.g. -p 20,80")

        return options, start_port, end_port

    def portScanner(self, ip, start_port, end_port):
        for port in range(start_port, end_port + 1):
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP bağlantısı için
            sckt.settimeout(2)  # Timeout değeri
            try:
                result = sckt.connect_ex((ip, port))  # Hata kodunu döner
                if result == 0:
                    print(f"{port} port is open")  # Port açık
                else:
                    print(f"{port} port is closed or filtered")  # Port kapalı
            except socket.timeout:
                print(f"{port} port is timed out")  # Zaman aşımı durumu
            except socket.error as e:
                print(f"Error connecting to port {port}: {e}")  # Hata mesajı
            finally:
                sckt.close()  # Socket'i kapat

pscanner = PortScanner()
options, start_port, end_port = pscanner.getValues()
pscanner.portScanner(options.ip, start_port, end_port)