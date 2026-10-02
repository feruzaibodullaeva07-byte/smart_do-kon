# Smart do'kon - mahsulotlar bilan ishlash
nomi = "Non"
narxi = 4000
miqdori = 25

print("Mahsulot:", nomi)
print("Narxi:", narxi, "so'm")
print("Miqdori:", miqdori, "dona")


def mahsulot_qoshish(nomi, narxi, miqdori):
    print("Yangi mahsulot qo‘shildi")
    print("Nomi:", nomi)
    print("Narxi:", narxi, "so‘m")
    print("Miqdori:", miqdori, "dona")
 
mahsulot_qoshish("Sut", 12000, 20)

def qoldiq_tekshir(nomi, miqdori):
    if miqdori < 10:
        print(nomi, "kam qoldi! Yangi mahsulot buyurtma qilish kerak.")
    else:
        print(nomi, "yetarli.")
 
qoldiq_tekshir("Non", 5)
qoldiq_tekshir("Sut", 20)

