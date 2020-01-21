from collections import defaultdict
from sys import argv



def conf_parser(config):

    traffic_segmentation = []
    disable_ports = "нет"
    changedspeed_ports={}
    ports_description= {}
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
                        ports_description[(line.split())[2]] = (line[(line.find("description ")+13)::]).strip('\n')
            #########################SNMP LOCATION##################################
            if 'system_location' in line:
                snmp_location = (line.split())[3]

            ###########################VLAN#########################################
            #ALL VLAN
            if 'create vlan' in line:
                all_vlans[(line.split())[2]] = (line.split())[4]

            #VLAN PORTS
            '''
                config vlan default delete 1-28
                config vlan default advertisement enable
                config vlan default add untagged 25-28
                create vlan Control tag 378
                config vlan Control add tagged 25-28
                config vlan Control add untagged 24
                create vlan Users tag 1070
                config vlan Users add tagged 25-28
                config vlan Users add untagged 1-23

            '''
            
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


    #                else:
    #                   pass
    #


            

                    
                        

                    







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

    print('description портов:',ports_description)

    #SNMP LOCATION
    print('-'*20)
    print('snmp location:',snmp_location)

    #VLAN
    print('-'*20)
    print("все созданные vlan:", all_vlans)
    print('-'*20)
    print('-'*4,'VLAN-PORT','-'*5)



    for i in vlan_port_dict_tagged:
        print('-'*20)
        print('порт', i)
        for a in vlan_port_dict_tagged[i]:
            print('tagged',(str(vlan_port_dict_tagged[i])).strip('[]'))
            break

    for i in vlan_port_dict_untagged:
        print('-'*20)
        print('порт', i)
        for a in vlan_port_dict_untagged[i]:
            print('untagged',(str(vlan_port_dict_untagged[i])).strip('[]'))
            break