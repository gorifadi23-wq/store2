[app]

title = Excel Manager AI
package.name = excelmanagerai
package.domain = org.fadi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivymd,pandas,openpyxl,plyer
orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.arch = arm64-v8a

log_level = 2

[buildozer]

log_level = 2
warn_on_root = 1
