from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

topics = {

"carbon":["carbon emission","co2 emission"],
"fuel":["fuel consumption","fuel usage"],
"engine":["engine load","engine power"],
"speed":["ship speed","vessel speed"],
"weather":["wave height","wind speed"],
"efficiency":["ship efficiency"]

}

topic_embeddings = {
topic:model.encode(phrases)
for topic,phrases in topics.items()
}

def classify_question(question):

    q_embedding=model.encode(question)

    best_topic=None
    best_score=0

    for topic,emb in topic_embeddings.items():

        score=util.cos_sim(q_embedding,emb).max()

        if score>best_score:
            best_score=score
            best_topic=topic

    if best_score<0.4:
        return "unknown"

    return best_topic