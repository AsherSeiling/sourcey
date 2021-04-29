pyinstaller main.py --onefile
mv dist/main ./sourcey
rm -rf /usr/local/bin/sourcey
mv ./sourcey /usr/local/bin/sourcey
rm -rf ./build
rm -rf ./dist
rm -f main.spec