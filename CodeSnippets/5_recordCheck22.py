#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

import dns.resolver


def get_records(domain):
    ids = ['A', 'AAAA', 'SOA', 'CNAME', 'MX', 'NS', 'PTR', 'CERT', 'SRV', 'TXT']

    
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
    a = open("list.22.smokingwheels.github.io.domains", "r") # For checking DNS while other one runs
    b = open("list22_valid.txt", "w") # For the shorter valid types
    c = open("list22_invalid.txt", "w") # For the shorter invalid types
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
    
