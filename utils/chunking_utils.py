def chunk_text(text, chunk_size=2000, overlap=200):
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")
    if chunk_size <= overlap:
        raise ValueError("Chunk size must be greater than overlap")

    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks