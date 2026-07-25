import argparse


def preload(parser: argparse.ArgumentParser):
    try:
        parser.add_argument(
            "--ad-no-huggingface",
            action="store_true",
            help="Do not automatically download YOLO models",
        )
    except argparse.ArgumentError:
        pass
