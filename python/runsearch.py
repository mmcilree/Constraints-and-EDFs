import argparse
import json
import math
from os import listdir, system, SEEK_END
import time

# This is the main script for automatically running conjure on .param files in the
# gap/params folder. It can also be used to collate conjure output to a JSON files.

# Matthew McIlree 2022ß∑∑

start_time = time.time()

# Default options
PARAM_PATH = "./gap/params"
CONJURE_OUTPUT_PATH = "./conjure-output"
ESSENCE_FILE = "./essence/edf.essence"
TIMEOUT = "30"
NUM_SOLS = "1"

def lcm(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    return lcm

def got_solution(paramfile):
    # Check if one solution has been found yet.
    outputfiles = listdir(CONJURE_OUTPUT_PATH)
    for s in outputfiles:
        if paramfile[:-6] in s and s.endswith(".solution"):
            return True
    return False

def all_models(findone):
    # Run on all parameter sets in the gap/params folder
    files = listdir(PARAM_PATH)
    for f in sorted(files):
        if f.endswith(".param"):
            system(
                "conjure solve {0} {1}/{2} --limit-time {3} --output-format=json --number-of-solutions={4} --smart-filenames ".format(
                    ESSENCE_FILE, PARAM_PATH, f, TIMEOUT, NUM_SOLS
                )
            )
        current_time = time.time()
        print(current_time - start_time)

        # If findone is true, stop after we find one solutionß
        if findone:
            if got_solution(f):
                break


def one_model(modelpath):
    # Run on just a single specified .param file.
    system(
        "conjure solve {0} {1} --limit-time {2} --output-format=json --number-of-solutions={3} --smart-filenames ".format(
            ESSENCE_FILE, modelpath, TIMEOUT, NUM_SOLS
        )
    )


def clean_output(path, rwedf):
    # Read all of the conjure json output files, extract the important bits
    # and store in a single file
    
    files = listdir(CONJURE_OUTPUT_PATH)
    outputfile = open(path, "w+")
    output = []
    for filepath in files:
        if filepath.endswith(".json"):
            metadata = filepath.split("_")
            f = open(CONJURE_OUTPUT_PATH + "/" + filepath, "r")
            data = json.load(f)
            f.close()

            if rwedf:
                rwedf = [[x for x in s.values()] for s in data["edf"].values()]
                group = [int(metadata[1]), int(metadata[2])]
                numsets = int(metadata[3])
                setsizes = json.loads(metadata[4])
                dups = int(metadata[5].split("-")[0]) / lcm(setsizes + [group[1]])
                record = {
                    "rwedf": rwedf,
                    "group": group,
                    "setsize": setsizes,
                    "numsets": numsets,
                    "dups": dups,
                }
                output.append(record)
            else:
                try:
                    osedf = [[x for x in s.values()] for s in data["edf"].values()]
                    overgroup = [int(metadata[1]), int(metadata[2])]
                    subgroup = [int(metadata[3]), int(metadata[4])]
                    numsets = int(metadata[5])
                    setsize = int(metadata[6])

                    dups = int(metadata[7].split("-")[0])
                    record = {
                        "osedf": osedf,
                        "overgroup": overgroup,
                        "subgroup": subgroup,
                        "setsize": setsize,
                        "numsets": numsets,
                        "dups": dups,
                    }
                    output.append(record)
                except ValueError:
                    continue

    if len(outputfile.readlines()) == 0:
        outputfile.write("[")
    else:
        outputfile.seek(-1, SEEK_END)
        outputfile.truncate()

    for i, r in enumerate(output):
        outputfile.write(
            json.dumps(r, sort_keys=True)
            + ("," if i != len(output) - 1 else "")
            + "\n\n"
        )
    outputfile.write("]")

# Parse command line arguments
parser = argparse.ArgumentParser(
    description="Automate the running of conjure on lots of models"
)

parser.add_argument("--allmodels", action="store_true")
parser.add_argument("--fromimage", action="store_true")
parser.add_argument("--makeimage", action="store_true")
parser.add_argument("--rwedf", action="store_true")
parser.add_argument("--findone", action="store_true")
parser.add_argument("--onemodel")
parser.add_argument("--cleanoutput")
parser.add_argument("--timeout")
parser.add_argument("--numsols")

args = parser.parse_args()

# Set options accordinglyß
if args.timeout is not None:
    TIMEOUT = str(args.timeout)
if args.numsols is not None:
    NUM_SOLS = str(args.numsols)
if args.fromimage:
    ESSENCE_FILE = "essence/edffromimage.essence"
elif args.makeimage:
    ESSENCE_FILE = "essence/edfimage.essence"
elif args.rwedf:
    ESSENCE_FILE = "essence/rwedf.essence"

# Perform specified taskß
if args.allmodels:
    all_models(args.findone)
elif args.onemodel is not None:
    one_model(args.onemodel)

if args.cleanoutput is not None:
    clean_output(args.cleanoutput, args.rwedf)
