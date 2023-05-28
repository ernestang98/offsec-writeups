import itertools
import binascii

# word to crack: collision
# https://emn178.github.io/online-tools/crc32.html
# https://stackoverflow.com/questions/47342250/python-find-crc32-of-string
# https://stackoverflow.com/questions/7074051/what-is-the-best-way-to-generate-all-possible-three-letter-strings

stuff = ['o', '0', 'i', 'l', '1', 's', '5']

keywords = [''.join(i) for i in itertools.product(stuff, repeat = 7)]

for kw in keywords:
	final_string = "c" + kw + "n"
	if str(hex(binascii.crc32(final_string.encode('utf8')))) == "0xf76635ab":
		print(f"Found it: {final_string}")
		break

print("Script end, hopefully we did not fail :)")


