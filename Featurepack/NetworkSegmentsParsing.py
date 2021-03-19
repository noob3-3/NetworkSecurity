import ipaddress

def get_ip_list(ip = '192.168.0.0/24'):
    hoostsLList = ipaddress.ip_network(ip).hosts()
    # print(hoostsLList)
    iplist = []
    for i in hoostsLList:
        # print(str(i))
        iplist.append(str(i))
    return iplist

if __name__ == '__main__':
    print(get_ip_list('192.168.0.1/24'))