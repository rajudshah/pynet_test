#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

# Read cisco_ipsec.text file using CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

# Find all entries that begin with crypto map CRYPTO
crypto_map =  cisco_cfg.find_objects(r"^crypto map CRYPTO")

# Now print the CRYPTO map entries found
print "\nPrinting the crypto map CRYPTO entries found\n"
for i in crypto_map:
    print i.text
print "\n"

# Find all entries that are using pfs group2
crypto_PFS = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map", childspec=r"pfs group2")

# Print all crypto map using pfs group2
print "\nPrinting the crypto map entries using pfs group2\n"
for i in crypto_PFS:
    print i.text
print "\n"


# Find all crypto maps that are not usind AES transform-set
crypto_noAES =  cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"set transform-set AES")

# Print all maps without AES and config under eact.
print "\nPrinting the crypto map entries using pfs group2\n"
for i in crypto_noAES:
    print i.text
    for j in i.children:
        print j.text



