from collections import defaultdict
from tabulate import tabulate
from sys import argv
config = argv[1]

traffic_segmentation = []
disable_ports = "нет"
changedspeed_ports={}
ports_description= defaultdict(list)
snmp_location = ''
all_vlans = {}
vlan_port_dict_untagged = defaultdict(list)
vlan_port_dict_tagged = defaultdict(list)


with open(config, 'r') as conf:
    for line in conf:
        ###############################LOOPDETECT################################
        if 'loopdetect ports' in line:
            if 'enabled' in line:
                loopdetect_enable = (line.split())[3]
            else:
                loopdetect_disable = (line.split())[3]


        ############################TRAFFIC SIGMENTATION#########################        
        elif 'traffic_segmentation' in line:
            
            traffic_segmentation.append((line.split())[2])
            traffic_segmentation.append((line.split())[4])


        ############################PORTS########################################        
        
            #DISABLE_PORTS
        elif 'config ports' in line:
            if 'state disable' in line:
                disable_ports = (line.split())[2]
            #CHANGED SPEED    
            if 'speed' in line:
                if not 'speed auto' in line:
                    changedspeed_ports[(line.split())[2]] = (line.split())[4]
            #DESCRIPTION
            if 'description' in line:
                if 'clear_description' in line:
                    pass
                else:
                    ports_description[(line.split())[2]].append((line[(line.find("description ")+13)::]).strip('\n'))
        #########################SNMP LOCATION##################################
        if 'system_location' in line:
            snmp_location = (line.split())[3]

        ###########################VLAN#########################################
        #ALL VLAN
        if 'create vl"burnakovka-1.6"
iso.3.6.1.2.1.1.6.0 = STRING: "Burnakovskaja55p2"
iso.3.6.1.2.1.1.7.0 = INTEGER: 3
iso.3.6.1.2.1.1.8.0 = Timeticks: (1637150) 4:32:51.50an' in line:
            all_vlans[(line.split())[2]] = (line.split())[4]
            all_vlans_view = defaultdict(list)
            all_vlans_view[(line.split())[2]].append((line.split())[4])

        #VLAN PORTS

        
        if 'config vlan' in line:
            if 'delete' in line:
                deleted_vlan = line.split()[2]

            if 'tagged' in line:
                ports = (line.split())[5]
                if 'untagged' in line:
                    if deleted_vlan in line:
                        pass
                        
                    elif '-' in ports:   
                        for port in range(int(ports.split('-')[0]),int(ports.split('-')[1])+1):

                            vlan_port_dict_untagged[port].append(all_vlans[((line.split())[2])])
                    else:
                        vlan_port_dict_untagged[ports].append(all_vlans[((line.split())[2])])
                else:
                    for port in range(int(ports.split('-')[0]),int(ports.split('-')[1])+1):
                        vlan_port_dict_tagged[port].append(all_vlans[((line.split())[2])])

a = '''



'''
print(a)
#LOOPDETECT
print('-'*20)
print ('loopdetect включен на портах:',loopdetect_enable)
print ('loopdetect выключен на портах:',loopdetect_disable)

#TRAFFIC SIGMENTATION 
print('-'*20)
print ('Сигментация траффика:',traffic_segmentation[0],'->',traffic_segmentation[1],'|',traffic_segmentation[2],'->',traffic_segmentation[3])

#PORTS
print('-'*20)
print('отключенные порты:', disable_ports)

print('скорость портов:',changedspeed_ports)

print(tabulate(ports_description, headers='keys',tablefmt='grid'))

#SNMP LOCATION
print('-'*20)
print('snmp location:',snmp_location)

#VLAN
print(
'''


''')
print('Все созданные VLAN: ',','.join(list(all_vlans.values())),'''

''')

print('untagged')
print(tabulate(vlan_port_dict_untagged,headers='keys', tablefmt='grid'))

print('tagged')
print(tabulate(vlan_port_dict_tagged,headers='keys', tablefmt='grid'))


