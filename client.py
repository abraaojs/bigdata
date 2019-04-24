# -*- coding: utf-8 -*-
"""
created by Abraão Silva

@uthor abraaosilva
"""

from urllib import request


date_bolsa = "date_bolsa=" + input("Date Bolsa: ")
open_bolsa = "open_bolsa=" + input("Open Bolsa: ")
high_bolsa = "high_bolsa=" + input("High Bolsa: ")
low_bolsa =  "high_bolsa=" + input("Low Bolsa: ")
close_bolsa = "close_bolsa=" + input("Close Bolsa: ")
volume_bolsa = "volume_bolsa=" + input("Volume Bolsa: ")

url_path = 'http://localhost:5000/api?%s&%s&%s&%s'%(date_bolsa,
                                                    open_bolsa,
                                                    high_bolsa,
                                                    low_bolsa,
                                                    close_bolsa,
                                                    volume_bolsa)

with request.urlopen(url_path) as response:
    result = str(response.read())

print("A classe para a Bolsa com {%s, %s, %s, %s} é %s"%(date_bolsa,
                                                        open_bolsa,
                                                        high_bolsa,
                                                        low_bolsa,
                                                        close_bolsa,
                                                        volume_bolsa,
                                                        result))
