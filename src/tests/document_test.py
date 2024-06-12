from search.document import (
    get_terms_from_documents_index,
    get_terms_from_document_index,
    get_term_document_list_occurrence,
    get_terms_id_from_tokens,
)


def test_get_documents_by_terms(index):
    terms_doc_10 = get_terms_from_document_index(index, 10)
    terms_doc_56 = get_terms_from_document_index(index, 56)
    terms_doc_1005 = get_terms_from_document_index(index, 1005)

    all_terms_expected = {
        10: terms_doc_10,
        56: terms_doc_56,
        1005: terms_doc_1005,
    }

    terms_docs = get_terms_from_documents_index(index, [10, 56, 1005])
    assert all_terms_expected == terms_docs


def test_list_occurence_size(index, vocab):
    docs_terms = get_term_document_list_occurrence(vocab, index)
    assert len(vocab) == len(docs_terms.keys())


def test_terms_from_tokens(vocab):
    query_tokens = [
        vocab[1000],
        vocab[1001],
        "random_non_existent",
        vocab[2506],
    ]
    terms_ids = get_terms_id_from_tokens(vocab, query_tokens)
    assert [1000, 1001, 2506] == terms_ids
