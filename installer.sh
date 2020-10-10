#!/bin/bash
#-*- coding:UTF-8 -*-
#
#         BASİT  ██     ███████       ██       ██████ 
#               ████   ░██░░░░██     ████     ██░░░░██
#              ██░░██  ░██   ░██    ██░░██   ██    ░░ 
#             ██  ░░██ ░███████    ██  ░░██ ░██       
#            ██████████░██░░░██   ██████████░██       
#           ░██░░░░░░██░██  ░░██ ░██░░░░░░██░░██  ██ ██
#           ░██     ░██░██   ░░██░██     ░██ ░░███████ 
#           ░░      ░░ ░░     ░░ ░░      ░░   ░░░░██░  
#
#  ██    ██ ██     ██ ██   ██ ██       ████████ ██    ██ ██   ██████  ██
# ░░██  ██ ░██    ░██░██  ██ ░██      ░██░░░░░ ░░██  ██ ░██  ██░░░░██░██
#  ░░████  ░██    ░██░██ ██  ░██      ░██       ░░████  ░██ ██    ░░ ░██
#   ░░██   ░██    ░██░████   ░██      ░███████   ░░██   ░██░██       ░██
#    ░██   ░██    ░██░██░██  ░██      ░██░░░░     ░██   ░██░██       ░██
#    ░██   ░██    ░██░██░░██ ░██      ░██         ░██   ░██░░██    ██░██
#    ░██   ░░███████ ░██ ░░██░████████░████████   ░██   ░██ ░░██████ ░██
#    ░░     ░░░░░░░  ░░   ░░ ░░░░░░░░ ░░░░░░░░    ░░    ░░   ░░░░░░  ░░  1.0
#
#   ==> BASİT DNS DEĞİŞTİRME ARACI (dnsdegistir) - ARAÇ KURULUM SCRIPTI <==
#   --> BU ARAÇ YALNIZCA EĞİTİM AMAÇLI KULLANILMAK İÇİN GELİŞTİRİLMİŞTİR <--
#     --> KULLANIMINDAN OLUŞABİLECEK DURUMLARDA SORUMLULUK SİZE AİTTİR <--
#
#           -> -> -> -> ahmetemindilben.com.tr | v1.0 <- <- <- <-
#
# 	    MIT License - Copyright © 2020 ahmetemindilben.com.tr
#  	      --> github.com/ahmetemindilben/DNSdegistirici <--
#
#== == == == KONFİGÜRASYON == == == ==#

KURULUM_DIZINI="/usr/share/doc/dnsdegistir"
BIN_DIZIN_KONUMU="/usr/bin/"

NORMAL='\e[0m'
BLINK='\e[5m'
KALIN='\e[1m'
DIKKAT='\e[1;41m'
UYARI='\e[31m'
ONAY='\e[1;42m'
KONTROL='\e[1;40m'
LOGO='\e[36m'
BASLIK1='\e[1;31m'
BASLIK2='\e[1;1;35m'

#== == == == GİRİŞ EKRANI == == == ==#

clear
echo -e $LOGO "  BASİT  ███████   ████     ██  ████████   "       
echo 	     "         ░██░░░░██ ░██░██   ░██ ██░░░░░░            "       
echo 	     "         ░██    ░██░██░░██  ░██░██                  "       
echo 	     "  █████  ░██    ░██░██ ░░██ ░██░█████████   █████   "
echo 	     " ░░░░░   ░██    ░██░██  ░░██░██░░░░░░░░██  ░░░░░    "
echo 	     "         ░██    ██ ░██   ░░████       ░██           "
echo         "         ░███████  ░██    ░░███ ████████            "
echo -e      "         ░░░░░░░   ░░      ░░░ ░░░░░░░░  DEĞİŞTİRİCİ" $NORMAL
echo ""
echo -e $BASLIK1 "  -> -> Basit ve hızlı DNS değiştirme aracı <- <-" $NORMAL
echo -e $BASLIK2 "   --> --> ahmetemindilben.com.tr | v1.0 <-- <--" $NORMAL
echo ""
echo "[NOT:] Kurulum için internet bağlantısı gerekmektedir."
echo "[NOT:] Aracı kullanabilmek için root yetkisi gerekmektedir."
echo ""
echo -e $BLINK"[~] Kuruluma başlamak için herhangi bir tuşa basın:"$NORMAL
read kosulKabul

