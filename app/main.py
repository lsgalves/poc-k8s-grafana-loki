import time
import random
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(name)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('app-logger')


def main():
    logger.info("Starting the application...")

    while True:
        try:
            logger.info("Working...")
            random_number = random.randint(1, 100)
            logger.info(f"Generated random number: {random_number}")
            if random_number < 10:
                logger.warning(f"NUMBER TOO LOW: Random number `{random_number}` is less than 10.")
            if random_number > 90:
                logger.error(f"NUMBER TOO HIGH: Random number `{random_number}` is greater than 90.")

            time.sleep(3)

        except KeyboardInterrupt:
            logger.info("Application interrupted by user.")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            break

    logger.info("Application finished successfully.")


if __name__ == "__main__":
    main()
