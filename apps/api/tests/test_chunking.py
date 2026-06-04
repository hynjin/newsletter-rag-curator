from app.services.chunking import ChunkingService


def test_short_text_produces_one_chunk() -> None:
    service = ChunkingService(target_tokens=20, max_tokens=25, overlap_tokens=5)

    chunks = service.chunk_text("This is a short newsletter paragraph.")

    assert len(chunks) == 1
    assert chunks[0].chunk_index == 0
    assert chunks[0].content == "This is a short newsletter paragraph."
    assert chunks[0].token_count == 6


def test_long_text_produces_ordered_chunks_with_overlap() -> None:
    service = ChunkingService(target_tokens=6, max_tokens=8, overlap_tokens=2)
    text = "\n\n".join(
        [
            "one two three four",
            "five six seven eight",
            "nine ten eleven twelve",
        ]
    )

    chunks = service.chunk_text(text)

    assert [chunk.chunk_index for chunk in chunks] == [0, 1, 2]
    assert chunks[0].content == "one two three four"
    assert chunks[1].content == "three four five six seven eight"
    assert chunks[2].content == "seven eight nine ten eleven twelve"


def test_large_paragraph_splits_by_max_tokens() -> None:
    service = ChunkingService(target_tokens=5, max_tokens=5, overlap_tokens=1)
    text = " ".join(str(index) for index in range(12))

    chunks = service.chunk_text(text)

    assert [chunk.content for chunk in chunks] == [
        "0 1 2 3 4",
        "4 5 6 7 8",
        "8 9 10 11",
    ]


def test_empty_text_produces_no_chunks() -> None:
    service = ChunkingService()

    assert service.chunk_text("   \n\n  ") == []
