import os

from buffet.cut import cut_file


BLASTDB =  os.environ.get('BLASTDB','/root/blastdb/')

SCAFFOLDS =  os.environ.get('SCAFFOLDS','/root/scaffolds/mm8/')




#
# main.blast(SCAFFOLDS, 'chr6:136640001-136641000_1000.prsp', '/BLASTDB/', 'mm8')
# from buffet import cut

# cut.cut_file(SCAFFOLDS + 'chr6-1-400' + 'fasta')
#
# from buffet import digest
# digest.digest_file(SCAFFOLDS + 'hg38' + 'fasta')
# digest.digest_coord(SCAFFOLDS +'chr21:42774475-42905100' + 'fasta' ,'mm8', SCAFFOLDS + 'mm8.fasta )


def payload(params_value):

    coord = params_value.get('Input.genomic-coord', 'chr6-1-400.fasta')
    # genome = args_value['Input.genome-id']
    # chunk_size = args_value['Input.blast_chunk_size']
    # max_hsps = args_value['Input.blast_max_hsps']

    # args_value['Input.binding_interference_spacing']

    cuts = cut_file(SCAFFOLDS + coord + '.fasta')

    return cuts
