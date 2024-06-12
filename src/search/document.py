def get_terms_from_document_index(index: list[list], doc: int) -> list[str]:
    """Returns the terms stored in the index for a document"""
    terms_doc = [item[0] for item in index if item[1] == doc]
    return terms_doc


def get_terms_from_documents_index(
    index: list[list], docs: set[int]
) -> dict[int:list]:
    """Returns the terms stored in the index for a document"""
    terms_docs = {}
    docs_filtered = [item for item in index if item[1] in docs]
    for item in docs_filtered:
        if item[1] not in terms_docs:
            terms_docs[item[1]] = []
        terms_docs[item[1]].append(item[0])
    return terms_docs


def get_tokens_from_document_index(
    vocab: list[str], index: list[list], doc: int
) -> list[str]:
    """Returns the tokens stored in the index for a document"""
    terms_doc = get_terms_from_document_index(index, doc)
    tokens_doc = [vocab[term_id] for term_id in terms_doc]
    return tokens_doc


def get_term_document_list_occurrence(
    vocab: list[str], index: list[list]
) -> dict[str:str]:
    """Returns the tokens stored in the index for all documents"""
    docs_terms = {}
    for doc_term in index:
        (term_id, doc_id) = (
            doc_term[0],
            doc_term[1],
        )
        if term_id not in docs_terms:
            docs_terms[term_id] = []
        docs_terms[term_id].append(doc_id)
    return docs_terms


def get_terms_id_from_tokens(
    vocab: list[str], query_tokens: list[str]
) -> list[str]:
    terms_ids = []
    for token in query_tokens:
        try:
            terms_ids.append(vocab.index(token))
        except ValueError:
            pass
    return terms_ids
