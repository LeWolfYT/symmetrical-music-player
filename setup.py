from cx_Freeze import setup, Executable
import sys

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

build_exe = {
    "packages": ["pygame"],
    'excludes':['PyQt4', 'PyQt5', 'PySide', 'PySide2', 'IPython', 'jupyter_client', 'jupyter_core', 'ipykernel', 'ipython_genutils', 'pytz', 'asyncio', 'pandas', 'psutil', 'numpy', 'pygments', 'scipy', 'openpyxl', 'matplotlib', 'docutils', 'sqlalchemy', 'sqlite3', 'tornado', 'libssl', 'pyportmidi', 'pycrypto', 'crypto', 'http', 'email', 'xml', 'xmlrpc', 'macholib'],
}

setup(
    name="Simple Music Player",
    version="1.0",
    author="LeWolfYT",
    author_email="ciblox3@gmail.com",
    description="A music player made with tkinter.",
    options={"build_exe": build_exe},
    executables=[Executable("tkmusic.py", base=base)],
)