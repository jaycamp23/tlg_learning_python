ipchk = '192.168.0.1'

if ipchk:
    print('looks like the IP address was set: ' + ipchk)
ipchk = input('apply an ip address: ')
if ipchk:
    print('looks like the IP address was set: ' + ipchk)
else:
    print('you did not provide input.')


ipchk = input('apply an IP address: ')
if ipchk == ' 192.168.70.1':
    print('looks like the ip address of that gateway was set:' + ipchk + ' this is not recommended.')
elif ipchk:
    print('looks like the IP address was set: ' + ipchk)
else:
    print('you did not provide input.')