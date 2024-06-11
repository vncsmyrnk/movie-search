from flask import jsonify, Blueprint
from search.rank import query_rank_documents
from search.file import read_vocab, read_index


def build_routes():
    bp = Blueprint("bp_query", __name__)

    @bp.get("")
    def query():
        q = "music play urbanit"
        vocab = read_vocab()
        index = read_index()
        ranking = query_rank_documents(vocab, index, q)
        return jsonify(ranking)

    return bp
