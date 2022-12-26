import argparse

import readme_generator
from workspace_creators import AocWorkspaceCreator


def prepare_workspace_for_problem(url: str):
    workspace_creator = AocWorkspaceCreator(url)
    workspace_creator.create_workspace()


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("url")

    args = arg_parser.parse_args()

    prepare_workspace_for_problem(args.url)
    readme_generator.main()


if __name__ == "__main__":
    main()
