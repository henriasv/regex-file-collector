import os
import re 


class Collector:
    def __init__(self, path, pattern, fields=None):
        self.fields = fields
        self.pattern = re.compile(pattern)
        self.files = {}
        print("The pattern contains", self.pattern.groups, "capturing groups")
        for root, _, files in os.walk(path):
            for name in files:
                fullfile = os.path.join(root, name)
                matches = re.findall(self.pattern, fullfile)
                if len(matches) == 1:
                    param_tuple = matches[0]
                    print(fullfile)
                    if not param_tuple in self.files.keys():
                        self.files[param_tuple] = fullfile
                    else:
                        raise DoubleEntryError
                    
                elif len(matches) > 1:
                    print("Found more than one match group")
                else: 
                    pass
                    
                
                #for file in files:
                #    print(os.path.join(name, file))

    def get_tree(self, custom_ordering=None):
        """ Get a nested dictionary of the files. 
        The tree structure will group elements based on the identifier tuples, from left to right
        Optinal custom_ordering that will change the order of the dictionary nesting. Only works if fields were provided upon creation of the Collection object. 
        """
        return_dict = {}
        for key, value in self.files.items():
            current_dict = return_dict
            if not custom_ordering is None:
                if not sorted(list(custom_ordering)) == sorted(list(self.fields)):
                    raise ValueError
                key = tuple([key[i] for i in [list(self.fields).index(element) for element in custom_ordering]])

            for i in range(len(key)):
                identifier = key[i]

                if i == len(key)-1:
                    if identifier in current_dict.keys():
                        raise DoubleEntryError
                    else: 
                        current_dict[identifier] = value

                if not identifier in current_dict.keys():
                    current_dict[identifier] = {}
                    current_dict = current_dict[identifier]
                else:
                    current_dict = current_dict[identifier]
                    
        return return_dict


    def get_flat(self):
        return self.files

    def print_ascii_tree(self):
        raise NotImplementedError
        
class DoubleEntryError(Exception):
    def __init__(self, expression, message):
        self.expression = expression 
        self.message = message
