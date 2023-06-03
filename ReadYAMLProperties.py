import yaml

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# get CBRArranger config file
file_path = 'cbrProperties.yaml'
config = read_config(file_path)

# Access configuration properties
tempdirStr = config['tempdir']
archivedirStr = config['archivetype']


# Print the configuration properties
print(f"Property 1: {tempdirStr}")
print(f"Property 2: {archivedirStr}")

