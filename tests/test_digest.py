import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from crispr.digest import coord_to_bedtuple_and_filename, digest_referencefastafile



def test_coord_to_bedtuple_filename():
    assert(coord_to_bedtuple_and_filename('chr6:136640001-136680000') ==
           ([('chr6', '136640000', '136680000')], 'chr6+136640001-136680000_40000')
           )


def digesttest_stretch_to_bedtuple_filename():
    assert(stretch_to_bedtuple_and_filename('chr6:136640001_40000') ==
           ([('chr6', '136640000', '136680000')], 'chr6+136640001-136680000_40000')
           )



# 42nt long section of of Scaffold02974 around the first cut from enzyme BfaI
#############################################################################
# with recognition site C^TA_G at one-based coords: 21,22,23,24
# GCGCTGGCCAGAACGTTCTC^TA_GGAATCGTGGAGAAGACATT

def test_digest_fastafile_42():
    pass

    # this requires bedtools being installed
    #
    # digest_referencefastafile('tests/data/fourtytwobp.fasta')
    #
    # with open('tests/data/fourtytwobp.fasta.prsp.bed') as prspbed:
    #     str(prspbed.read())=='fourtytwobps\t0\t20\tBfaI\t1000\t+\nfourtytwobps\t22\t42\tBfaI\t1000\t-\n'
    #
    # with open('tests/data/fourtytwobp.fasta.prsp.fasta') as prspfasta:
    #      str(prspfasta.read())=='fourtytwobps\t0\t20\tBfaI\t1000\t+\nfourtytwobps\t22\t42\tBfaI\t1000\t-\n'



