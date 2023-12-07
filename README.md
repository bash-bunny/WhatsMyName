# Description

Python wrapper for the WhatsMyName repo

Check their awesome work in their repo [Github Repo WebBreacher WhatsMyName](https://github.com/WebBreacher/WhatsMyName/tree/main)

# Requirements

The program makes use of the following libraries

```txt
json
requests
```

And also make use of the `wmn-data.json` file from the [WebBreacher Github Repo](https://github.com/WebBreacher/WhatsMyName/blob/main/wmn-data.json)

*Note: It's recommended to update the file `wmn-data.json` often*

## Installation

```bash
git clone https://github.com/DeadS3c/WhatsMyName.git
cd WhatsMyName
python -m venv venv
. venv/bin/activate
pip install requirements.txt
```

## Usage

Just pass the username that you are looking for to the program and it would look at every url that the wmn-data.json file has

```bash
python whatsmyname.py username
```

