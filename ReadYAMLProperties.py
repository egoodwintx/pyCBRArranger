import yaml

# Class to store information about user preference

class Configuration:
    # get CBRArranger config file
    file_path = 'cbrProperties.yaml'




    # Access configuration properties
    def read_config(file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        tempdirStr = config['tempdir']
        archivedirStr = config['archivetype']
        return config
    
    # Return a configuration value
    def get_property(property_name):
        match property_name:
            case "tempdirStr":
                return self.tempdirStr
            case "archivedirStr":
                return self.archivedirStr
            
    def __init__(self) -> None:
        self.read_config(self.file_path)


if __name__ == "__main__":
    cv = Configuration()
    cv.run()