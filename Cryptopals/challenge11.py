#Convert hex to base64

import base64
import binascii #bonus

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

hex_bytes = bytes.fromhex(string)
base64_string = base64.b64encode(hex_bytes)

print (base64_string)
#b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

'''bonus'''
print (binascii.unhexlify(string))
#b"I'm killing your brain like a poisonous mushroom"
