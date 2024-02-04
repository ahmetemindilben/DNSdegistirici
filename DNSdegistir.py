#!/usr/bin/python
#-*- coding:UTF-8 -*-
#
#   BASİT  ███████   ████     ██  ████████        
#         ░██░░░░██ ░██░██   ░██ ██░░░░░░         
#         ░██    ░██░██░░██  ░██░██               
#  █████  ░██    ░██░██ ░░██ ░██░█████████   █████
# ░░░░░   ░██    ░██░██  ░░██░██░░░░░░░░██  ░░░░░ 
#         ░██    ██ ░██   ░░████       ░██        
#         ░███████  ░██    ░░███ ████████         
#         ░░░░░░░   ░░      ░░░ ░░░░░░░░  DEĞİŞTİRİCİ    
#
# ==> ==> BASIT ve HIZLI DNS DEĞİŞTİRME ARACI <== <==
#  -> -> -> ahmetemindilben.com.tr | v1.0  <- <- <-
#
#*YALNIZCA EĞİTİM AMACIYLA KULLANILMAK İÇİN YAZILMIŞTIR*
#*YAŞANABİLECEK HER TÜRLÜ DURUMDA SORUMLULUK SİZE AİTTİR*
#*KULLANIM SÖZLEŞMESİNİ OKUMADAN PROGRAMI KULLANMAYINIZ*
#
# MIT License - Copyright © 2020 ahmetemindilben.com.tr
#
#   --> github.com/ahmetemindilben/DNSdegistirici <--

import os 
import sys, traceback
import time
import random

#== == == == KONFİGÜRASYON == == == ==#

dosyaKonumu = "/etc/resolv.conf" #DNS dosyasının bulunduğu konum (Genelde /etc/resolv.conf)
dnsAdresleri = ["09.244.0.3", "209.244.0.4", "08.67.222.222", "208.67.220.220", "8.8.8.8", "8.8.4.4", "64.6.64.6", "64.6.65.6"]
# dnsAdresleri konfigürasyonu rastgele DNS kayıt etme işlemi için kullanılmaktadır. Bu listede Level3, OpenDNS, Google DNS ve Verisign gibi internetten alınmış ücretsiz DNS adresleri bulunmaktadır.

onayKelimeleri = ["e", "E", "y", "Y", "yes", "YES", "evet", "EVET"]

#== == == == RENKLER == == == ==#

class renk:
	normal = '\033[0m' 
	kalin = '\033[1m'
	altcizgi = '\033[4m'
	uyari = '\033[31m' # arka yok, yazı açık kırmızı
	baslik = '\033[40m' # arka gri, yazı beyaz
	dikkat = '\033[41m' # arka kırmızı, yazı beyaz
	onaylama = '\033[42m' # arka yeşil, yazı beyaz
	duzkirmizi = '\033[91m' # arka yok, yazı kırmızı
	duzyesil = '\033[92m' # arka yok, yazı yeşil
	duzsari = '\033[93m' # arka yok, yazı sarı 
	duzlacivert = '\033[94m' # arka yok, yazı lacivert
	duzmor = '\033[95m' # arka yok, yazı mor
	duzmavi = '\033[96m' # arka yok, yazı mavi

#== == == == TEMEL FONKSİYONLAR == == == ==#

def ekranTemizle():
	os.system("clear")

def baskaIslem():
	islemSoru = raw_input(renk.altcizgi + renk.duzmavi + "\nBaşka bir işlem yapmak istiyor musunuz? (y/n): " + renk.normal)
	if(islemSoru in onayKelimeleri):
		giris()
	else:
		print("Araç kapatılıyor..")
		time.sleep(0.5)


#== == == == LOGO == == == ==#

rastgelerenk = [renk.duzkirmizi, renk.duzyesil, renk.duzsari, renk.duzlacivert, renk.duzmor, renk.duzmavi]
random.shuffle(rastgelerenk)

logo = rastgelerenk[0] + """
  BASİT  ███████   ████     ██  ████████        
        ░██░░░░██ ░██░██   ░██ ██░░░░░░         
        ░██    ░██░██░░██  ░██░██               
 █████  ░██    ░██░██ ░░██ ░██░█████████   █████
░░░░░   ░██    ░██░██  ░░██░██░░░░░░░░██  ░░░░░ 
        ░██    ██ ░██   ░░████       ░██        
        ░███████  ░██    ░░███ ████████         
        ░░░░░░░   ░░      ░░░ ░░░░░░░░  DEĞİŞTİRİCİ       

""" + renk.normal + renk.kalin + rastgelerenk[1] + " -> -> Basit ve hızlı DNS değiştirme aracı <- <-" + renk.normal + rastgelerenk[2] + "\n  --> --> ahmetemindilben.com.tr | v1.0 <-- <--\n" + renk.normal

#== == == == PROGRAM SAYFALARI= = == == ==#

