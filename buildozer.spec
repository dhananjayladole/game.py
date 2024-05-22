[app]

# (str) Title of your application
title = Tic Tac Toe

# (str) Package name
package.name = tictactoe

# (str) Package domain (needed for Android/IOS packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (int) Build version code (used for Android versioning)
version.code = 1

# (str) Application versioning (method 2)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow==10.3.0

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/image/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/image/presplash.png


#android.permissions = INTERNET


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (list) List of source pattern to ignore
#ignore_patterns = 

# (str) Path to a custom distribution template
# dist_template = $HOME/.buildozer/dist/default

# (str) Path to a custom SDK directory
# android.sdk = /home/kivy/android-sdk

# (str) Path to the android ndk
# android.ndk = /home/kivy/android-ndk-r19c

# (str) Android NDK version to use
# android.ndk_path = 

# (str) Android SDK version to use
# android.sdk_path = 

# (str) Android entry point
# android.entrypoint = org.example.myapp.MyApp

# (list) Application permissions
# android.permissions = INTERNET

# (str) Android app theme
# android.theme = '@android:style/Theme.Material'

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path = 

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.app_theme = @android:style/Theme.NoTitleBar.Fullscreen

# (str) Custom android manifest additions to intent filters, activities or other android elements
# android.manifest_additions = 

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android adb command to use
# adb_cmd = adb

# (str) Android entry point
# android.entrypoint = org.example.tictactoe.TicTacToeActivity

# (str) Android app theme
# android.theme = "@style/AppTheme"

# (list) Pattern to whitelist for the whole project
# whitelist = 

# (str) Path to a custom whitelist file
# whitelist_src = whitelist.txt

# (str) Path to a custom blacklist file
# blacklist_src = blacklist.txt

# (list) List of Java classes to add as activity
# android.add_activites = com.example.ExampleActivity

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# android.add_aars = foo/bar/myaar.aar

# (list) Gradle dependencies to add (currently works only with sdl2_gradle)
# android.gradle_dependencies = com.google.firebase:firebase-core:16.0.9

# (list) Repeated lines for each tool to run
# android.prebuild_addition = 

# (list) Java classes to add as activity
# android.add_activity =

# (list) Java classes to add as services
# android.add_service =

# (list) Java classes to add as receivers
# android.add_receiver =

# (list) Java classes to add as providers
# android.add_provider =

# (list) XML files to copy
# android.add_xml =

# (list) Java files to add (can be java or a_dir/*.java)
# android.add_src =

# (str) Android manifest intent filters
# android.manifest_intent_filters =

# (str) Android manifest meta data
# android.manifest_meta_data =

# (str) Android activity launch mode
# android.activity_launch_mode = standard

#android.manifest_additions = <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="YOUR_ADMOB_APP_ID"/>
