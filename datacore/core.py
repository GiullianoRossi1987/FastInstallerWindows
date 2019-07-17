# coding = utf-8
# using namespace std
import sqlite3
from os import system
from os import getcwd
from os import chdir

"""
"""


class DatabaseConnection(object):
    """"""

    connection_db = sqlite3.connect("./datacore/main-db.db")
    cursor = connection_db.cursor()
    got_data = False

    def __init__(self, file_db: str = "./datacore/main-db.db"):
        self.connection_db = sqlite3.connect(file_db)
        self.cursor = self.connection_db.cursor()
        self.got_data = True


class PackagesDatabase(DatabaseConnection):
    """

    """

    __dir_downloads__ = getcwd() + "\\Local-apps"

    class PackageNotFoundError(BaseException):
        args: object = "This package don't exists in the database!"

    class PackageExistsError(BaseException):
        args: object = "This package already exists in the database!"

    class InvalidDataSchema(BaseException):
        args: object = "This data structure's incorrect!"

    class InvalidLinkValue(BaseException):
        args: object = "This is not a valid link!"

    class InvalidCampTo(BaseException):
        args: object = "This camp don't exists to alter!"

    @classmethod
    def pack_exists(cls, package: str) -> bool:
        """

        :param package: The package to query
        :return:
        """
        query = cls.cursor.execute("select nm_pack from tb_packs;")
        for vl in query:
            if vl[0] == package: return True
        return False

    def add_pack(self, pack_data: list):
        """

        :param pack_data: Add a package to the database!
        """
        if len(pack_data) != 2: raise self.InvalidDataSchema()
        if self.pack_exists(pack_data[0]): raise self.PackageExistsError()
        if "http://" or "https://" or "/" not in pack_data[1]:
            raise self.InvalidLinkValue()
        insert_vals = self.cursor.execute("insert into tb_packs (nm_pack, link_to) values (?,?);", pack_data)
        self.connection_db.commit()
        del insert_vals

    def del_pack(self, pack: str):
        """

        :param pack:
        """
        if not self.pack_exists(pack):
            raise self.PackageNotFoundError()
        del_query = self.cursor.execute(f"delete from tb_packs where nm_pack = '{pack}';")
        self.connection_db.commit()
        del del_query

    def alt_pack_data(self, camp_to: str, new_vl: str, pack_to: str):
        """

        :param camp_to:
        :param new_vl:
        :param pack_to:
        :return:
        """
        if not self.pack_exists(pack_to):
            raise self.PackageNotFoundError()
        if camp_to not in ("nm_pack", "link_to"):
            raise self.InvalidCampTo()
        alt_query = self.cursor.execute(f"update tb_packs set {camp_to}='{new_vl}' where nm_pack='{pack_to}';")
        self.connection_db.commit()
        del alt_query

    def get_all_packs(self) -> list:
        """

        :return:
        """
        query = self.cursor.execute("select * from tb_packs;")
        return query.fetchall()

    def install_pack(self, pack_to: str = "*"):
        """

        :param pack_to:
        :return:
        """
        system("powershell -Command \"$webclient = New-Object System.Net.WebClient\"")
        if pack_to == "*":
            all_packs = self.get_all_packs()
            files_to = []
            for pack in all_packs:
                sep_link = "/".split(pack[2])
                fl_nm = self.__dir_downloads__+"\\"+sep_link[-1]
                files_to.append(fl_nm)
                install_command = system(f"powershell -command \"$webclient.DownloadFile({pack[2]}, {fl_nm})\"")
                del install_command
            for file in files_to:
                system("start "+file)
        else:
            query_one = self.cursor.execute(f"select * from tb_packs where nm_pack='{pack_to}';").fetchone()
            sep_ln = "/".split(query_one[2])
            fl_nm = self.__dir_downloads__ + "\\"+sep_ln[-1]
            install_command = system(f"powershell -command \"$webclient.DownloadFile({query_one[2]}, {fl_nm})\"")
            install_command = system("start "+fl_nm)
            del install_command


