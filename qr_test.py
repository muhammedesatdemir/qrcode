import qrcode
import qrcode.constants

#değişken qrcode olarak tanımlandı
code = qrcode.QRCode(
    version = 1,   #boyut(kare sayısı)(40'a kadar gider) 1 -> 21x21(küçük url'lerde yeterli)
    error_correction = qrcode.constants.ERROR_CORRECT_L, #hata düzeltme(farklı seviyeler de var ama küçük ve basit qr'da yeterli)
    box_size = 10, #piksel olarak boyut(her bir kare boyutudur,burada 10x10)
    border = 4     #kenar boşluğu
)

code.add_data(input('Link giriniz : '))  #link eklenir
code.make(fit=True)  #qrcode en uygun boyutta oluşur


image = code.make_image(fill_color="black", back_color="white")    #arka plan beyaz , qrcode siyah
image.save("qrcode1.png") #qrcode çıktısı
