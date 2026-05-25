# ===================================
# Employee Inventory Application
# ===================================
# Developed by. Yoanita Dwi Harlandi 
# JCDS - [33]


# /************************************/

# /===== Data Model =====/
# Create your data model here
inventory_training = [
    {"emp_id" : "Di001", "emp_name":"Dila", "job_title":"Officer Liquidity Risk","dept_name":"Market & Liquidity Risk", "training_name":"Manajemen Risiko Jenjang 4", 
   "training_cat": "Sertifikasi", "training_date":"2026-05-15", "training_valid":4, "training_status":"Aktif"},
   {"emp_id" : "Al002", "emp_name":"Alia", "job_title":"Officer Talent Acquisition","dept_name":"Human Resource", "training_name":"Pelatihan Rekrutmen dan Seleksi", 
   "training_cat": "Non Sertifikasi", "training_date":"2025-12-22", "training_valid":0, "training_status":"Aktif"},
   {"emp_id" : "Ja003", "emp_name":"Jason", "job_title":"Data Analyst","dept_name":"Management Information", "training_name":"Visualisasi Data", 
   "training_cat": "Non Sertifikasi", "training_date":"2026-01-12", "training_valid":0, "training_status":"Aktif"}
]

#inventory_training =[] -- Ketika data di data collection sudah tidak ada

# /===== Feature Program =====/
# Create your feature program here
#function menu utama
def main_menu():
    print("\n=== Inventory Training Karyawan Bank ABC ===\n")
    print("1. Report Data Training Karyawan")
    print("2. Menambahkan Data Training Karyawan")
    print("3. Mengubah Data Training Karyawan")
    print("4. Menghapus Data Training Karyawan")
    print("5. Exit")
    input_mainmenu = input("Silahkan Pilih Menu Utama [1-5]: ")
    return input_mainmenu

#function sub menu fitur READ
def view_submenuread():
    print("\n~~~ Report Data Training Karyawan ~~~\n")
    print("1. Report Semua Data Training Karyawan")
    print("2. Mencari Data Training Karyawan Tertentu")
    print("3. Kembali Ke Menu Utama")
    input_sub_menuread = input("Silahkan Pilih Sub Menu Report Data [1-3]:" )
    return input_sub_menuread

#function fitur READ, display employee training inventory data
def read_training(data):
    if len(data) == 0:
       print("***Tidak Ada Data Training Karyawan***")
       return
    
    print("\nDaftar Data Training Karyawan")
    print("=" * 155)
    print(f'{"NIP":<5} {"Nama":<8} {"Jabatan":<30} {"Department":<25} {"Training":<35} {"Kategori":<16} {"Tanggal":<10} {"Valid":<5} {"Status":<8}')
    print("=" * 155)
    for tr in data:
        emp_id = tr["emp_id"]
        emp_name = tr["emp_name"]
        job_title = tr["job_title"]
        dept_name = tr["dept_name"]
        training_name = tr["training_name"]
        training_cat = tr["training_cat"]
        training_date = tr["training_date"]
        training_valid = tr["training_valid"]
        training_status = tr["training_status"]
        print(f"{emp_id:<5} {emp_name:<8} {job_title:<30} {dept_name:<25} {training_name:<35} {training_cat:<16} {training_date:<10} {training_valid:<5} {training_status:<8}")
    
#function validation key id 
def search_training(search_NIP):
    search_result = []
    for tr in inventory_training:
        emp_id = tr["emp_id"]
        if search_NIP.lower() == emp_id.lower():
            search_result.append(tr)
    if len(search_result) >0:
       read_training(search_result)
    else:
       print("***Tidak Ada Data Training Karyawan***")

#function sub menu fitur CREATE
def view_submenucreate():
    print("\n~~~ Menambah Data Training Karyawan ~~~\n")
    print("1. Tambah Data Training Karyawan")
    print("2. Kembali Ke Menu Utama")
    input_sub_menucreate = input("Silahkan Pilih Sub Menu Create Data [1-2]:" )
    return input_sub_menucreate

#function validation no dupkey fitur CREATE
def cek_training(add_NIP):
    for tr in (inventory_training):
        emp_id = tr["emp_id"]
        if add_NIP.lower() == emp_id.lower():
            print("Data Training Karyawan Sudah Ada")
            return True
    return False

#function fitur CREATE
def add_training(add_NIP, emp_name, job_title, dept_name, training_name, training_cat, training_date, training_valid, training_status):

    tr ={
        "emp_id" : add_NIP,
        "emp_name" : emp_name,
        "job_title" : job_title,
        "dept_name" : dept_name,
        "training_name" : training_name,
        "training_cat" : training_cat,
        "training_date" : training_date,
        "training_valid" : training_valid,
        "training_status" : training_status
    }
    create = True
    while create:
        confirm = input("Apakah Data akan disimpan? (Y/N)").lower()
        if confirm == "y":
            inventory_training.append(tr)
            print("Data Tersimpan")
            return
        elif confirm == "n":
            print("Data Tidak Ditambahkan")
            return
        else:
            print("Pilihan Salah, Masukkan Y/N")

