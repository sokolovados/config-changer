from config_changer import conf_parser
import pexpect
telnet = pexpect.spawn('telnet 10.220.43.76')
telnet.expect('[Uu]ser[Nn]ame:')
telnet.sendline('admin')

telnet.expect('[Pp]ass[Ww]ord:')

telnet.sendline('qjd9ud62')

telnet.expect('#')

telnet.sendline('disable clip')
telnet.expect('#')


'''with open('out.txt','w') as out:
    for vlan in range (1,10):
        telnet.sendline('create vlan '+ str(vlan) +' tag ' + str(vlan))
        telnet.expect('#')
        show_output = telnet.before.decode('utf-8')
        out.write(show_output)'''

with open('config.cfg','w') as conf:
    telnet.sendline('sh conf cu')
    telnet.expect('DES-1228/ME:5#', timeout=200)
    show_output = telnet.before.decode('utf-8')
    conf.write(show_output)

conf_parser('config.cfg')
    
    
    
  




