pwd, check pythoon version python --version
create virtual environment
python -m venv py_env

activation
.\py_env/Scripts/Activate.ps1




if you face error in activation

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


install airflow 
pip install 'apache-airflow==2.8.0' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.0/constraints-3.11.txt"




