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

def mahsulot_sotish(nomi, miqdori, sotilgan):
    if sotilgan <= miqdori:
        yangi_miqdor = miqdori - sotilgan
        print(nomi, "dan", sotilgan, "dona sotildi.")
        print("Omborda", yangi_miqdor, "dona qoldi.")
    else:
        print("Xatolik! Omborda yetarli mahsulot yo'q.")

mahsulot_sotish("Non", 25, 3)

def sotuv_hisobla(nomi, narxi, sotilgan):
    jami = narxi * sotilgan
    print("Mahsulot:", nomi)
    print("Sotilgan:", sotilgan, "dona")
    print("Jami to'lov:", jami, "so'm")
    return jami
jami_summa = sotuv_hisobla("Non", 4000, 3)

def chegirma_hisobla(jami):
    if jami >= 100000:
        chegirma = jami * 0.10
        yakuniy_narx = jami - chegirma
        print("10% chegirma:", chegirma, "so'm")
        print("To'lanadigan summa:", yakuniy_narx, "so'm")
    else:
        print("Chegirma mavjud emas.")
        print("To'lanadigan summa:", jami, "so'm")
chegirma_hisobla(jami_summa)
def mahsulotlarni_korsat():
    print("\n--- MAHSULOTLAR RO'YXATI ---")
    for mahsulot in mahsulotlar:
        print(
            mahsulot["nomi"],
            "| Narxi:", mahsulot["narxi"],
            "| Miqdori:", mahsulot["miqdori"]
        )

mahsulotlarni_korsat()
def mahsulot_qidir(nomi):
    for mahsulot in mahsulotlar:
        if mahsulot["nomi"].lower() == nomi.lower():
            print("Topildi:", mahsulot)
            return
    print("Bunday mahsulot topilmadi.")

mahsulot_qidir("Sut")
mahsulot_qidir("Guruch")
def mahsulot_sotish(nomi, soni):
    for mahsulot in mahsulotlar:
        if mahsulot["nomi"].lower() == nomi.lower():
            if soni <= 0:
                print("Sotuv miqdori noto'g'ri.")
                return
            if mahsulot["miqdori"] >= soni:
                mahsulot["miqdori"] -= soni
                summa = mahsulot["narxi"] * soni
                print(soni, "dona", nomi, "sotildi.")
                print("Jami summa:", summa, "so'm")
                print("Qoldiq:", mahsulot["miqdori"])
            else:
                print("Omborda mahsulot yetarli emas.")
            return
    print("Mahsulot topilmadi.")
mahsulot_sotish("Non", 3)
mahsulot_sotish("Sut", 5)
mahsulot_sotish("Shakar", 100)
mahsulot_sotish("Choy", 2)
mahsulot_sotish("Non", -2)

