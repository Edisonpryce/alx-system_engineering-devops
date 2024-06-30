# Puppet Task: Managing Python Virtual Environment and Flask Installation

## Overview

This Puppet task automates the creation of a Python virtual environment, installs the Flask web framework within it, and terminates any running `python3` processes. The manifest ensures that the virtual environment is set up correctly, Flask is installed, and unnecessary `python3` processes are terminated to free up system resources.

## Prerequisites

- Puppet installed on the system
- Python 3 installed on the system
- `venv` module available in Python 3

## Files

- `manage_flask.pp`: The Puppet manifest file that contains the necessary configuration to create the virtual environment, install Flask, and kill the `python3` process.

## Puppet Manifest Details

### Create Virtual Environment

The `create_virtualenv` exec resource ensures that a Python virtual environment is created in the specified directory.

```puppet
exec { 'create_virtualenv':
  command => 'python3 -m venv /home/janice/myenv',
  creates => '/home/janice/myenv/bin/activate',
}
```

### Install Flask

The `install_flask` exec resource installs the Flask web framework within the created virtual environment. This resource depends on the `create_virtualenv` resource.

```puppet
exec { 'install_flask':
  command => '/home/janice/myenv/bin/pip install Flask==2.1.0',
  require => Exec['create_virtualenv'],
}
```

### Kill Python3 Process

The `kill_python3_process` exec resource terminates any running `python3` processes. This resource depends on the `install_flask` resource.

```puppet
exec { 'kill_python3_process':
  command => '/usr/bin/pkill python3',
  require => Exec['install_flask'],
}
```

## Instructions

1. **Save the Manifest**:
   Save the provided Puppet manifest to a file named `manage_flask.pp`.

2. **Apply the Manifest**:
   Run the following command to apply the manifest and execute the tasks:

   ```sh
   sudo puppet apply manage_flask.pp
   ```

3. **Verify**:
   - Check if the virtual environment is created at `/home/janice/myenv`.
   - Verify that Flask is installed within the virtual environment.
   - Ensure that any running `python3` processes have been terminated.

## Troubleshooting

- **Permission Denied**: Ensure that you have the necessary permissions to create directories and install packages. You might need to use `sudo` to apply the manifest.
- **Command Not Found**: Make sure that the paths to `python3`, `venv`, and `pkill` are correct. Use the `which` command to find the correct paths if necessary.

## Example Command

```sh
sudo puppet apply manage_flask.pp
```

By following these instructions, you can automate the setup of a Python virtual environment, install Flask, and manage processes using Puppet.

## Author

Janice - Puppet Configuration Management

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
