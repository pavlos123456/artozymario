[app]

# (str) Title of your application
title = artozymario

# (str) Package name
package.name = artozymario

# (str) Package domain (reverse domain)
package.domain = org.pavlos123456

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (can be regex patterns)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Do not compile to .pyo files
# no.compile = 0

# (bool) Use the Python 3.8+ Android compatibility fixes
android.api = 33

# (int) Android API level to use
android.minapi = 23

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25c

# (bool) Enable AndroidX
android.enable_androidx = True

# (str) Android entry point (default is main.py)
android.entrypoint = artozymario.py

# (list) Permissions
android.permissions = INTERNET

# (bool) Fullscreen
fullscreen = 0

[buildozer]

# (str) Path to buildozer.spec file (default is .)
# buildozer.spec =

# (bool) Make an APK (Android) or AAB (Android App Bundle)
android.release = AAB

# (list) Log level (debug, info, warning, error, critical)
log_level = 2