def giris():
	ekranTemizle()
	print(logo)
	print(renk.kalin + renk.dikkat + "	[1]" + renk.normal + " Rastgele DNS Adresleri Gir")
	print(renk.kalin + renk.dikkat + "	[2]" + renk.normal + " Manuel DNS Adresleri Gir")
	print(renk.kalin + renk.dikkat + "	[3]" + renk.normal + " Yardım (Araç Kullanımı)")
	print(renk.kalin + renk.dikkat + "	[4]" + renk.normal + " Kullanım Sözleşmesi")

	print(renk.baslik + renk.kalin + "\n• Mevcut DNS Adresleriniz: " + renk.normal)
	os.system("cat " + dosyaKonumu)
	
	islemSec = raw_input(renk.kalin + renk.duzyesil + "\nBir işlem numarası girin: "+ renk.normal)
	if(islemSec == "1"):
		rastgeleDNS()
	elif(islemSec == "2"):
		manuelDNS()
	elif(islemSec == "3"):
		yardim()
	elif(islemSec == "4"):
		kullanimKosullari()
	else:
		baskaIslem()

def rastgeleDNS():
	ekranTemizle()
	print(renk.kalin + renk.baslik + "Otomatik DNS Adresi kayıt işlemi başlatılıyor.." + renk.normal)	
	print(renk.kalin + renk.dikkat + "DİKKAT: Bu işlemin gerçekleştirilebilmesi için root olmanız gerekmektedir." + renk.normal)
	print(renk.onaylama + "NOT:" +renk.normal + renk.duzyesil + " DNS adresleri değiştirilirken ağ bağlantınız kesilecektir.")
	print("İşlem tamamlandıktan sonra internete tekrardan bağlanmanız gerekebilir." + renk.normal)	
	time.sleep(3)
	print(renk.kalin + renk.duzmavi + "\n• Eski DNS Adresleriniz:" + renk.normal)
	random.shuffle(dnsAdresleri)
	os.system("cat " + dosyaKonumu)
	os.system("chattr -i "+ dosyaKonumu)
	os.system("rm " + dosyaKonumu)
	os.system("touch " + dosyaKonumu)
	os.system("echo nameserver " + dnsAdresleri[0] + " > " + dosyaKonumu)
	os.system("echo nameserver " + dnsAdresleri[1] + " >> " + dosyaKonumu)
	os.system("echo nameserver " + dnsAdresleri[2] + " >> " + dosyaKonumu)
	os.system("chattr +i " + dosyaKonumu)
	os.system("service network-manager restart")
	print(renk.kalin + renk.duzmavi + "\n• Yeni DNS Adresleriniz:" + renk.normal)
	os.system("cat " + dosyaKonumu)
	print(renk.kalin + renk.onaylama + "\n[✓]~ İŞLEM TAMAMLANDI ~[✓]" + renk.normal)
	print("\n• DNS adreslerini yukarıdan kontrol edebilirsiniz.")
	print("• Eğer internete bağlanamıyorsanız rastgele DNS değiştirme işlemini tekrardan uygulayın")
	print(renk.onaylama + "NOT:" +renk.normal + renk.duzyesil + " DNS adresleri kalıcı olarak değiştirildiğinden dolayı bilgisayarı yeniden başlattığınızda tekrardan DNS adreslerinizi değiştirmeye gerek yoktur." + renk.normal)
	baskaIslem()

def manuelDNS():
	ekranTemizle()
	print(renk.kalin + renk.baslik + "Manuel DNS Adresi kayıt işlemi başlatılıyor.." + renk.normal)	
	print(renk.kalin + renk.dikkat + "DİKKAT: Bu işlemin gerçekleştirilebilmesi için root olmanız gerekmektedir." + renk.normal)
	print(renk.onaylama + "NOT:" +renk.normal + renk.duzyesil + " DNS adresleri değiştirilirken ağ bağlantınız kesilecektir.")
	print("İşlem tamamlandıktan sonra internete tekrardan bağlanmanız gerekebilir." + renk.normal)	
	time.sleep(3)
	dnsadresi1 = raw_input(renk.altcizgi + renk.duzyesil + "\n• Girmek istediğiniz 1. DNS adresini yazın:" + renk.normal + " ")
	dnsadresi2 = raw_input(renk.altcizgi + renk.duzyesil + "• Girmek istediğiniz 2. DNS adresini yazın:" + renk.normal + " ")
	dnsadresi3 = raw_input(renk.altcizgi + renk.duzyesil + "• Girmek istediğiniz 3. DNS adresini yazın:" + renk.normal + " ")
	print(renk.kalin + renk.duzmavi + "\n• Eski DNS Adresleriniz:" + renk.normal)
	random.shuffle(dnsAdresleri)
	os.system("cat " + dosyaKonumu)
	os.system("chattr -i "+ dosyaKonumu)
	os.system("rm " + dosyaKonumu)
	os.system("touch " + dosyaKonumu)
	os.system("echo nameserver " + dnsadresi1 + " > " + dosyaKonumu)
	os.system("echo nameserver " + dnsadresi2 + " >> " + dosyaKonumu)
	os.system("echo nameserver " + dnsadresi3 + " >> " + dosyaKonumu)
	os.system("chattr +i " + dosyaKonumu)
	os.system("service network-manager restart")
	print(renk.kalin + renk.duzmavi + "\n• Yeni DNS Adresleriniz:" + renk.normal)
	os.system("cat " + dosyaKonumu)
	print(renk.kalin + renk.onaylama + "\n[✓]~ İŞLEM TAMAMLANDI ~[✓]" + renk.normal)
	print("\n• DNS adreslerini yukarıdan kontrol edebilirsiniz.")
	print("• Eğer internete bağlanamıyorsanız rastgele DNS değiştirme işlemini tekrardan uygulayın")
	print(renk.onaylama + "NOT:" +renk.normal + renk.duzyesil + " DNS adresleri kalıcı olarak değiştirildiğinden dolayı bilgisayarı yeniden başlattığınızda tekrardan DNS adreslerinizi değiştirmeye gerek yoktur." + renk.normal)
	baskaIslem()

