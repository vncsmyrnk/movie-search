from search.rank import (
    jaccard_similarity,
    query_rank_documents,
)
from search.document import (
    get_terms_from_document_index,
    get_terms_id_from_tokens,
)
from search.text import preprocess_text


def test_jaccard_similarity():
    """Tests if jaccard algorithm is working as expected"""
    q = set(["to", "do", "be"])

    documents_test = [
        "to do is to be to be is to do",
        "to be or not to be i am what i am",
        "i think therefore i am do be do be do",
        "do do do da da da let it be let it be",
    ]

    jaccard_q_d1 = jaccard_similarity(q, set(documents_test[0].split()))
    jaccard_q_d2 = jaccard_similarity(q, set(documents_test[1].split()))
    jaccard_q_d3 = jaccard_similarity(q, set(documents_test[2].split()))
    jaccard_q_d4 = jaccard_similarity(q, set(documents_test[3].split()))

    assert round(jaccard_q_d1, 2) == 0.75
    assert round(jaccard_q_d2, 2) == 0.25
    assert round(jaccard_q_d3, 2) == 0.29
    assert round(jaccard_q_d4, 2) == 0.33

    print("Jaccard similarity ests passed")


def test_ranking():
    """Tests if the ranking algorithm is working as expected"""
    q = "house black red"
    vocab_test = [
        "black",
        "comput",
        "day",
        "exampl",
        "fine",
        "fun",
        "great",
        "hous",
        "music",
        "purpl",
        "red",
        "sky",
        "song",
        "test",
        "white",
    ]
    index_test = [
        (5, 0, [4]),
        (8, 0, [3]),
        (9, 0, [1]),
        (10, 0, [2]),
        (18, 0, [5]),
        (20, 0, [0]),
        (4, 1, [4]),
        (6, 1, [6]),
        (10, 1, [5]),
        (12, 1, [3]),
        (13, 1, [0]),
        (15, 1, [1]),
        (16, 1, [2]),
        (7, 2, [3]),
        (11, 2, [2]),
        (14, 2, [0]),
        (17, 2, [1]),
        (0, 3, [4]),
        (1, 3, [2]),
        (2, 3, [3]),
        (3, 3, [0]),
        (19, 3, [1]),
        (21, 3, [5]),
    ]

    ranking_test = query_rank_documents(vocab_test, index_test, q)
    print(ranking_test)

    assert ranking_test[0] == (
        jaccard_similarity(
            set(
                get_terms_id_from_tokens(
                    vocab_test, preprocess_text(q).split()
                )
            ),
            set(get_terms_from_document_index(index_test, 2)),
        ),
        2,
    )
    assert ranking_test[1] == (
        jaccard_similarity(
            set(
                get_terms_id_from_tokens(
                    vocab_test, preprocess_text(q).split()
                )
            ),
            set(get_terms_from_document_index(index_test, 0)),
        ),
        0,
    )
    assert ranking_test[2] == (
        jaccard_similarity(
            set(
                get_terms_id_from_tokens(
                    vocab_test, preprocess_text(q).split()
                )
            ),
            set(get_terms_from_document_index(index_test, 3)),
        ),
        3,
    )
    assert ranking_test[3] == (
        jaccard_similarity(
            set(
                get_terms_id_from_tokens(
                    vocab_test, preprocess_text(q).split()
                )
            ),
            set(get_terms_from_document_index(index_test, 1)),
        ),
        1,
    )


def test_query_http_request(client):
    """Tests if the web server is returning the expected query results"""
    response = client.get("/api/query?q=music%20play")
    assert response.status_code == 200
    assert len(response.json) == 10
    assert response.json[0]["movie_id"] == 3304
    assert response.json[0]["score_jaccard"] == 0.4
