from confidential import get_main_llm, get_embeddings_llm, get_vector_db, get_prediction

class Chatbot:
    def __init__(self, main_model_id='GritLM-7B', main_model_temperature=0.7, main_model_max_new_tokens=200,
                 embeddings_model_id='mxbai-embed-large-v1', embeddings_device=0, search_k=1, chunk_size=1024, chunk_overlap=128, question='Hello!'):

        self.main_model_id = main_model_id
        self.main_model_temperature = main_model_temperature
        self.main_model_max_new_tokens = main_model_max_new_tokens
        self.main_llm = None
        self.embeddings_model_id = embeddings_model_id
        self.embeddings_device = embeddings_device
        self.embeddings_llm = None
        self.search_k = search_k
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.vector_db = None
        self.question = question
        self.prediction = ''

    def construct_main_llm(self):
        self.main_llm = get_main_llm(
            self.main_model_id, self.main_model_temperature, self.main_model_max_new_tokens)

    def construct_embeddings_llm(self):
        if self.main_model_id == 'Meta-Llama-3-8B-Instruct':
            self.embeddings_device = 0
        self.embeddings_llm = get_embeddings_llm(
            self.embeddings_model_id, self.embeddings_device)

    def generate_vector_db(self):
        self.vector_db = get_vector_db(
            self.embeddings_llm, self.chunk_size, self.chunk_overlap)

    def construct_chain(self):
        if self.main_llm is None:
            self.construct_main_llm()
        if self.embeddings_llm is None:
            self.construct_embeddings_llm()
        if self.vector_db is None:
            self.generate_vector_db()

    def query_model(self):
        self.query = get_prediction(self.question, self.main_llm, self.vector_db, self.search_k)
