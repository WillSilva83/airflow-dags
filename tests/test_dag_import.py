from airflow.models import DagBag


def test_dags_import_without_errors():
    dag_bag = DagBag(dag_folder="dags", include_examples=False)

    assert dag_bag.import_errors == {}, dag_bag.import_errors
    assert "hello_airflow" in dag_bag.dags
