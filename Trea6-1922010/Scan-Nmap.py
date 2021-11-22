import nmap
import csv

ip=input("IP Objetivo: ")
nm = nmap.PortScanner()
puertos_abiertos="-p "
results = nm.scan(hosts=ip)#-n -Pn -T4 #arguments="-sT "
count=0
#print (results)
print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())

for proto in nm[ip].all_protocols():
    print("Protocol : %s" % proto)
    print()
    lport = nm[ip][proto].keys()
    sorted(lport)

    for port in lport:
        print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
        if count==0:
            puertos_abiertos=puertos_abiertos+str(port)
            count=1
        else:
            puertos_abiertos=puertos_abiertos+", "+str(port)
        
print("\nPuertos abiertos: "+puertos_abiertos +" - "+str(ip))

#with open("Puertosss.csv", "w") as file:
        #escribir = csv.writer(file)
        #escribir.writerows(puertos_abiertos)