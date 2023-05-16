from pathlib import Path
from sys import argv, exit
from version import VERSION


def should_create_folders():
    return "--create" in argv


def parse_args():
    if "--help" in argv:
        print_usage()
        exit(0)
    elif "--version" in argv:
        print_version()
        exit(0)
    elif len(argv) > 1:
        print("Error: Unrecognized argument")
        exit(1)


def print_usage():
    print(
        f"""Downloads organizer {VERSION}
Flags:
    --create        # Create required folders if missing
    --help          # Print this usage information
    --version       # Print version information
""",
    )


def print_version():
    print(VERSION)


class DownloadsOrganizer:
    def __init__(self):
        self.downloads = Path("~/Downloads").expanduser()
        self.pictures = self.downloads.joinpath(Path("Pictures"))
        self.documents = self.downloads.joinpath(Path("Documents"))
        self.binaries = self.downloads.joinpath(Path("Binaries"))
        self.other = self.downloads.joinpath(Path("Other"))
        self.data = self.downloads.joinpath(Path("Data"))
        if should_create_folders():
            self.pictures.mkdir(exist_ok=True)
            self.documents.mkdir(exist_ok=True)
            self.binaries.mkdir(exist_ok=True)
            self.data.mkdir(exist_ok=True)
            self.other.mkdir(exist_ok=True)

    def didInitialize(self) -> bool:
        return all(
            [
                self.downloads.exists(),
                self.pictures.exists(),
                self.documents.exists(),
                self.binaries.exists(),
                self.other.exists(),
                self.data.exists(),
            ]
        )

    def move_files(self) -> int:
        count = 0
        image_patterns = [".jpg", ".jpeg", ".png", ".svg"]
        binary_patterns = [".deb", ".run", ".aab", ".iso", ".AppImage"]
        document_patterns = [".pdf", ".doc", ".docx", ".md", ".pptx"]
        data_patterns = [".json", ".csv", ".xls", ".xlsx", ".xlsm", ".ipynb", ".bin"]

        for file in self.downloads.glob("*"):
            if file.suffix in image_patterns:
                self.move_file(file, self.pictures)
                count += 1
            elif file.suffix in binary_patterns:
                self.move_file(file, self.binaries)
                count += 1
            elif file.suffix in document_patterns:
                self.move_file(file, self.documents)
                count += 1
            elif file.suffix in data_patterns:
                self.move_file(file, self.data)
                count += 1
            elif file.is_file():
                self.move_file(file, self.other)
                count += 1
        return count

    def move_file(self, file: Path, folder: Path):
        if folder.joinpath(file.name).exists():
            count = 2
            name = f"{file.stem} (copy){file.suffix}"
            while folder.joinpath(name).exists():
                name = f"{file.stem} (copy {count}{file.suffix}"
                count += 1
            file.rename(folder / name)
        else:
            file.rename(folder / file.name)

    def __repr__(self):
        return str(self.downloads)
