import shutil
import webbrowser
import zipfile as zf
import pathlib


def make_archive(file, dest):
	with zf.ZipFile(pathlib.Path(dest, "com.zip"), 'w') as archive:
		archive.write(file, arcname=pathlib.Path(file).name)
