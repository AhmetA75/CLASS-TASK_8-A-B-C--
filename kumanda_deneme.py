import time
import random



class Kumanda():

    def __init__(self, tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT",menu=[],aktif_bağlantılar=["HDMI","VGA","AV","USB","PC","DVI"]):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal= kanal
        self.menu=menu
        self.aktif_bağlantılar=aktif_bağlantılar

        
       
    def tv_ac(self):

        if (self.tv_durum  == "Kapalı"):
            print("Tv açılıyor")
            self.tv_durum="Açık"
        else:
            print("Tv zaten acik")

    def tv_kapat(self):
        
        if (self.tv_durum  == "Kapalı"):
            print("Tv zaten kapalı")
        
        else:
            print("Tv zaten kapaniyor")
            self.tv_durum="Kapalı"

    def bağlantı_ekle(self,bağlantı):
    
        if bağlantı in self.aktif_bağlantılar:
            print("Bağlantı zaten var")
        else:
            print("Bağlantı ekleniyor...")
            time.sleep(1)
            self.aktif_bağlantılar.append(bağlantı)
            print("Bağlantı listesi: {}".format(self.aktif_bağlantılar))
    def bağlı_cihazlar(self):
        print("Bağlı cihazlar: {}".format(self.aktif_bağlantılar))

    def ses_ayari(self):

        while True:

            cevap=input("Sesi artır :>\nSesi azalt: <\nÇıkış: q")

            if (cevap=='>'):
                if self.tv_ses>=100:
                    print("Max Ses")
                else:
                    self.tv_ses+=1
                print("Tv Sesi: {}".format(self.tv_ses))
            
            elif (cevap=="<"):
                if (self.tv_ses<=0):
                    print("Min ses")
                else:
                    self.tv_ses-=1
                print("tv_ses: {}",format(self.tv_ses))
            elif (cevap=="q"):
                break
            else:
                print("hatalı tuşlama")

    def kanal_ekle(self,kanal):
        if kanal in self.kanal_listesi:
            print("Kanal zaten var")
        else:
            
            print("Kanal ekleniyor...")
            time.sleep(1)
            

            self.kanal_listesi.append(kanal)

            print("Kanal listesi: {}".format(self.kanal_listesi))
    
    def menu_in(self,menu_fonks):
        print("Menuye girdiniz")
        if  menu_fonks in self.menu :
            print("Menu zaten var")
        elif self.menu.append(menu_fonks):
            print("Menu eklendi")

        
        print(self.menu)       

        

    def kanal_sec(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]
        print(self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv_durum: {}\ntv_ses: {}\nkanal listesi: {}\nkanal:{}\nmenu:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal,self.menu)

print("""

        1. TV aç
        2. TV kapat
        3. Ses Ayarları
        4. Kanal Ekle
        5. Açık Kanalı Öğren
        6. Kanal Sayısı
        7. TV Bilgileri
        8. Menu
        9. Bağlıantı Ekle
        10. Bağlı Cihazlar

Çıkmak için q'ya bas.

""")
kumanda=Kumanda()

while True:

    islem= input("İslem seçiniz")

    if islem =="q":
        print("Sonlandırılıyor")
     
    elif islem =="1":
        kumanda.tv_ac()
    
    elif islem=="2":
        kumanda.tv_kapat()

    elif islem=="3":
        kumanda.ses_ayari()
    
    elif islem=="4":

    

        kanal_isimleri=input("Kanal isimlerini lütfen , ile ayırarak giriniz.")

        x=kanal_isimleri.split(",")

        for i in x:
            kumanda.kanal_ekle(i)
    
    elif islem=="5":
        kumanda.kanal_sec()

    elif islem=="6":
        print("Kanal sayısı: ",len(kumanda))
    
    elif islem=="7":
        print(kumanda)
    
    elif islem=="8":
        menu_fonks=input("Menuye eklemek istediginiz fonksiyonu giriniz")
        kumanda.menu_in(menu_fonks)
        print("Fonksiyon Eklendi")
        
    elif islem=="9":
        bağlantı=input("Bağlantıyı giriniz")
        kumanda.bağlantı_ekle(bağlantı)
    
    elif islem=="10":
        kumanda.bağlı_cihazlar()
    
    else:
        print("hatalı Tuşlama")

# Please read !!!
# Last two functions(islem==9, islem==10) added for assaginment by Ahmet Akçay
