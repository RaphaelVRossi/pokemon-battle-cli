#!/usr/bin/python
# -*- coding: utf-8 -*-

# pokemon battle cli
# https://github.com/RaphaelVRossi/pokemon-battle-cli

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 raphaelrossi raphael.vieira.rossi@gmail.com

import argparse
import logging
import sys

def generate_team():
    logging.debug("Team generated [001, 003, 004, 005, 006, 009]")

def main(params=None):
    if params is None:
        params = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Pokemon Battle CLI")

    team_group = parser.add_argument_group("Team")
    team_group.add_argument("-t", "--team", help="Pokemon Team")
    team_group.add_argument("--random-team", help="Random Team")

    other_group = parser.add_argument_group("Other Arguments")
    other_group.add_argument("-l", "--level", default="debug", help="Logging level")

    arguments = parser.parse_args(params)

    logging.basicConfig(level=getattr(logging, arguments.level.upper()))

    generate_team()

if __name__ == "__main__":
    main()
