[app]
title = Comanda Vocale
package.name = comandavoce
package.domain = org.ristorante
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,speechrecognition,pyaudio
orientation = portrait
fullscreen = 1

android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.minapi = 21
android.sdk = 30
android.ndk = 25
android.api = 33
android.build_tools = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.hardwareAudio = True

[buildozer]
log_level = 2
warn_on_root = 1

