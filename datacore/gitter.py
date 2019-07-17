# coding = utf-8
# using namespace std
from datacore.core import GitterSystem
from datacore.beauty import LocalTbs
from datacore.backup_maker import BackupMaker
from os import system


__help__ = """"""


class GitterScreens(object):
    """"""

    class EndUsage(KeyboardInterrupt):
        args: object = "Closed using!"

    def __init__(self):
        obj_gitter = GitterSystem()
        tbs_obj = LocalTbs()
        back_obj = BackupMaker()
        while True:
            cleaner = system("cls")
            del cleaner
            while True:
                # todo: copiar a logo do figlet no linux
                print("""
[1] Config Git Repositories.
[2] Add a new Git Repository.
[3] Remove a Repository.
[4] Alter a Repository Data.
[5] See all the repositories in the database.
[6] Help
[7] Exit
                """)
                op1 = int(input(">>> "))
                confirm = int(input("Confirm?\n[1]Y\n[2]N\n>>> "))
                if confirm == 1: break
            if op1 == 1:
                con = True
                while True:
                    repo_to = str(input("Repository to configure (for all type '*'): "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_gitter.config_git_repo(repo_to)
                    input("Configured Successfully!\n<<press any button to return>>")
                del repo_to
                continue
            elif op1 == 2:
                con = True
                while True:
                    repo_nm = str(input("Type the repository name: "))
                    host_vl = str(input("Type the repository host (http/https): "))
                    remote_nm = str(input("Type a remote name: "))
                    user_email = str(input("The user email: "))
                    user_nm = str(input("The user name: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_gitter.add_repo([repo_nm, host_vl, remote_nm, user_email, user_nm])
                    input("Added to the database!\n<<press any button to return>>")
                del repo_nm, host_vl, remote_nm, user_nm, user_email
                continue
            elif op1 == 3:
                con = True
                while True:
                    repo_to = str(input("The repository to delete: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_gitter.del_repo(repo_to)
                    input("Removed Successfully!\n<<press any button to return>>")
                del repo_to
                continue
            elif op1 == 4:
                con = True
                while True:
                    repo_to = str(input("The repository to alter: "))
                    camp = str(input("The camp to alter: "))
                    new_vl = str(input("The new value: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        con = False
                        break
                    if confirm == 1: break
                if con:
                    obj_gitter.alt_repo_data(repo_to, camp, new_vl)
                    input("Altered Successfully!\n<<press any button to return>>")
                del repo_to, camp, new_vl
                continue
            elif op1 == 5:
                all_data = obj_gitter.show_all_data()
                print(tbs_obj.get_schema_gits(all_data))
                del all_data
                input("<<press any button to return>>")
                continue
            elif op1 == 6:
                print(__help__)
                input("<<press any button to return>>")
                continue
            elif op1 == 7:
                bc_exists = back_obj.check_back_exists(back_obj.main_db)
                back_obj.update_backup_file(bc_exists)
                raise self.EndUsage()
            else:
                input("Invalid Option Try again!\n<<press any button to try again>>")
                continue







