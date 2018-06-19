#!/usr/bin/python
# coding: utf-8

import os
import sys

import distutils
from PyInstaller.building.datastruct import Tree
from distutils.dir_util import copy_tree

from settings import VERSION

DIR_PATH = os.getcwd()
COMPILING_PLATFORM = distutils.util.get_platform()

PATH_EXE = [os.path.join(DIR_PATH, 'wallet.py')]

VERSION = '.'.join(str(n) for n in VERSION)

print('\033[33m{}'.format('#'*46))
print('#{}#'.format(' '*44))
print("""#  \033[35m/  |  _  /  | /      \ /  |  _  /  |/  |\033[33m  #
#  \033[35m▓▓ | / \ ▓▓ |/▓▓▓▓▓▓  |▓▓ | / \ ▓▓ |▓▓ |\033[33m  #
#  \033[35m▓▓ |/▓  \▓▓ |▓▓ |  ▓▓ |▓▓ |/▓  \▓▓ |▓▓ |\033[33m  #
#  \033[35m▓▓ /▓▓▓  ▓▓ |▓▓ |  ▓▓ |▓▓ /▓▓▓  ▓▓ |▓▓ |\033[33m  #
#  \033[35m▓▓ ▓▓/▓▓ ▓▓ |▓▓ |  ▓▓ |▓▓ ▓▓/▓▓ ▓▓ |▓▓/ \033[33m  #
#  \033[35m▓▓▓▓/  ▓▓▓▓ |▓▓ \__▓▓ |▓▓▓▓/  ▓▓▓▓ | __ \033[33m  #
#  \033[35m▓▓▓/    ▓▓▓ |▓▓    ▓▓/ ▓▓▓/    ▓▓▓ |/  |\033[33m  #
#  \033[35m▓▓/      ▓▓/  ▓▓▓▓▓▓/  ▓▓/      ▓▓/ ▓▓/ \033[33m  #""")
print('#{}#'.format(' '*44))

if COMPILING_PLATFORM == 'win-amd64':
    platform = 'win'
    STRIP = False
elif COMPILING_PLATFORM == 'linux-x86_64':
    platform = 'nix64'
    STRIP = True
elif 'macosx' in COMPILING_PLATFORM:
    platform = 'mac'
    STRIP = True
else:
    err_str = ' UNRECOGNIZED PLATFORM, EXITING NOW!'
    print('#{}{}#'.format(err_str, ' '*(44-len(err_str))))
    print('#{}#'.format(' '*44))
    print('{}\033[0m'.format('#'*46))
    sys.exit()

ver_str = ' COMPILING WOWNERO GUI WALLET v{}'.format(VERSION)
platform_str = ' PLATFORM: {}'.format(COMPILING_PLATFORM)
print('#{}{}#'.format(ver_str, ' '*(44-len(ver_str))))
print('#{}{}#'.format(platform_str, ' '*(44-len(platform_str))))
print('#{}#'.format(' '*44))
print('{}\033[0m'.format('#'*46))

block_cipher = None


a = Analysis(['wallet.py'],
             pathex=PATH_EXE,
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Wownero GUI Wallet',
          icon='./Resources/icons/favicon.ico',
          debug=False,
          strip=STRIP,
          upx=True,
          runtime_tmpdir=None,
          console=False)
coll = COLLECT(exe,
               Tree('./Resources'),
               a.datas,
               strip=STRIP,
               upx=True,
               name=os.path.join('dist', 'Resources'))
if platform == 'mac':
    app = BUNDLE(exe,
                 name='Wownero GUI Wallet.app',
                 icon='./Resources/icons/appicon.icns',
                 bundle_identifier='org.wownero.wallet',
                 info_plist={
                     'NSHighResolutionCapable': 'True'
                 })
    copy_tree(
        'dist/Resources',
        'dist/Wownero GUI Wallet.app/Contents/Resources/',
    )
