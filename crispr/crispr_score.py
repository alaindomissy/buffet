from __future__ import print_function
import argparse
from score import score
from config import SCORE_LOG_ON

parser = argparse.ArgumentParser()

parser.add_argument('prsp_file_wo_fasta_ext',
                     help='prsp_file_wo_fasta_ext: protospacers fasta file without the .fasta extension' )

parser.add_argument('blastdb_db',
                     help="blastdb_db: name of the blast database to blast the protospacers againt")

parser.add_argument('chunk_size',
                     help="chunk_size: number of protospacers to blast in each chunk")

parser.add_argument('max_hsps',
                     help="max_hsps: per scaffold hit, maximum number of hsps to return")

parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

parser.add_argument("-q", "--quiet", help="no logs",
                    action="store_true")

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
if args.quiet:
    print("logs turned off")
    SCORE_LOG_ON = False

score('./', args.prsp_file_wo_fasta_ext, args.blastdb_db, args.chunk_size, args.max_hsps)