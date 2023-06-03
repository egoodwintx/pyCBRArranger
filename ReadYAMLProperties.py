import yaml

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Example usage
file_path = 'config.yaml'
config = read_config(file_path)

# Access configuration properties
property1 = config['property1']
property2 = config['property2']
# ...

# Print the configuration properties
print(f"Property 1: {property1}")
print(f"Property 2: {property2}")
# ...
