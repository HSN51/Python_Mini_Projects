
# Boş bir to do listesi oluşturma
to_do_list = []

def add_task(to_do_list):
    task = input("Yapılacak görevi giriniz:")
    to_do_list.append(task)
    print("Görev başarıyla eklendi")

def show_task(to_do_list):
    print("Yapılacak Görevler")

    for task in to_do_list:
        print("- " + task)

def remove_task(to_do_list):
    task = input("Silmek istediğiniz görevi yazınız:")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Görev başarıyla silindi.")
    else:
        print("Görev bulunamadı")


while True:
    print("\nTo-Do list uygulaması:")
    print("\n1.Görev ekle")
    print("\n2.Görevleri Göster")
    print("\n3.Görev sil")
    print("\n4.Çıkış")
    choice = input("Seçiminiz (1/2/3/4):")

    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_task(to_do_list)
    elif choice == "3":
        remove_task(to_do_list)
    elif choice == "4":
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin!")

















