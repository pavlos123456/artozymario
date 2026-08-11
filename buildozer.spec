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
requirements = python3,kivy

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../../kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of services to declare
# services = name:description

# (bool) Do not compile to .pyo files
# no.compile = 0

# (bool) Use the Python 3.8+ Android compatibility fixes
android.api = 31

# (int) Android API level to use
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded)
# android.ant_path =

# (bool) Enable Android Java 8 features (desugaring)
android.gradle_dependencies =

# (list) Java classes to add as dependencies
# android.add_src =

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (bool) Enable AndroidX
android.enable_androidx = True

# (bool) Enable automatic AndroidX migration
android.gradle_dependencies = androidx.appcompat:appcompat:1.3.1

# (str) Android entry point (default is main.py)
android.entrypoint = artozymario.py

# (list) Permissions
android.permissions = INTERNET

# (list) Android additional libraries to copy
# android.add_libs =

# (bool) Use Kivy's SDL2 backend
# kivy.sdl2 = 0

# (bool) Use Kivy's GStreamer backend
# kivy.gstreamer = 0

# (bool) Use Kivy's Pygame backend
# kivy.pygame = 0

# (str) iOS bundle identifier
# ios.bundle_identifier =

# (str) iOS bundle name
# ios.bundle_name =

# (str) iOS bundle version
# ios.bundle_version =

# (str) iOS supported orientations
# ios.orientation = portrait

[buildozer]

# (str) Path to buildozer.spec file (default is .)
# buildozer.spec =

# (bool) Make an APK (Android) or AAB (Android App Bundle)
android.release = AAB

# (list) Log level (debug, info, warning, error, critical)
log_level = 2

# (list) Warnings to ignore
# warn_ignore =

# (bool) Rebuild everything on each run
# rebuild = True

# (bool) Use the Android SDK directory
# android.use_sdk = False

# (bool) Use the Android NDK directory
# android.use_ndk = False

# (str) Path to the Android SDK directory
# android.sdk_path =

# (str) Path to the Android NDK directory
# android.ndk_path =

# (str) Path to the ANT directory
# android.ant_path =

# (bool) Use the Android SDK's tools
# android.use_sdk_tools = False

# (bool) Use the Android SDK's platform-tools
# android.use_platform_tools = False

# (bool) Use the Android SDK's build-tools
# android.use_build_tools = False

# (str) Path to the Java Development Kit (JDK)
# java.home =

# (bool) Use the Java Development Kit (JDK)
# java.use_home = False

# (str) Path to the Java executable
# java.path =

# (bool) Use the Java executable
# java.use_path = False

# (bool) Use the Python interpreter
# python.use_path = False

# (str) Path to the Python interpreter
# python.path =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android = False

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_path =

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_fixes =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android_fixes = False

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_fixes_path =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android_fixes_path = False

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_fixes_include =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android_fixes_include = False

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_fixes_exclude =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android_fixes_exclude = False

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_fixes_include_paths =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android_fixes_include_paths = False

# (str) Path to the Python 3.8+ Android compatibility fixes
# python.android_fixes_exclude_paths =

# (bool) Use the Python 3.8+ Android compatibility fixes
# python.use_android_fixes_exclude_paths = False

# (list) Android library to include
# android.add_libs =

# (list) Android library to exclude
# android.exclude_libs =

# (list) Android library to include from the Android SDK
# android.sdk_add_libs =

# (list) Android library to exclude from the Android SDK
# android.sdk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =

# (list) Android library to include from the Android NDK
# android.ndk_add_libs =

# (list) Android library to exclude from the Android NDK
# android.ndk_exclude_libs =
