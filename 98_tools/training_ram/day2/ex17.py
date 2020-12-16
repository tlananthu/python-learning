#ipaddress validation
def ip_val(ipadd):
    l=ipadd.split(".")

    if len(l)!=4:
        return False
    for i in l:
        if int(i) not in range(256):
            return False
    return True
    
print(ip_val("192.168.0.1"))
print(ip_val("192.168.0.1.1"))
print(ip_val("192.168.258.1"))
