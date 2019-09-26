import logging

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults



class LoadDimensionOperator(BaseOperator):


    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 sql_template = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sql_template =  sql_template


    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        facts_sql = self.sql_template
        redshift.run(facts_sql)



