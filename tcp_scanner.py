import socket # used for low level networking interface
import datetime # used to track scan duration and performance
import sys # used to exit the program with control
import random # used to generate random port numbers
# could do from datetime import datetime, timedelta to shorten the code

port_names = {
    21: "FTP",  22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 135: "MSRPC", 139: "NetBIOS", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S", 3306: "MySQL",
    3389: "RDP",  4444: "Metasploit",  8080: "HTTP-Alt",  8443: "HTTPS-Alt"
}

target = input("Enter IP address or hostname to scan: ")

# examples of good input: scanme.nmap.org, 127.0.0.1 / localhost, 
# google.com

# attempt to resolve the hostname to an IPV4 address using DNS
# socket.gaierror is raised when gethostbyname fails to resolve a hostname
# "gai" stands for "get address info" - this error means:
# - The hostname is invalid or does not exist
# - There is no internet connection
# - DNS resolution failed on the system
# Catching this prevents the program from crashing if the input is invalid

try:
    target_ip = socket.gethostbyname(target) 

    print(f"Scanning host: {target_ip}") #f-string is a formatted string
    # which allows variables or expressions to be embedded 
    # using curly braces

except KeyboardInterrupt:
    print("\nScan interrupted by user. Exiting.")
    sys.exit(0)

except EOFError:
    print("\nNo input detected (Ctrl + Z or end-of-stream). Exiting.")
    sys.exit(0)

except socket.gaierror:
    print("Hostname could not be resolved. Exiting.")
    sys.exit(1) #Stop the program immediately and cleanly; avoids unexpected
    # errors or crashes later in the script, 1 is a general error / handled 
    # failure code

print ("\nChoose scan mode:")
print("1 - Random 100 ports")
print("2 - Common ports (well-known services)")

mode = input("Enter scan mode (1 or 2): ")

if mode == "1":
    port_list = sorted(random.sample(range(1, 65536), 100))

elif mode == "2":
    port_list = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                 993, 995, 3306, 3389, 4444, 8080, 8443] 
   
else:
    print("Invalid mode selected. Defaulting to 100 random ports.")
    port_list = sorted(random.sample(range(1, 65536), 100))

print(f"Scanning {len(port_list)} random ports...")
start_time = datetime.datetime.now() # datetime CLASS inside 
# datetime MODULE

# Loop through the random ports and check which ones are open
for port in port_list:
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET is for the IPv4 Address Family
        # SOCK_STREAM for continuous reliable byte stream (TCP)
        socket.setdefaulttimeout(0.5) # Set a timeout of .5 second 
        # for the connection attempt, prevents hangs or unreachable ports

        # Attempt to connect to the target on the current port
        result = sock.connect_ex((target_ip, port))
        # connect_ex returns an error code instead of 
        # throwing an exception

        if result == 0:
            service = port_names.get(port, "Unknown")
            print(f"Port {port} is OPEN ({service})")
        sock.close()

    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting.")
        sys.exit(0)

    except socket.timeout:
        print(f"Port {port}: Connection timed out.")
        # Happens when a connection takes too long

    except socket.error as e:
        print(f"Port {port}: Socket error occurred -> {e}")
        # General base class for most network-related issues.

    except OSError as e:
    print(f"Port {port}: System-level error → {e}")
    
    except Exception as e:
        print(f"Port {port}: Unexpected error -> {e}")

# Record the time after the scan ends
end_time = datetime.datetime.now()

# Calculate and display the total scan duration
print(f"Scan completed in: {end_time - start_time}")




