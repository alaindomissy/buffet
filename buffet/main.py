########################################################################################################################
#
# MAIN
#
# API functions: digest_and_blast_and_score_coord
#
########################################################################################################################

from buffet.digest import digest_coord, digest_stretch
from buffet.blast import blast
from buffet.score import score
from buffet.cluster import cluster



#########################################################
# DIGEST AND BLAST
#########################################################

def digest_and_blast_coord(direct, coord, reference, blastdb_db, chunk_size=50, max_hsps=50):
    focusfn = digest_coord(direct, coord, reference)
    nbr = blast(direct, focusfn + '.prsp', blastdb_db, chunk_size=chunk_size, max_hsps=max_hsps)
    return nbr

def digest_and_blast_stretch(direct, stretch, reference, blastdb_db, chunk_size=100, max_hsps=100):
    focusfn = digest_stretch(direct, stretch, reference)
    nbr = blast(direct, focusfn + '.prsp', blastdb_db, chunk_size=chunk_size, max_hsps=max_hsps)
    return nbr


#########################################################
# BLAST AND SCORE
#########################################################

def blast_and_score(direct, fn_noext, blastdb_db, chunk_size=50, max_hsps=50,
                    reref_substrate_id='chr6', low=75, high=75, load_genome=True, howmany=24):
    nbr = blast(direct, fn_noext, blastdb_db, chunk_size=chunk_size, max_hsps=max_hsps)
    guides = score(direct, fn_noext, blastdb_db, chunk_size=chunk_size, nbrofchunks=nbr,
          reref_substrate_id='chr6', load_genome=load_genome)
    return cluster(guides, direct, reref_substrate_id, low=75, high=75, howmany=None)


#########################################################
# DIGEST AND BLAST AND SCORE
#########################################################

# requires:
# blastdb database
# dict      a genome fasta file against which pam lookup is optionnaly done for guides candidates
# genome    same, used when (correctly) blasting agaist whole geome
#
# TODO get rid of reref_substrate_id122
def digest_and_blast_and_score_coord(direct, coord, reference, blastdb_db, chunk_size=50, max_hsps=50,
                                     reref_substrate_id='chr6', low=75, high=75, load_genome=False, howmany=None):
    """

    :param direct:
    :param coord:
    :param reference:
    :param blastdb_db:
    :param chunk_size:
    :param max_hsps:
    :param reref_substrate_id:
    :param low:
    :param high:
    :param load_genome:
    :param howmany:
    :return:
    """
    focusfn = digest_coord(direct, coord, reference)
    fn_noext = focusfn + '.prsp'
    nbr = blast(direct, fn_noext, blastdb_db, chunk_size=chunk_size, max_hsps=max_hsps)
    guides = score(direct, fn_noext, blastdb_db, chunk_size=chunk_size, nbrofchunks=nbr,
          reref_substrate_id='chr6', load_genome=load_genome)
    return cluster(guides, direct, reref_substrate_id, low, high, howmany, fn_noext)


# TODO merge with the above onto one flexible input function
def digest_and_blast_and_score_stretch(direct, stretch, reference, blastdb_db, chunk_size=50, max_hsps=50,
                                       reref_substrate_id='chr6', low=75, high=75, load_genome=False, howmany=None):
    """

    :param direct:
    :param stretch:
    :param reference:
    :param blastdb_db:
    :param chunk_size:
    :param max_hsps:
    :param reref_substrate_id:
    :param low:
    :param high:
    :param load_genome:
    :param howmany:
    :return:
    """
    # TODO validation of input as either coord with a - or stretch with a _
    # assert type(stretch) is type(""), "requires a string"
    focusfn = digest_stretch(direct, stretch, reference)
    fn_noext = focusfn + '.prsp'
    nbr = blast(direct, fn_noext, blastdb_db, chunk_size=chunk_size, max_hsps=max_hsps)
    guides = score(direct, fn_noext, blastdb_db, chunk_size=chunk_size, nbrofchunks=nbr,
          reref_substrate_id='chr6', load_genome=load_genome)
    return cluster(guides, direct, reref_substrate_id, low, high, howmany, fn_noext)
