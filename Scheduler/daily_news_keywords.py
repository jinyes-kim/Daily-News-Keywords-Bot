from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

args = {'owner': 'Jinyes', 'start_date': days_ago(n=1)}

dag = DAG(dag_id='Daily_News_Keywords',
           default_args=args,
           schedule_interval='@daily')

t1 = BashOperator(task_id="crawler",
                  bash_command="python3 /home/jinyes/Daily-News-Keywords-Bot/Crawler/Naver/main.py",
                  dag=dag)

t2 = BashOperator(task_id="producer",
                  bash_command="python3 /home/jinyes/Daily-News-Keywords-Bot/Producer/producer.py",
                  dag=dag)

t3 = BashOperator(task_id="consumer",
                  bash_command="python3  /home/jinyes/Daily-News-Keywords-Bot/Consumer/main.py",
                  dag=dag)

t4 = BashOperator(task_id="slack-bot",
                  bash_command='python3 /home/jinyes/Daily-News-Keywords-Bot/Bot/main.py',
                  dag=dag)

t1 >> t2 >> t3 >> t4