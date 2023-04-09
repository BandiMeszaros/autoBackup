import os
from enum import Enum
import uuid
import time
import json
from error_utils import *

BackupRule = Enum('BackupRule', ['ON_MOD', 'ON_TURNOFF', 'EVERY_WEEK', 'ONCE'])


class BackUpRule:
    """defines a backup rule"""
    def __init__(self, rulename: str, loc: str, rule: BackupRule):
        self.rule_name = rulename
        self.ID = uuid.uuid4()

        if os.path.exists(loc):
            self.loc = loc
        else:
            raise LocationNotFoundError

        self.rule = rule

    def __str__(self):
        return {self.rule_name: {'ID': self.ID,
                                 'loc': self.loc, 'rule': self.rule}}

    def getID(self):
        return self.ID


class FileUtils:
    """handles file management"""
    def __init__(self, loc: str, savesloc=None):
        self.backupRules = []
        self.backupRulesID = []
        self.backuploc = None

        if savesloc is not None:
            if not os.path.isdir(savesloc):
                try:
                    os.mkdir(savesloc)
                except Exception:
                    raise FileCreationError
                self.savesloc = savesloc
        if os.path.isdir(loc):
            self.backuploc = loc
        else:
            try:
                os.mkdir(loc)
                self.backuploc = loc
                with open(self.backuploc, 'w') as file:
                    json.dump('{}', file, indent=4)

            except Exception:
                raise DirectoryInitError

    def save_rules(self):
        with open(self.savesloc, 'w') as f:
            json.dump(self.backupRules,f , indent=4)

    def add_new_rule(self, name, loc, ruletype: BackupRule):

        if ruletype in BackupRule:
            new_rule = BackUpRule(name, loc, ruletype)
            self.backupRules.append(new_rule)
            self.backupRulesID.append(new_rule.getID())
            self.save_rules()
        else:
            print("Bad rule type, try again")

    def _load_rules(self):

        if self.backuploc:
            with open(self.backuploc, 'r') as file:
                data = json.load(file)
            if data is not '':
                for v in data:
                    self.backupRulesID.append(v.getID())
                    self.backupRules.append(v)