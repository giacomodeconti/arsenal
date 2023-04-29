### Remove icon from Launchpad
Replace APP_NAME_CASE_SENSITIVE with the name of the app
- sqlite3 $(find /private/var/folders \( -name com.apple.dock.launchpad -a -user $USER \) 2> /dev/null)/db/db "DELETE FROM apps WHERE title='APP_NAME_CASE_SENSITIVE';" && killall Dock
