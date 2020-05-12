# DNSdegistirici
Linux sistemler için basit ve hızlı DNS değiştirme aracı

# Araç Hakkında
DNSdegistirici /etc/resolv.conf dosyasını düzenleyerek Linux sistemlerde DNS adresini değiştiren basit bir araçtır. Sızma testi ve etik hackerlık uygulamaları yapmak isteyenlerin yaşadıkları DNS değiştirme işlemi sorunlarının önüne geçmek için yazılmıştır.
Aracın kurulumu ve kullanımı oldukça kolaydır.

![Arayüz Ekran Görüntüsü](https://raw.githubusercontent.com/ahmetemindilben/DNSdegistirici/master/Ekran%20G%C3%B6r%C3%BCnt%C3%BCleri/arayuz.png)

## Kurulum
### 1. Otomatik Kurulum
Aracı kurabilmek için internet bağlantısı olan herhangi bir linux sistemde aşağıdaki kodu terminale yazmanız yeterlidir. Kodu yazdıktan sonra kurulum ekranı sizi yönlendirecektir.
```
bash <(wget -qO- https://git.io/Jf8cu)
```
Kurulum tamamlandıktan sonra ```sudo dnsdegistir``` komutu ile aracı çalıştırabilirsiniz.

### 2. Manuel Kurulum
* 1. Manuel olarak kurulum yapabilmek için ilk olarak bu depodaki dosyaları sisteminize indirin.
* 2. Dosyaları indirdiğiniz dizinde bir terminal açın ve bash install.sh komutu ile kurulum scriptini açın.
* 3. Kurulum ekranı sizi yönlendirecektir.
* 4. Kurulum tamamlandıktan sonra ```sudo dnsdegistir``` komutu ile aracı çalıştırabilirsiniz.

## KULLANIM
DNSdegistirici aracı ile DNS adresini değiştirmek için iki yöntem bulunmaktadır;

### 1. Rastgele DNS Adresleri Kaydetme
Otomatik DNS adresleri kaydetme yöntemi ile aracın kodu içerisinde bulunan ücretsiz DNS adreslerinden herhangi üç tanesini sisteminize kayıt edebilirsiniz. 

![Rastgele DNS Ekran Görüntüsü](https://raw.githubusercontent.com/ahmetemindilben/DNSdegistirici/master/Ekran%20G%C3%B6r%C3%BCnt%C3%BCleri/otomatikDNS.png)

### 2. Manuel DNS Adresleri Kaydetme
Manuel DNS adresleri kaydetme yöntemi ile kendi istediğiniz DNS adreslerini sisteme kayıt edebilirsiniz.

![Rastgele DNS Ekran Görüntüsü](https://raw.githubusercontent.com/ahmetemindilben/DNSdegistirici/master/Ekran%20G%C3%B6r%C3%BCnt%C3%BCleri/manuelDNS.png)

# Aracın Test Edildiği Sistemler

DNSdegistirici aracı birçok Linux sistemine uygun olmakla beraber bazı durumlarda belirli sistemlerde hatalar verebilir. Herhangi bir hatayla karşılaşmanız durumunda hata@ahmetemindilben.com.tr mail adresine mail atabilirsiniz.</p>

• Kali Linux 2019.4 ve öncesi:</strong> Araç sorunsuz çalışmaktadır.
• Kali Linux 2020.1 ve sonrası:</strong> Araç sorunsuz çalışmaktadır. 
• Ubuntu: Araç geliştirme çalışmaları devam etmektedir.

# Sorumluluk Reddi Beyanı
Bu araç yalnızca eğitim amacıyla yasal sınırlar çerçevesinde kullanılmak için yazılmıştır. Aracın kullanımından kaynaklanabilecek her türlü durumda sorumluluk tarafınıza aittir.

# Lisans (License)
Bu proje MIT Lisansı altında yayınlanmıştır - detayları görüntülemek için [LICENSE.md](LICENSE.md)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
