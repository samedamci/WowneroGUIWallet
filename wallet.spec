# -*- mode: python -*-

block_cipher = None


a = Analysis(['wallet.py'],
             pathex=['.'],
             binaries=[],
             datas=[('Resources/*', 'Contents/Resources')],
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
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='Wownero GUI Wallet.app',
             icon='./Resources/icons/appicon.icns',
             bundle_identifier='org.wownero.wallet',
             info_plist={
                 'NSHighResolutionCapable': 'True'
             })
