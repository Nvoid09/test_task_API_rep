import argparse
import logging

import uvicorn

from test_task.api import app

# Logging config
logger = logging.getLogger('test_task')

log_config = uvicorn.config.LOGGING_CONFIG
format_str = '%(asctime)s - %(name)s_logger - %(levelname)s - %(message)s'
log_config["formatters"]["access"]["fmt"] = format_str
log_config["formatters"]["default"]["fmt"] = format_str


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        help="Listen IP",
        type=str,
        default="127.0.0.1"
    )
    parser.add_argument(
        "--port",
        help="Listen Port",
        type=int,
        default=8080
    )
    parser.add_argument(
        "-v", "--version",
        help="Show App Version",
        action="store_true"
    )
    args = parser.parse_args()

    logger.info('Module is starting...')

    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        log_config=log_config,
        forwarded_allow_ips=['*']
    )


if __name__ == "__main__":
    main()
