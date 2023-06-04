import yaml

# Class to store information about user preference

class Configuration:
    # set up default class members
    file_path = 'cbrProperties.yaml'
    tempdirStr = ""
    archivedirStr = ""
    cb7 = ""
    cbr = ""
    cba = ""
    cbz = ""
    cbt = ""

    # Access configuration properties
    def read_config(self, file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        self.tempdirStr = config['tempdir']
        self.archivedirStr = config['archivetype']
        
        # define the compression types
        self.cb7 = config["CB7"]
        self.cba = config["CBA"]
        self.cbt = config["CBT"]
        self.cbz = config["CBZ"]
        self.cbr = config["CBR"]
    
    # Return a configuration value
    def get_property(self, property_name):
        match property_name:
            case "tempdirStr":
                return self.tempdirStr
            case "archivedirStr":
                return self.archivedirStr
            case "compressorTypes":
                return {
                    "cbz" : self.cbz,
                    "cba" : self.cba,
                    "cbr" : self.cbr,
                    "cbz" : self.cbz,
                    "cbt" : self.cbt,
                    "cb7" : self.cb7
                }
            
    def __init__(self) -> None:
        self.read_config(self.file_path)


if __name__ == "__main__":
    cv = Configuration()