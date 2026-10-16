import socket
import time
print("=" * 40)
print("    CyberShield V1.0")
print("=" * 40)
try:
    target = input("Enter the Target IP:")
    start_port = int(input("Enter the Starting Port:"))
    end_port = int(input("Enter the Ending Port:"))

    if start_port < 1 or end_port > 65535:
        print("Error: The Port must be between 1 & 65535")
        exit()

    if start_port > end_port:
        print("Error: Starting Port cannot be greater then Ending Port")
        exit()

    print("Scanning Ports....")

    file = open("scan_results.txt", "w")
    file.write("=" * 40 + "\n")
    file.write("    CyberShield V1.0\n")
    file.write("=" * 40 + "\n")
    file.write(f"Target IP: {target}\n")
    file.write(f"Starting Port: {start_port}\n")
    file.write(f"Ending Port: {end_port}\n")
    file.write("Scanning Ports...\n")

    open_ports = 0
    closed_ports = 0

    start_time = time.time()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target,port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"    
            output = f"[+] Port {port} is OPEN ({service.upper()})"
            print(output)
            file.write(output + "\n")
            open_ports += 1

        else:
            output = f"[-] Port {port} is CLOSED"
            print(output)
            file.write(output + "\n")
            closed_ports += 1


        sock.close()

    end_time = time.time()

    total_ports = open_ports + closed_ports
    scan_time = end_time - start_time

    print("=" * 40)
    print("    Scan Completed!")
    print("=" * 40)
    print(f"Total Ports Scanned: {total_ports}")
    print(f"Open Ports:          {open_ports}")
    print(f"Closed Ports:        {closed_ports}")
    print(f"Scan Time:           {scan_time:.2f}Seconds")
    print("=" * 40)
    
    file.write("=" * 40 + "\n")
    file.write("Scan Completed!\n")
    file.write("=" * 40 + "\n")
    file.write(f"Total Ports Scanned: {total_ports}\n")
    file.write(f"Open Ports:          {open_ports}\n")
    file.write(f"Closed Ports:        {closed_ports}\n")
    file.write(f"Scan Time:           {scan_time:.2f}Seconds\n")
    file.write("=" * 40 + "\n")

    file.close()

    print("scan report saved as 'scan_result.txt'")

except ValueError:
    print("Error: Please enter numbers for the port values.")

except KeyboardInterrupt:
    print("Program Cancelled by user.")

except Exception as e:
    print("An unexpected error occur.", e)



