import shutil


def download_system(output_path, dir_path):
    shutil.make_archive(output_path, 'zip', root_dir=dir_path)
