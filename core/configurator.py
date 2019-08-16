# coding = utf-8
# using namespace std
__author__ = "GiullianoRossi1987"
# impprt animations
import json
from typing import AnyStr


class ConfigFile(object):

    source = AnyStr
    conf_doc = dict()
    got_data = False

    class InvalidDocument(Exception):
        args = "That's not a valid document for the configurations"

    class InvalidCamp(Exception):
        args = "That's not a valid camp"

    class InvalidData(Exception):
        args = "That's not a valid value for that camp!"

    class NotFoundDocument(Exception):
        args = "There's no document to use as the configurations"

    @staticmethod
    def check_document(doc: dict) -> bool:
        """

        :param doc:
        :return:
        """
        if "AuthorName" or "Configured" or "AuthorGitHub" not in doc.keys() or len(doc.keys()) != 3: return False
        if (doc["AuthorName"] is None or doc["AuthorGithub"] is None) and doc["Configured"] is True: return False
        if doc["Configured"] is None: return False
        return True

    def __init__(self, source="./core/conf.json"):
        """

        :param source:
        """
        self.source = source
        with open(self.source, "r") as config:
            if not self.check_document(json.loads(config.read())): raise self.InvalidDocument
            self.conf_doc = json.loads(config.read())
        self.got_data = True

    @classmethod
    def commit_changes(cls):
        """

        :return:
        """
        if cls.got_data is False: raise cls.NotFoundDocument
        with open(cls.source, "w") as config: config.write(json.dumps(cls.conf_doc))

    def alter_data(self, camp: str, nw_vl):
        """"""
        if self.got_data is False: raise self.NotFoundDocument
        if camp not in {"AuthorName", "Configured", "AuthorGitHub"}: raise self.InvalidCamp
        if camp == "Configured" and nw_vl is not bool or None: raise self.InvalidData
        if (camp == "AuthorName" or camp == "AuthorGitHub") and nw_vl is not None or str: raise self.InvalidData
        self.conf_doc[camp] = nw_vl
        self.commit_changes()







