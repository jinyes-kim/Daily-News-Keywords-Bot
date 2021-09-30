from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

args = {'owner': 'Jinyes', 'start_date': days_ago(n=1)}

dag = DAG(dag_id='Daily-News-Keywords',
           default_args=args,
           schedule_interval='@daily')

t1 = BashOperator(task_id="crawler",
                  bash_command='date', # 커맨드
                  dag=dag)

t2 = BashOperator(task_id="producer",
                  bash_command='sleep 3',
                  dag=dag)

t3 = BashOperator(task_id="consumer",
                  bash_command='whoami',
                  dag=dag)

t4 = BashOperator(task_id="slack-bot",
                  bash_command='whoami',
                  dag=dag)

t1 >> t2 >> t3 >> t4
