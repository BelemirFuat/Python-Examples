aranacak_dizi = [1,2,3,4,5]

aranacak_eleman = int(input("aramak istediğiniz sayiyi giriniz: "))

for x in aranacak_dizi:
    if (x==aranacak_eleman):
        print("bulundu")
        break
    elif(x==aranacak_dizi[-1]):
        print("bulunamadı.")

