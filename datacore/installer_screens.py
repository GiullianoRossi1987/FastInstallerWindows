# coding = utf-8
# using namespace std
from datacore.core import PackagesDatabase
from datacore.beauty import LocalTbs
from datacore.backup_maker import BackupMaker
from os import system


__help__ = """"""


class MainInstallerScreen(object):

    class EndUsage(KeyboardInterrupt):
        args: object = "Closed Usage!"

    def __init__(self):
        obj_1 = PackagesDatabase()
        tbs_obj = LocalTbs()
        back_obj = BackupMaker()
        while True:
            clean = system("cls")
            del clean
            # todo: Fazer a tela de menu (copiar do figlet do linux kkk)
            print("""
[1] Install a Package
[2] Add a Package
[3] Remove a Package
[4] Update a Package Data
[5] See all Packages
[6] Help
[7] Exit
                """)
            while True:
                op1 = int(input(">>> "))
                confirm = int(input("Confirm?\n[1]Y\n[2]N\n>>> "))
                if confirm == 1: break
            if op1 == 1:
                con = True
                while True:
                    pack_to = str(input("Type the package to install (for all the packages type '*': "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_1.install_pack(pack_to)
                    input("Packages installed successfully!\n<<press any button to return>>")
                del pack_to
                continue
            elif op1 == 2:
                con = True
                while True:
                    pack_nm = str(input("Type a name for the package: "))
                    link_download = str(input("The link to the installer download: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_1.add_pack([pack_nm, link_download])
                    input("Added Successfully!\n<<press any button to return>>")
                del pack_nm
                del link_download
                continue
            elif op1 == 3:
                con = True
                while True:
                    pack_to = str(input("The package to remove: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_1.del_pack(pack_to)
                    input("Removed Successfully!\n<<press any button to return>>")
                del pack_to
                continue
            elif op1 == 4:
                con = True
                while True:
                    pack_to = str(input("The package to alter data: "))
                    camp_to = str(input("The camp to alter: "))
                    new_vl = str(input("The new value to the camp data: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_1.alt_pack_data(camp_to, new_vl, pack_to)
                    input("Updated Successfully!\n<<press any button to return>> ")
                del pack_to, camp_to, new_vl
                continue
            elif op1 == 5:
                data = obj_1.get_all_packs()
                print(tbs_obj.get_schema_packs(data))
                input("<<press any button to return>>")
                del data
                continue
            elif op1 == 6:
                print(__help__)
                input("<<press any button to return>>")
            elif op1 == 7:
                bc_e = back_obj.check_back_exists(back_obj.main_db)
                a = back_obj.update_backup_file(bc_e)
                raise self.EndUsage()
            else:
                print("That's not a valid option!\nTry again!")
                continue
















