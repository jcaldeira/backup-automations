import os
import shutil
from datetime import datetime

Timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
DestinationPath = os.path.join(str(os.getenv('OneDrive')), r'Game Saves\Ark\Single Player\Backups\Automatic')

Archive_base_name = os.path.join(DestinationPath, Timestamp)
Archive_format = 'zip'
Archive_root_dir = r'C:\Program Files (x86)\Steam\steamapps\common\ARK\ShooterGame'
Archive_base_dir = r'Saved'
Archive_dry_run = False

ArkLocalSavePath = os.path.join(Archive_root_dir, Archive_base_dir)

if (os.path.exists(ArkLocalSavePath)):
    print('Ark saves exist. Creating an archive of tree structure.')
    shutil.make_archive(
        base_name=Archive_base_name,
        format=Archive_format,
        root_dir=Archive_root_dir,
        base_dir=Archive_base_dir,
        dry_run=Archive_dry_run
    )