class GitterSystem(DatabaseConnection):
    """

    """

    class RepositoryNotFound(BaseException):
        args: object = "That repository don't exists in the database!"

    class RepositoryExistsError(BaseException):
        args: object = "That repository already exists in the database!"

    class InvalidCamp(IndexError):
        args: object = "That camp's not valid!"

    class InvalidDataStructure(TypeError, IndexError):
        args: object = "Those data are'nt valid!"

    class InvalidGitHost(BaseException):
        args: object = "That link's not valid!"

    @staticmethod
    def get_clone_local() -> str:
        """

        :return:
        """
        return ".."

    @classmethod
    def check_repo_exists(cls, repo: str) -> bool:
        """

        :param repo:
        :return:
        """
        query_to = cls.cursor.execute("select nm_git from tb_gits;")
        for vl in query_to.fetchall():
            if vl[0] == repo:
                return True
        return False

    @classmethod
    def check_host_valid(cls, host: str) -> bool:
        """

        :param host:
        :return:
        """
        return "https://github.com" in host

    def add_repo(self, repo_data: list):
        """

        :param repo_data:
        """
        if self.check_repo_exists(repo_data[0]):
            raise self.RepositoryExistsError()
        if len(repo_data) != 5:
            raise self.InvalidDataStructure()
        if not self.check_host_valid(repo_data[1]):
            raise self.InvalidGitHost()
        insert_q = self.cursor.execute("insert into tb_gits (nm_git, host_git, nm_remote, user_email, user_name) values (?,?,?,?, ?);", repo_data)
        self.connection_db.commit()
        del insert_q

    def del_repo(self, repo: str):
        """

        :param repo:
        :return:
        """
        if not self.check_repo_exists(repo): raise self.RepositoryNotFound()
        del_q = self.cursor.execute("delete from tb_gits where nm_git = '{}'")
        self.connection_db.commit()
        del del_q

    def alt_repo_data(self, repo_to: str, camp_to: str, new_vl: str):
        """

        :param repo_to:
        :param camp_to:
        :param new_vl:
        :return:
        """
        if not self.check_repo_exists(repo_to):
            raise self.RepositoryNotFound()
        if not camp_to in ("nm_git", "host_git", "nm_remote", "user_email", "user_name"):
            raise self.InvalidCamp()
        if camp_to == "host_git" and not self.check_host_valid(new_vl):
            raise self.InvalidGitHost()
        alt_q = self.cursor.execute(f"update tb_gits set {camp_to} = '{new_vl}' where nm_git = '{repo_to}';")
        self.connection_db.commit()
        del alt_q

    def show_all_data(self) -> list:
        """

        :return:
        """
        query = self.cursor.execute("select * from tb_gits;")
        return query.fetchall()

    def config_git_repo(self, repo_to: str = "*"):
        """

        :param repo_to:
        """
        chdir("..")
        if repo_to == "*":
            all_data = self.show_all_data()
            for data in all_data:
                co = system("git clone "+str(data[2]))
                chdir(str(data[1]))
                co =system("git remote add "+str(data[3])+" "+str(data[2]))
                co = system("git config --global user.email = "+str(data[4]))
                co = system("git config --global user.name = "+str(data[5]))
                chdir("..")
                del co
        else:
            if not self.check_repo_exists(repo_to):
                raise self.RepositoryNotFound()
            data = self.cursor.execute(f"select * from tb_gits where nm_git = '{repo_to}';").fetchone()
            co = system("git clone " + str(data[2]))
            chdir(str(data[1]))
            co = system("git remote add " + str(data[3]) + " " + str(data[2]))
            co = system("git config --global user.email = " + str(data[4]))
            co = system("git config --global user.name = " + str(data[5]))
            chdir("..")
            del co
        chdir("FastInstallerWindows")





























