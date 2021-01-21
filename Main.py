Word = input()
Storage = []

def Encrypt():
	Encrypted = ""
	for x in range(1, len(Word) + 1):
		ASCII = ord(Word[x - 1])
		if (x % 2 == 1):
			Check = ASCII - x
			if (Check < 32):
				Encrypted += chr(127 - (x - (ASCII - 32)))
			else:
				Encrypted += chr(ASCII - x)
		else:
			Check = ASCII + x
			if (Check > 127):
				Encrypted += chr(32 + (x + (ASCII - 127)))
			else:
				Encrypted += chr(ASCII + x)
	print(Encrypted)

def Decrypt():
	Decrypted = ""
	for x in range(1, len(Word) + 1):
		Char = ord(Word[x - 1])
		if (x % 2 == 1):
			Check = Char + x
			if (Check > 127):
				Decrypted += chr(32 + (Char - (127 - x)))
			else:
				Decrypted += chr(Char + x)
		else:
			Check = Char - x
			if (Check < 32):
				Decrypted += chr(127 - (x - (Char - 32)))
			else:
				Decrypted += chr(Char - x)
	print(Decrypted)


Encrypt()
Decrypt()