def yardim():
	ekranTemizle()
	print(renk.kalin + renk.onaylama + "\n[?]~ YARDIM - ARAÇ KULLANIMI ~[?]" + renk.normal)
	print("""
"Basit DNS Değiştirici" Kali Linux başta olmak üzere Linux sistemlerde DNS değiştirme işleminde yaşanan hataların önüne geçen ve bu işlemi kolaylaştıran açık kaynaklı, kullanımı kolay bir araçtır. 
\nAraç DNS adreslerini değiştirebilmek için /etc/resolv.conf dosyası üzerinde kalıcı düzenleme yapar. Böylelikle bilgisayarınızı yeniden başlattığınızda tekrardan DNS adreslerini değiştirmeniz gerekmez.
\nBasit DNS Değiştirici aracında DNS adreslerinizi değiştirebilmeniz için iki yöntem bulunmaktadır;""")
	print(renk.duzmavi + "\nRastgele DNS Adresleri Gir" + renk.normal + " yöntemi ile aracın kodu içerisinde bulunan ücretsiz DNS adreslerinden rastgele 3 tanesini bilgisayarınızda kullanabilirsiniz.")
     	print(renk.duzmavi + "\nManuel DNS Adresleri Gir" + renk.normal + " yöntemi ile kendi istediğiniz 3 DNS adresini kalıcı olarak girebilirsiniz.")
     	print("\nBu araç açık kaynaklı olmakla beraber geliştirilebilir ve web siteme atıf yapılarak yayınlanabilir.")
	print("\nAracın kullanımına dair daha fazla bilgi için man 'dnsdegistir' komutunu kullanabilirsiniz.")
     	print("\nBu araç sızma testlerinde basit etik hackerlık uygulamalarında yasal sınırlar çerçevesinde kullanılmak amacıyla yazılmıştır. Aracın kullanımından oluşabilecek bütün sorunlar tarafınıza ait olacaktır ve ahmetemindilben.com.tr bu durumdan sorumlu sayılmayacaktır.")
	baskaIslem()

def kullanimKosullari():
	ekranTemizle()
	print(renk.kalin + renk.dikkat + "\n[!]~ KULLANIM KOŞULLARI ~[!]" + renk.normal)
	print("""
   "Basit DNS Değiştirici" veya "dnsdegistirici" yalznıca sızma testlerinde ve etik hackerlık uygulamalarında eğitim amacıyla yasal sınırlar çerçevesinde kullanılmak için yazılmıştır.
   \nAraç linux sistemindeki /etc/resolv.conf dosyasını düzenleyerek DNS adreslerini değiştirir. DNS adreslerini otomatik değiştirmek için Level3, OpenDNS, Google DNS ve Verisign gibi internet üzerinden bulunabilen ücretsiz DNS adresleri kullanılmaktadır.
   \nAracın kullanımından oluşabilecek her türlü durumda sorumluluk tarafınıza ait olduğu gibi ahmetemindilben.com.tr herhangi bir sorumluluk almayacaktır.
   \nBu aracı kullanarak, sistemlerinizde barındırarak veya hizmetlerinden yararlanarak bu koşulları kabul ettiğiniz gibi bu aracı yasal sınırlar çerçevesinde kullanacağınızıda kabul etmiş sayılırsınız.
   \nAraç açık kaynaklı ve MIT lisanslıdır. Aracın kaynak kodlarına erişebilir, aracı geliştirebilir ve web siteme atıf yaparak yayınlayabilirsiniz.
	""")
	baskaIslem()

#== == == == PROGRAM BAŞLATMA == == == ==#

if __name__ == "__main__":
    try:
    	giris()
    except KeyboardInterrupt:
	print(renk.uyari + renk.kalin + " Program kapatılıyor\n" + renk.normal)
        time.sleep(0.50)
