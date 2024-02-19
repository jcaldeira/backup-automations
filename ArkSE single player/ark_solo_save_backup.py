import os
import shutil
from datetime import datetime

#region Ask if the script is supose to run
UserInput = ' '

while (UserInput.lower() not in ['y', 'n', '']):
    UserInput = input('Run Ark: SE single player backup script? (Y/n) ')

if (UserInput.lower() == 'n'):
    RunScript = False
else:
    RunScript = True

#endregion Ask if the script is supose to run

#region Create paths and timestamps for backup
Timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
DestinationPath = os.path.join(str(os.getenv('OneDrive')), r'Game Saves\Ark\Single Player\Backups\Automatic')

ArchiveBaseName = os.path.join(DestinationPath, Timestamp)
ArchiveFormat = 'zip'
ArchiveRootDir = r'C:\Program Files (x86)\Steam\steamapps\common\ARK\ShooterGame'
ArchiveBaseDir = r'Saved'
ArchiveDryRun = False

ArkLocalSavePath = os.path.join(ArchiveRootDir, ArchiveBaseDir)

#endregion Create paths and timestamps for backup

#region Make sure backup folder is not cluttered
BackupsInFolder = os.listdir(DestinationPath)

OldestBackupPath = os.path.join(DestinationPath, BackupsInFolder[0])

# OldestBackupTimestamp = datetime.fromtimestamp(os.stat(OldestBackupPath).st_birthtime)
# OldestTimeDelta = (datetime.now() - OldestBackupTimestamp).days

# if ((len(BackupsInFolder) > 30) and (OldestTimeDelta > 180)):
if (len(BackupsInFolder) > 30):
    os.remove(OldestBackupPath)

#endregion Make sure backup folder is not cluttered

#region Create backup
if (os.path.exists(ArkLocalSavePath) and (RunScript)):
    print('Creating backup now.')
    shutil.make_archive(
        base_name=ArchiveBaseName,
        format=ArchiveFormat,
        root_dir=ArchiveRootDir,
        base_dir=ArchiveBaseDir,
        dry_run=ArchiveDryRun
    )

#endregion Create backup

input('Press ENTER to close this window.')
