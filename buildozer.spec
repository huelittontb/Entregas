[app]
title = Entregas
package.name = entregas
package.domain = com.huelitton.entregas
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xls,xlsx
source.main = main.py
version = 1.0.0

# Dependências
requirements = python3==3.10.12, kivy==2.2.1, openpyxl, cython==0.29.36, git+https://github.com/tito/pyjnius.git

# Bootstrap e arquiteturas
bootstrap = sdl2
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21
android.api = 31

# Permissões
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Outras configs
orientation = portrait
log_level = 2
fullscreen = 0

# Ícone (opcional)
# icon.filename = %(source.dir)s/data/icon.png

# Pasta de build local
build_dir = .buildozer

[buildozer]
log_level = 2
warn_on_root = 1

