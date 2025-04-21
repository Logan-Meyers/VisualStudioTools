from pathlib import PurePath
import uuid

class Project:
    # uuids
    proj_type: uuid.UUID = None
    unique_uuid: uuid.UUID = None
    # names and paths
    name: str = None
    root_dir: PurePath = None
    proj_sln_same_path: bool = None
    # post solution stuff
    post_sln_configs: str = []

    def __init__(self, type: uuid.UUID, unique: uuid.UUID, name: str, vcxproj_path_rel: str, sln_path: PurePath):
        self.proj_type = type
        self.unique_uuid = unique
        self.name = name

        # same path setting
        if (vcxproj_path_rel.find("\\") == -1):
            self.proj_sln_same_path = True
        else:
            self.proj_sln_same_path = False
        
        self.root_dir = sln_path

    def add_config(self, config: str):
        self.post_sln_configs += config

    