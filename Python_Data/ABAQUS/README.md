# Abaqus Reader
A small python-based Abaqus inp file parser/reader (using parser lib [lark-parser](https://github.com/lark-parser/lark))

## Dependencies: 
Install lark-parser by 
```
pip install lark-parser
```

## Usage:
```
python abaqusInpReader.py INPUTFILENAME.inp
```
The script will parse the input file and write out selected section of input file.
(At the moment it targets *Node* and *Nset*)

## TODO Known rough edges
1. `os.mkdir` throws exception
2. crude handling after "*End Assembly"
3. Error handling in parsing
(?) migrate to Python3?
