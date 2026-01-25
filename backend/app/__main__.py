from argparse import ArgumentParser

import uvicorn

from app import app
from app.core.db import init_db
from app.seeders import seed_static


def main():
    # Seeders map
    seeders = {
        "static": seed_static,
    }

    # Init argument parser
    argparser = ArgumentParser(description="Acetaria backend")
    argparser_sub = argparser.add_subparsers(dest="command")

    # Web
    args_web = argparser_sub.add_parser("web", help="Run a web server")
    args_web.add_argument("--host", default="0.0.0.0", help="Host address")
    args_web.add_argument("--port", default=8000, type=int, help="Port number")

    # Seeders
    args_seed = argparser_sub.add_parser("seed", help="Run a specified seeder")
    args_seed.add_argument("seeder", choices=seeders.keys(), help="Seeder to run")

    # Parse arguments
    args = argparser.parse_args()

    # Run the web server
    if args.command == "web":
        uvicorn.run(app, host=args.host, port=args.port)

    # Run seeder
    if args.command == "seed":
        init_db()  # Ensure database is initialized
        seeders[args.seeder]()


if __name__ == "__main__":
    main()
