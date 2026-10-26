import subprocess

drive = input("Type the drive: (D:, E:...): ").strip().upper()

if len(drive) != 2 or drive[0] not in "DEFGHIJKLMNOPQRSTUVWXYZ" or drive[1] != ":":
    print("Invalid drive letter.")
    exit()

confirm = input(f"Are you sure? (Type y) ")

if confirm != "y":
    print("Cancelled.")
    exit()


command = (
    f"Format-Volume -DriveLetter {drive[0]} "
    "-FileSystem exFAT -NewFileSystemLabel USB -Confirm:$false"
)

subprocess.run(
    ["powershell", "-NoProfile", "-Command", command],
    check=True
)
