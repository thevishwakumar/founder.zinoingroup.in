import zipfile
import os

source_dir = "founder.zinoingroup.in"
target_zip = "founder_zinoingroup_backup_step29_predeploy.zip"

print(f"Creating backup archive {target_zip} from {source_dir}...")
with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
            zipf.write(file_path, arcname)

size = os.path.getsize(target_zip)
print(f"Backup created successfully: {target_zip} ({size:,} bytes)")
