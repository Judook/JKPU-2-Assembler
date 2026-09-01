# JKPU-2-Assembler

>I have not yet uploaded a world download link for my computer, but I sure will in the near future, when it will be completed. I have also not provided the link to the ISA file to the custom assembly language used in this computer.

This is the assembler and supporting programs written for my minecraft CPU JKPU-2.

## How to use this thing

There are two python scripts in the repo - `assembler.py` and `schematicMaker.py`. There is also a file called `program.asm`, where the program to be assembled is stored.

### Usage

1. Edit the `program.asm` according to the ISA for the computer and write your assembly code in it. Make sure to save the file.
2. Run `assembler.py`.
3. Then run `schematicMaker.py`.
4. A file will be created in the `schems` folder. Copy that file into the schematics folder in your desired location(preferably, the schematics folder used by __World edit__.
5. Paste the schematics into the minecraft world using __WorldEdit__ by standing exactly on top of the the first line in the program memory(most probably white stained glass, on the corner near to the ALU).
