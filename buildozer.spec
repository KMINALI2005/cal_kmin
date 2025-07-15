[app]
title = Smart Sum Calculator
package.name = smartsum
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3,kivy==2.3.0,hostpython3,sdl2,pyjnius,pillow,pango,cairo,glib,android
orientation = portrait
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# هذا يخبر Buildozer باستخدام API 34، والذي قمنا بتثبيت أدواته في الـ YAML
android.api = 34
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# [مهم] تحديد إصدار NDK لتجنب المشاكل مع API 34
# الإصدار 25b معروف بتوافقه الجيد مع الإصدارات الحديثة
android.ndk = 25b