#== == == == KULLANIM KOŞULLARI KABULU == == == ==#

clear
echo -e $KALIN $DIKKAT"KULLANIM KOŞULLARI"$NORMAL $UYARI
echo ""
echo "'Basit DNS Değiştirici' veya 'dnsdegistirici' yalnızca sızma testlerinde ve etik hackerlık uygulamalarında eğitim amacıyla yasal sınırlar çerçevesinde kullanılmak için yazılmıştır."
echo ""
echo "Araç linux sistemindeki /etc/resolv.conf dosyasını düzenleyerek DNS adreslerini değiştirir. DNS adreslerini otomatik değiştirmek için Level3, OpenDNS, Google DNS ve Verisign gibi internet üzerinden bulunabilen ücretsiz DNS adresleri kullanılmaktadır."
echo ""
echo "Aracın kullanımından oluşabilecek her türlü durumda sorumluluk tarafınıza ait olduğu gibi ahmetemindilben.com.tr herhangi bir sorumluluk almayacaktır."
echo ""
echo "Bu aracı kullanarak, sistemlerinizde barındırarak veya hizmetlerinden yararlanarak bu koşulları kabul ettiğiniz gibi bu aracı yasal sınırlar çerçevesinde kullanacağınızıda kabul etmiş sayılırsınız."
echo ""   
echo "Araç açık kaynaklı ve MIT lisanslıdır. Aracın kaynak kodlarına erişebilir, aracı geliştirebilir ve web siteme atıf yaparak yayınlayabilirsiniz." 
echo -e $NORMAL""
echo "[!] Koşulları kabul ederek devam etmek için 'ENTER', kurulumu iptal etmek için 'CTRL+C' tuşlarına basın:"
read kosulKabul

#== == == == KLASÖR KONTROLÜ == == == ==#

clear
echo -e $KONTROL"[✔?]~ KLASÖRLER KONTROL EDİLİYOR.. ~[?✔] "$NORMAL
echo ""
if [ -d "$KURULUM_DIZINI" ]; then
	echo "[!?]~ 'dnsdegistir' adında bir klasör zaten mevcut, üstüne yazılsın mı? (y/n): ~[?!]"
	read cevap
	if [ "$cevap" = "y" ]; then
		rm -R "$KURULUM_DIZINI"
	else
		echo -e $KALIN $DIKKAT"[✘!] KURULUM İPTAL EDİLDİ [!✘]"$NORMAL
		exit
	fi
fi

#== == == == KURULUM İŞLEMİ == == == ==#

clear
echo -e $KONTROL"[✔]~ Kurulum Başlatılıyor.. ~[✔] "$NORMAL
echo ""
echo -e $BLINK $KONTROL"Gerekli paketler indiriliyor.."$NORMAL
echo ""
sleep 1.5
apt-get install git -y
apt-get install python2.7 -y
git clone https://github.com/ahmetemindilben/DNSdegistirici.git "$KURULUM_DIZINI"
echo "#!/bin/bash
python $KURULUM_DIZINI/DNSdegistir.py" '${1+"$@"}' > dnsdegistir
chmod +x dnsdegistir;
sudo cp dnsdegistir /usr/bin/
rm dnsdegistir
cp -p $KURULUM_DIZINI/dnsdegistir.1.gz /usr/share/man/man1/
cd /usr/share/man/man1 
mandb

#== == == == KURULUM TAMAMLAMA == == == ==#

clear
if [ -d "$KURULUM_DIZINI" ] 
	then
	echo ""
	echo -e $KALIN $BLINK $ONAY"[✔] KURULUM TAMAMLANDI [✔] "$NORMAL
	echo ""
	echo -e $ONAY "[✔] ==> == == == == == == == == == == == == == == == == == == <== [✔] "$NORMAL
	echo -e $ONAY "[✔] =>   sudo dnsdegistir yazarak aracı çalıştırabilirsiniz   <== [✔] "$NORMAL
	echo -e $ONAY "[✔] ==> == == == == == == == == == == == == == == == == == == <== [✔] "$NORMAL
	echo ""
else
	echo -e $KALIN $DIKKAT"[✘!] KURULUM BAŞARISIZ OLDU [!✘]"$NORMAL
	exit
fi
