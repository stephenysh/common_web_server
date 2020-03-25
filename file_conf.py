import json
from pathlib import Path
from argparse import Namespace

class FileConf:

    def __init__(self, filepath, type='json'):
        self.file_path = Path(filepath).resolve()
        self.type = type

        with open(self.file_path, 'r', encoding='utf-8') as fw:
            self.conf_obj = json.load(fw, object_hook=lambda d: Namespace(**d))
