from concurrent.futures import ThreadPoolExecutor

from src.usecase.get_conditioner import GetConditioner
from src.usecase.get_finisher import GetFinisher
from src.usecase.get_shampoo import GetShampoo


def main():
    run_parallel_usecase(
        lambda: GetShampoo().execute(),
        lambda: GetConditioner.execute(),
        lambda: GetFinisher.execute()
    )


def run_parallel_usecase(*tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()