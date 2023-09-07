

import paramiko

from jinja2 import Environment, FileSystemLoader

import yaml

env = Environment(loader=FileSystemLoader('.'))

# creating an ssh client object

ssh_client = paramiko.SSHClient()

# print(type(ssh_client))


ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',

#                    look_for_keys=False, allow_agent=False)


# Take user input for IP, port, username, and password

hostname = input("Enter the IP: ")

port = input("Enter the port: ")

username = input("Enter the username: ")

password = input("Enter the password: ")

# Define the data dictionary

router = {

    'hostname': hostname,

    'port': port,

    'username': username,

    'password': password

}

template = env.get_template('template.j2')

result = template.render(router)

dictionary = yaml.safe_load(template.render(hostname=hostname, port=port, username=username, password=password))

# Load existing data from YAML file, if it exists

existing_data = []

try:

    with open('data.yaml', 'r') as file:

        existing_data = yaml.safe_load(file)

except FileNotFoundError:

    pass

# Append the new dictionary to the existing data

existing_data.append(dictionary)

# Save the updated data to the YAML file

with open('data.yaml', 'w') as file:
    yaml.dump(existing_data, file)

print(f'Connecting to {router["hostname"]}')

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)  # using **kwargs

# checking if the connection is active

print(ssh_client.get_transport().is_active())