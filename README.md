# Regex File Collector

Takes a directory path and then matches with all files paths within that directory that obeys a regex pattern. 
The files are then put into a structure where they are identified by the capture groups in the regex pattern. Each file needs to have a unique set of cature groups to identify it. 

## Flat getter
The file-paths can be obtained as a flat structure: a dictionary with a tuples of the capture groups as the keys, and the file names as values. 

## Tree structure getter
The file paths can be obtained as a nested dictionary where the catch groups are the keys. For instance: If simulations are perfomed and the outputs are put in folders with the parameter names in them `simulation_param1_200_param2_400`, then the value of the relevant file inside that directory can be obtained by:

```
collection = regex_file_collector.Collector(path, pattern)
filename_200_400 = collection.get_tree()["200"]["400"]
```


## Installation 

```
git clone https://github.com/henriasv/regex-file-collector.git
cd regex-file-collector
pip3 install .
```
