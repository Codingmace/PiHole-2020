#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

import dns.resolver


def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain: 
    :return: 
    """
    ids = [
        'A',
        'CNAME',
        'SOA',
        'AAAA',
        'NS',
        'MD',
        'MF',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'ISDN',
        'RT',
        'NSAP',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'TLSA',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'UNSPEC',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
    ]
    
    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                print(a, ':', rdata.to_text())
                return a
            
        except Exception as e:
            print(e)  # or pass
    return "NA"

if __name__ == '__main__':
    a = open("list.13.zerodot1.gitlab.io.domains", "r") # For checking DNS while other one runs
    b = open("list13_valid.txt", "w") # For the shorter valid types
    c = open("list13_invalid.txt", "w") # For the shorter invalid types
    lines = a.readlines()
    for line in lines:
        ans = get_records(line)
        if (ans == "NA"):
            c.write(line)
        else:
            b.write(line)
    a.close()
    b.close()
    c.close()
    
