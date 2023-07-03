# Downtime Diary
<!-- python badge -->
![OS](https://img.shields.io/badge/Operating%20System-Linux-blue)
![OS](https://img.shields.io/badge/Python-3.10-blue)

A simple and lightweight downtime logger for your linux server

## Installation
To install the downtime diary, simply download the .whl file from the releases page and run the following command:
```bash
pip install <path to .whl file>
```

## Usage
To use the downtime diary, simply run the following command:
```bash
python -m downtime <command>
```

## Commands
Here is a list of all the commands available:
### Add
The add command allows you to add a downtime entry to the log. To use the add command, simply run the following command:
```bash
python -m downtime add
```
This will then walk you through the process of adding a downtime entry to the log.
downtime diary will then ask you for the following information:
- Start time (The time the downtime started)
- End time (The time the downtime ended)
- Reason (What caused the downtime)
- Severity (Minor, Major, Critical or Maintenance)
- Note (Any additional information you want to add)

The downtime will be added to the log file located in `~/.downtimes.log`

### View
The veiw command allows you to see all past downtime entries. To use the view command, simply run the following command:
```bash
python -m downtime view
```
This will then show you all past downtime entries in the log file.

### Clear
The clear command allows you to clear the log file. To use the clear command, simply run the following command:
```bash
python -m downtime clear
```
This will then clear the log file located in `~/.downtimes.log`

### Help
The help command allows you to view this help page. To use the help command, simply run the following command:
```bash
python -m downtime help
```
This will then show you this help page.

## Contributing
If you would like to contribute to the downtime diary, please fork the repository and submit a pull request.