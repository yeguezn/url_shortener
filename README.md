# URL shortener

## Main development tools
1. Python (3.10.12)
2. Django framework (4.2.7)
3. PostgreSQL (14.9)

## Installation
1. Clone this repository
```bash script
git clone https://github.com/yeguezn/url_shortener your-folder-name
```
2. Create a virtual environment
```bash script
python3 -m venv .venv
```
3. Activate virtual environment

Windows
```bash script
cd venv/scripts
activate
cd..
cd.. 
```

Linux
```bash script
cd ./.venv/bin
source activate
cd ..
cd ..
```
4. Install dependencies
```bash script
pip install -r requirements.txt
```

5. Create a database named shortener in PostgreSQL
~~~~sql
CREATE DATABASE shortener;
~~~~
6. Run makemigrations command
```bash script
python manage.py makemigrations
```
7. Run migrate command
```bash script
python manage.py migrate shortener
```
8. Run the application
```bash script
python manage.py runserver
```
9. Do click in the next link
[http://localhost:8000](http://localhost:8000)
