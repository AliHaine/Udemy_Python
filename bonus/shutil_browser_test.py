import shutil
import webbrowser
import zipfile as zf
import pathlib


def make_archive(file, dest):
	with zf.ZipFile(pathlib.Path(dest, "com.zip"), 'w') as archive:
		archive.write(file, arcname=pathlib.Path(file).name)


def decompress_archive(archive, dest):
	with zf.ZipFile(pathlib.Path(archive), 'r') as unzip:
		unzip.extractall(dest)
