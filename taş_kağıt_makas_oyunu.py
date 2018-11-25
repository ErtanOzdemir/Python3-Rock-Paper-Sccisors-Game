###### Taş Kağıt Makas Oyunu > Programmer: Ertan Özdemir #####

import os
import time

player_one_score=0
player_two_score=0


sunu= """

-----------------------------------------
>> Taş, Kağıt, Makas Oyununa Hoş Geldiniz
-----------------------------------------
"""

print(sunu)

player_one_name=input("İlk oyuncu lütfen isminizi girin:")
player_one_name=player_one_name.title()

player_two_name=input("İkinci oyuncu lütfen isminizi girin:")
player_two_name=player_two_name.title()

while True:
	options="""
	--------------
	|  1) Taş    |
	|  2) Kağıt  |
	|  3) Makas  |
	|  4) Sonuç  |
	--------------
	"""

	print(options)
	player_one_option=input("{} yukarıda ki bir seçeneği seç: ".format(player_one_name))
	os.system('cls' if os.name=="nt" else "clear")

	print(options)
	player_two_option=input("{} yukarıda ki bir seçeneği seç: ".format(player_two_name))
	os.system('cls' if os.name=="nt" else "clear")

	if player_one_option == "4" or player_two_option =="4":
		print("""
			{}:{}
			{}:{}""".format(player_one_name,player_one_score,player_two_name,player_two_score))
		input("Çıkış için bir tuşa basın!")
		break
	else:
		pass

	print("TAŞ")
	time.sleep(1)

	print("KAĞIT")
	time.sleep(1)

	print("MAKAS")
	time.sleep(3)

	os.system('cls' if os.name=="nt" else "clear")

	if player_one_option=="1" and player_two_option=="1": 
		print("{} TAŞI, {} ise TAŞI seçti! BERABERE!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		os.system('cls' if os.name=="nt" else "clear")
		pass


	elif player_one_option=="1" and player_two_option=="2":
		print("{} TAŞI, {} ise KAĞIDI seçti!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		player_two_score+=1
		os.system('cls' if os.name=="nt" else "clear")

	elif player_one_option=="1" and player_two_option=="3": 
		print("{} TAŞI, {} ise MAKASI seçti!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		os.system('cls' if os.name=="nt" else "clear")
		player_one_score+=1
	
	elif player_one_option=="2" and player_two_option=="2": 
		print("{} KAĞIT, {} ise KAĞIDI seçti! BERABERE!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		os.system('cls' if os.name=="nt" else "clear")
		pass

	elif player_one_option=="2" and player_two_option=="1": 
		print("{} KAĞIT, {} ise TAŞI seçti!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		player_one_score+=1
		os.system('cls' if os.name=="nt" else "clear")

	elif player_one_option=="2" and player_two_option=="3": 
		print("{} KAĞIT, {} ise MAKASI seçti!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		player_two_score+=1
		os.system('cls' if os.name=="nt" else "clear")

	elif player_one_option=="3" and player_two_option=="3": 
		print("{} MAKAS, {} ise MAKASI seçti! BERABERE!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		os.system('cls' if os.name=="nt" else "clear")
		pass

	elif player_one_option=="3" and player_two_option=="1": 
		print("{} MAKAS, {} ise TAŞI seçti!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		player_two_score+=1
		os.system('cls' if os.name=="nt" else "clear")

	elif player_one_option=="3" and player_two_option=="2": 
		print("{} MAKAS, {} ise KAĞIDI seçti!".format(player_one_name,player_two_name))
		input("Devam etmek için bir tuşa basın...")
		player_one_score+=1
		os.system('cls' if os.name=="nt" else "clear")
	else:
		print("HATALI DEĞER GİRMİŞ OLABİLİR MİSİN?")

	