[app]
title = AlDimashqi
package.name = aldimashqi
package.domain = com.aldimashqi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,db
version = 0.1
requirements = python3,kivy

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 0
android.accept_sdk_license = True
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 0
