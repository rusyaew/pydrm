import random, hashlib
print("l - launch obfuscated\no - obfuscate\nd - deobfuscate")
do,target = input("Enter some command: ").split()
if do == "o":
	print("Loading info...")
	f = open(target, "r")
	target_info = f.read()
	f.close()
	print("Generating key...")
	hash_count = len(target_info) // 32 + 1
	h = hashlib.md5()
	h.update(bytes([random.randint(0,255)]))
	key=h.hexdigest()
	for i in range(hash_count+1):
		h.update(bytes([random.randint(0,255)]))
		key+=h.hexdigest()
	key_file = open("timezone.ini", "w")
	key_file.write(key)
	key_file.close()
	print("Obfuscating...")
	tmp = "{}".format(target_info)
	crypted = int(bytes(tmp, "utf-8").hex(), 16) ^ int(key, 16)
	crypted = "{:x}".format(crypted)
	crypted = bytes.fromhex(crypted)
	cf = open("time.dll", "wb")
	cf.write(crypted)
	cf.close()
	print("Generating launcher...")
	launcher = open("start.py", "w")
	launcher.write("setting=open(\"se\"+\"tt\"+\"ings.py\",\"wb\");dll=open(\"t\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"ime.d\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"ll\", \"rb\");dlldata=dll.read();ini=open(\"ti\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"mezone.ini\",\"r\");inidata=ini.read();ini.close();dll.close();res=\"{:x}\".format(int(dlldata.hex(),16) ^ int(inidata,16));res=bytes.fromhex(res);setting.write(res);setting.close()\nfrom settings import main\nmain()\nwith open(\"se\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"tt\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"\"+\"ings.py\",\"wb\"):\n	   pass")
	launcher.close()
	print("Complete!")