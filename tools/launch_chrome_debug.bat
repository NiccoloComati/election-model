@echo off
REM Starts a separate Chrome instance that the save_tabs.py script can talk to.
REM Chrome only allows remote debugging on a non-default profile, so this uses
REM its own profile folder. Log in to Silver Bulletin once in this window;
REM the login is remembered for next time.
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%LOCALAPPDATA%\ChromeDebugProfile"
