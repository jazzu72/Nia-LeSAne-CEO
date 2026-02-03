from pinecone import Pinecone

class MemoryLayer:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        self.index = self.pc.Index('nia-memory')

    def store(self, vector, metadata):
        self.index.upsert([(str(uuid.uuid4()), vector, metadata)])

    def query(self, query_vector):
        return self.index.query(vector=query_vector, top_k=5, include_metadata=True)

    def prune(self):
        # Self-pruning stub (e.g., delete old entries)
        logger.info("Memory pruned")
