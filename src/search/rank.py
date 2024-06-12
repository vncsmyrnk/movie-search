import heapq
from .text import preprocess_text
from .document import (
    get_terms_id_from_tokens,
    get_terms_from_documents_index,
)


def jaccard_similarity(set1: set[str], set2: set[str]) -> float:
    """Computes the Jaccard similarity between two sets."""
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    if union == 0:
        return 0.0
    return intersection / union


def query_rank_documents(
    vocab: list[str], index: list[list], query: str, top_count: int = 10
) -> list[tuple]:
    """
    Returns a list with the top N most relevant documents according to a query
    """
    query_tokens = set(preprocess_text(query).split())
    query_terms = set(get_terms_id_from_tokens(vocab, query_tokens))

    # Filter documents that contain the specific words in the query
    candidate_docs = set([item[1] for item in index if item[0] in query_terms])

    # Search all the relevant documents contents
    candidate_docs = get_terms_from_documents_index(index, candidate_docs)

    # Calculate Jaccard similarity for candidate documents
    min_heap = []
    for doc_id, doc_terms in candidate_docs.items():
        score = jaccard_similarity(query_terms, set(doc_terms))

        # If the heap is smaller than top_n, add the new score
        if len(min_heap) < top_count:
            heapq.heappush(min_heap, (score, doc_id))
        else:
            # If the new score is larger than the smallest in the heap,
            # replace the smallest
            if score > min_heap[0][0]:
                heapq.heapreplace(min_heap, (score, doc_id))

    # Extract the top N elements in descending order
    top_documents = sorted(min_heap, key=lambda x: x[0], reverse=True)
    return top_documents
