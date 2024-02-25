## Steps to install virtual environment
open terminal where  you want to create the new project folder.
```bash 
mkdir project_name
cd project_name
```
Install Virtual Environment:
```bash
pip install virtualenv
python -m venv myenv
```

List all packages and export:
```bash
./myenv/Scripts/activate

pip list
<here install any package>
pip list > requirement.txt

```
To exit from virtual environment use this command :
```bash
deactivate
```
