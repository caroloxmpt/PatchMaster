# PatchMaster - Executable Patcher

PatchMaster is a simple and intuitive tool for patching Windows executable files (.exe). It allows users to search for a specific binary pattern within an executable file and replace it with a new pattern. The tool provides a graphical user interface (GUI) for easy use, making it accessible for users without programming experience.

## Features

- **Load Executable Files**: Easily select and load executable files for patching.
- **Pattern Matching and Replacement**: Input hex patterns to search and replace binary data.
- **GUI Interface**: User-friendly interface built with `tkinter`.
- **File Saving**: Save patched files with a custom name and location.

## How It Works

1. **Load an Executable**: Choose an `.exe` file from your computer to begin the patching process.
2. **Specify Patterns**: Enter the hex pattern to search for and the hex pattern to replace it with. Ensure both patterns have the same length.
3. **Apply the Patch**: PatchMaster will search for the pattern in the executable and replace it.
4. **Save the Patched File**: Save the modified file to your desired location.

## Requirements

- Python 3.x
- Standard `tkinter` library (pre-installed with Python)

## Use Cases

- Modify or customize executables for testing purposes.
- Replace specific binary data within executables.
- Educational purposes for understanding binary patching.

## Notes

- Ensure you have permission to modify the executable files you work with.
- Always create a backup of the original file before applying patches.
- Use this tool responsibly and in compliance with software licenses and terms of use.

## Disclaimer

PatchMaster is provided "as is" without warranty of any kind. The creators are not responsible for any unintended consequences, including but not limited to corrupted files, data loss, or legal issues resulting from improper use of this tool.
