from utils import DownloadsOrganizer, parse_args
from sys import exit

if __name__ == "__main__":
    parse_args()
    organizer = DownloadsOrganizer()
    if not organizer.didInitialize():
        print(
            "Some folders could not be located. "
            "Please run with --create to create them."
        )
        exit(1)
    print("Organized", organizer.move_files(), "files.")
    exit(0)
