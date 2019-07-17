# coding = utf-8
# using namespace std

"""

"""


class LocalTbs(object):
    """

    """

    ident_guide = " "*4

    def get_schema_packs(self, data: list) -> str:
        """

        :param data:
        :return:
        """
        rs = ""
        for i in data:
            rs += str(i[1]) + " -> \n"
            rs += "   |"+self.ident_guide + "ID => "+str(i[0]) + "\n"
            rs += "   |"+self.ident_guide + "Package Name => "+str(i[1]) + "\n"
            rs += "   |"+self.ident_guide + "Link Download => "+str(i[2]) + "\n"
            rs += "   |---->"
        return rs

    def get_schema_gits(self, data: list) -> str:
        rs = ""
        for i in data:
            rs += str(i[1]) + " -> \n"
            rs += "   |" + self.ident_guide + "ID => " + str(i[0]) + "\n"
            rs += "   |" + self.ident_guide + "Git Name => " + str(i[1]) + "\n"
            rs += "   |" + self.ident_guide + "Link Git => " + str(i[2]) + "\n"
            rs += "   |" + self.ident_guide + "Remote Name => "+str(i[3]) + "\n"
            rs += "   |" + self.ident_guide + "User Email => " + str(i[4]) + "\n"
            rs += "   |" + self.ident_guide + "User Name => "+str(i[5]) + "\n"
            rs += "   |---->"
        return rs
