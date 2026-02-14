
[app]
# (str) Title of your application
title = Biosecurity Pro

# (str) Package name
package.name = biosecuritypro

# (str) Package domain (needed for android packaging)
package.domain = org.biosecurity

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements 
# Note: kivymd and pillow are required for your specific app code
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sdl2_ttf,sdl2_image,openssl

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API support
android.minapi = 21

# (int) Android SDK/NDK versions for compatibility
android.sdk = 33
android.ndk = 25b

# (list) Android architectures
android.archs = armeabi-v7a, arm64-v8a

# (str) python-for-android branch
p4a.branch = master

# (str) Bootstrap to use for android
p4a.bootstrap = sdl2

# (int) Log level (2 = debug info)
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
