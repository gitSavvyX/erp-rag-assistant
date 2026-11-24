import os
import pandas as pd
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class ERPRagEngine:
    def __init__(self, data_path="data/erp_data.csv"):
        self.data_path = data_path
        self.vector_store = None
        self.chain = None

    def load_data(self):
        # Load CSV data into a string format
        df = pd.read_csv(self.data_path)
        # Convert rows to text for the RAG context
        texts = [f"Product: {row['Product']}, Category: {row['Category']}, Sales in Oct: {row['Sales_Oct']}, Inventory: {row['Inventory']}, Price: {row['Price']}" for _, row in df.iterrows()]
        return texts

    def initialize_rag(self):
        texts = self.load_data()
        
        # 1. Create Embeddings and Vector Store (FAISS)
        embeddings = OpenAIEmbeddings()
        self.vector_store = FAISS.from_texts(texts, embeddings)
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 2})

        # 2. Define the Prompt Template
        template = """
        You are an AI ERP Assistant. Use the following ERP data to answer the user's question.
        If you don't know the answer based on the data, just say you don't know.
        
        ERP Data:
        {context}
        
        Question: {question}
        """
        prompt = PromptTemplate.from_template(template)

        # 3. Create the RAG Chain
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        
        self.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    def ask(self, question: str):
        if not self.chain:
            self.initialize_rag()
        return self.chain.invoke(question)
