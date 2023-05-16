# Downloads organizer

## About

A simple python app which moves files in the ~/Downloads directory into sub-folders.

| Subfolder | Extension                                     |
| :-------- | :-------------------------------------------- |
| Pictures  | .jpg, .jpeg, .png, .svg                       |
| Binaries  | .deb, .run, .aab, .iso, .AppImage             |
| Documents | .pdf, .doc, .docx, .md, .pptx                 |
| Data      | .json, .csv, .xls, .xlsx, .xlsm, .ipynb, .bin |
| Other     | Any excluding above                           |

If a duplicate filename is found, the newer file is renamed **\<filename> (copy).\<suffix>**, **\<filename> (copy 2).\<suffix>** etc.
Ignores folders by default.

# Usage

Simply run the binary

```shell
./organizer
```

to organize your `~/Downloads` folder.

| Flag      | Description                      |
| :-------- | :------------------------------- |
| --create  | Create new subfolders if missing |
| --help    | Display usage information        |
| --version | Display version information      |
