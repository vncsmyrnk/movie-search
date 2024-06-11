from flask import jsonify, request, Blueprint
from search.rank import query_rank_documents
from search.file import read_vocab, read_index, read_reviews


def build_routes():
    bp = Blueprint("bp_query", __name__)

    @bp.get("")
    def query():
        """GET route for querying movie descriptions"""
        q = request.args.get("q")
        if not q:
            return {"error": 'Query string param "q" should be informed.'}, 400
        vocab = read_vocab()
        index = read_index()
        reviews = read_reviews()
        ranking = query_rank_documents(vocab, index, q)
        ranking_details = [
            {
                "movie_id": item[1],
                "score_jaccard": item[0],
                "movie": reviews[item[1]],
            }
            for item in ranking
        ]
        return jsonify(ranking_details)

    return bp
