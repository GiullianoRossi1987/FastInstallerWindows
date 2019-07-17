# coding = utf-8
# using namespace std
from os import system
from typing import AnyStr
from os import listdir


class BackupMaker(object):
    """

    """
    main_db = AnyStr
    got_data = False

    def __init__(self, file_db="./datacore/main-db.db"):
        """

        :param file_db:
        """
        self.main_db = file_db
        self.got_data = True

    @classmethod
    def create_backup_file(cls):
        """

        :return:
        """
        command = system(f"COPY {cls.main_db} ./public-backups")
        del command

    @classmethod
    def update_backup_file(cls, backup_exists=True):
        """

        :param backup_exists:
        """
        if not backup_exists:
            cls.create_backup_file()
        else:
            co1 = system(f"DELETE ./public-backups/{cls.main_db}")
            cls.create_backup_file()
            del co1

    @classmethod
    def check_back_exists(cls, backup_file: AnyStr) -> bool:
        """

        :param backup_file:
        :return:
        """
        return backup_file in listdir("./public-backups")


























