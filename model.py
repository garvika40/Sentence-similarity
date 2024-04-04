from sentence_transformers import SentenceTransformer, util

model_path = "./model"
model = SentenceTransformer(model_path)


def compute_similarity(text1, text2):
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)
    cosine_similarities = util.cos_sim(embeddings1, embeddings2)
    return cosine_similarities.item()
