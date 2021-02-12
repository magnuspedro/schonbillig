import time
from concurrent.futures import ThreadPoolExecutor

from src.config.logger.logging_module import PTLogger
from src.usecase.get_conditioner import GetConditioner
from src.usecase.get_finisher import GetFinisher
from src.usecase.get_leave import GetLeave
from src.usecase.get_permament import GetPermanent
from src.usecase.get_shampoo import GetShampoo
from src.usecase.get_shaper import GetShaper
from src.usecase.get_treatment import GetTreatment

logger = PTLogger(name=__name__)


def main():
    # GetShampoo().execute(),
    # GetConditioner.execute(),
    # GetFinisher.execute(),
    # GetTreatment.execute()
    start = time.time()
    run_parallel_usecase(
        lambda: GetLeave.execute(),
        lambda: GetShampoo().execute(),
        lambda: GetConditioner.execute(),
        lambda: GetFinisher.execute(),
        lambda: GetTreatment.execute(),
        lambda: GetShaper.execute(),
        lambda: GetPermanent.execute(),
    )
    end = time.time()
    logger.info(f'Execution Time: {(end - start) / 60}m')


def run_parallel_usecase(*tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
    for running_task in running_tasks:
        running_task.result()
