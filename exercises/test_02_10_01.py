def test():
    assert (
        "doc1.similarity(doc2)" or "doc2.similarity(doc1)" in __solution__
    ), "Are you comparing the similarity of the two docs?"
    assert isinstance(
        similarity, float
    ), "The value of similarity needs to be a float. Did you calculate it correctly?"
    __msg__.good("Well done!")
