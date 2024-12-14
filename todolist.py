list = []

def menu():
    print('\n')
    print('='*40)
    print('SELAMAT DATANG DI TO DO LIST SEDERHANA')
    print('='*40)
    print('''
    1. Lihat daftar tugas
    2. Tambah daftar tugas
    3. Hapus tugas
    4. Keluar
        ''')

def daftar():
    while True:
        if not list:
            print('\nDAFTAR TUGAS\nKOSONG\n')
        else:
            print('\nDAFTAR TUGAS')
            for i, tugas in enumerate(list, 1):
                print(f'{i}. {tugas}',)
        input_user = input('apakah ingin keluar dari daftar tugas? (y/n): ')
        if input_user == 'y':
            break
            
def tambah_tugas():
    while True:
        tugas = input('\nMasukkan tugas: ')
        if tugas:
            list.append(tugas)
            print(f'tugas {tugas} berhasil di tambahkan\n')
        else:
            print('input error!')
        input_user = input('apakah ada lagi tugas yang ingin dimasukkan? (y/n): ')
        if input_user == 'n':
            break
        
def daftar_delete():
    if not list:
            print('\nDAFTAR TUGAS\nKOSONG\nTIDAK ADA YANG PERLU DI HAPUS')
    else:
            print('\nDAFTAR TUGAS')
            for i, tugas in enumerate(list, 1):
                print(f'{i}. {tugas}',)
        
def delete_tugas():
    while True:
        if list !=  []:
            delete_number = int(input('Angka berapa yang ingin di hapus: '))
        elif list == []:
            break
        if 1 <= delete_number <= len(list):
                tugas = list.pop(delete_number-1)
                print(f'{tugas} berhasil di hapus\n')
        else:
                    print('Masukkan angka yang benar')
                    
        input_user = input('apakah ada yang ingin di hapus lagi? (y/n): ')
        if input_user == 'n':
                break
        if input_user == 'y':
            daftar_delete()
            delete_tugas()
  
while True:      
    menu()
    input_menu = (input('Pilih menu nomor berapa: '))
    
    if input_menu == '1':
        daftar()
    
    if input_menu == '2':
        tambah_tugas()
        
    if input_menu == '3':
        daftar_delete()
        delete_tugas()
            
        
    if input_menu == '4':
        break