#function sub menu UPDATE 
def view_submenuupdate():
    print("\n~~~ Mengubah Data Training Karyawan ~~~\n")
    print("1. Ubah Data Training Karyawan")
    print("2. Kembali Ke Menu Utama")
    input_sub_menuupdate = input("Silahkan Pilih Sub Menu Update Data [1-2]:" )
    return input_sub_menuupdate

#function fitur UPDATE
def update_training(search_NIP):
    for tr in inventory_training:
        if search_NIP.lower() == tr["emp_id"].lower():
            update = True
            while update:
                confirm = input("Tekan Y jika akan mengupdate data dan N untuk membatalkan (Y/N) :").lower()
                if confirm == "y":
                    updated_field = input("Masukan Nama Kolom yang Diupdate\n'(emp_name; job_title; dept_name; training_name; training_cat; training_date; training_valid; training_status)' :")
                    if updated_field not in tr:
                        print("!! Nama Kolom Salah")
                        return
                    updated_value = input("Masukkan Nilai Baru: ")
                    while True:
                        save_value = input("Apakah Data akan Diupdate? (Y/N)").lower()
                        if save_value == "y":
                            if updated_field == "training_valid":
                                updated_value = int(updated_value)
                            tr[updated_field] = updated_value
                            print("Data Terupdate")
                            return
                        elif save_value == "n":
                            print("Data Tidak Terupdate")
                            return
                        else:
                            print("Pilihan Salah, Masukkan Y/N")
                elif confirm == "n":
                    print("Data Tidak Diupdate")
                    return
                else:
                    print("Pilihan Salah, Masukkan Y/N")

#function sub menu DELETE
def view_submenudelete():
    print("\n~~~ Menghapus Data Training Karyawan ~~~\n")
    print("1. Hapus Data Training Karyawan")
    print("2. Kembali Ke Menu Utama")
    input_sub_menudelete = input("Silahkan Pilih Sub Menu Hapus Data [1-2]:" )
    return input_sub_menudelete

#function fitur DELETE
def delete_training(search_NIP):
    for tr in inventory_training:
        if search_NIP.lower() == tr["emp_id"].lower():
            delete = True
            while delete:
                confirm = input("Apakah Data akan Dihapus? (Y/N): ").lower()
                if confirm == "y":
                    inventory_training.remove(tr)
                    print("Data Terhapus")
                    return
                elif confirm == "n":
                    print("Data Tidak Terhapus")
                    return
                else:
                    print("Pilihan Salah, Masukkan Y/N")


# /===== Main Program =====/
# Create your main program here
running = True
while running:
    input_mainmenu = main_menu()
    #print(f"DEBUG: '{input_mainmenu}'")
    if input_mainmenu == "1":
        submenu_read = True
        while submenu_read:
            input_sub_menuread = view_submenuread()
            if input_sub_menuread == "1":
                print("Daftar Training Karyawan:")
                read_training(inventory_training)
            elif input_sub_menuread == "2":
                search_NIP = input("Masukkan NIP Karyawan: ")
                print("Data Training Karyawan dengan NIP :",search_NIP)
                search_training(search_NIP)
            elif input_sub_menuread == "3":
                submenu_read = False
    elif input_mainmenu == "2":
        submenu_create = True
        while submenu_create:
            input_sub_menucreate = view_submenucreate()
            if input_sub_menucreate == "1":
                add_NIP = input("Masukkan NIP Karyawan: ")
                if cek_training(add_NIP):
                    continue
                emp_name = input("Masukkan Nama Karyawan : ")
                job_title = input("Masukkan Jabatan : ")
                dept_name = input("Masukkan Department : ")
                training_name = input("Masukkan Nama Training : ")
                training_cat = input("Masukkan Kategori Training : ")
                training_date = input("Masukkan Tanggal Training : ")
                training_valid = int(input("Masukkan Masa Berlaku Training : "))
                training_status = input("Masukkan Status Training : ")
                add_training(add_NIP, emp_name, job_title, dept_name, training_name, training_cat, training_date, training_valid, training_status)
            elif input_sub_menucreate == "2":
                submenu_create = False
    elif input_mainmenu == "3":
        submenu_update = True
        while submenu_update:
            input_sub_menuupdate = view_submenuupdate()
            if input_sub_menuupdate == "1":
                search_NIP = input("Masukkan NIP Karyawan: ")
                search_training(search_NIP)
                update_training(search_NIP)
            elif input_sub_menuupdate == "2":
                submenu_update = False
    elif input_mainmenu == "4":
        submenu_delete = True
        while submenu_delete:
            input_sub_menudelete = view_submenudelete()
            if input_sub_menudelete == "1":
                search_NIP = input("Masukkan NIP Karyawan: ")
                search_training(search_NIP)
                delete_training(search_NIP)
            elif input_sub_menudelete == "2":
                submenu_delete = False
    elif input_mainmenu == "5":
        print ("Terima Kasih Sudah Menggunakan Aplikasi")
        running = False
    else:
        print("***Pilihan yang Anda Masukkan Salah***")