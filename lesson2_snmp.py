#!/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract


COMMUNITY_STRING = 'galileo'
SNMP_PORT_RTR1 = 7961
SNMP_PORT_RTR2 = 8061
IP = '50.76.53.27'

rtr1_device = (IP, COMMUNITY_STRING, SNMP_PORT_RTR1)
rtr2_device = (IP, COMMUNITY_STRING, SNMP_PORT_RTR2)

# OID for sysName
OID1 = '1.3.6.1.2.1.1.5.0'

# OID for sysDescr
OID2 = '1.3.6.1.2.1.1.1.0'

# --------  Ger data for Rtr1  ------------
snmp_data = snmp_get_oid(rtr1_device, oid=OID1)
sysName = snmp_extract(snmp_data)

snmp_data = snmp_get_oid(rtr1_device, oid=OID2)
sysDesc = snmp_extract(snmp_data)

print '\n------------------------------------------'
print 'sysName = ' + sysName
print 'sysDesc = ' + sysDesc


# --------  Ger data for Rtr2  ------------
snmp_data = snmp_get_oid(rtr2_device, oid=OID1)
sysName = snmp_extract(snmp_data)

snmp_data = snmp_get_oid(rtr2_device, oid=OID2)
sysDesc = snmp_extract(snmp_data)

print '\n------------------------------------------'
print 'sysName = ' + sysName
print 'sysDesc = ' + sysDesc
print '\n'

