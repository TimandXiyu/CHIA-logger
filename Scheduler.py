from apscheduler.schedulers.blocking import BlockingScheduler
import HPool_Crawler
import logging
import os


if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)
    if not os.path.exists('worker_keywords.json'):
        raise FileNotFoundError('worker hash table not found')
    logging.info('scheduler started')
    scheduler = BlockingScheduler()
    logging.info(f'scheduler initialized, data will be downloaded at 10:00')
    scheduler.add_job(HPool_Crawler.main, 'cron',
                      hour='0-23/1',
                      misfire_grace_time=10)
    scheduler.add_job(HPool_Crawler.DailyAverage, 'cron',
                      hour=23, minute=50, misfire_grace_time=5)
    scheduler.start()




