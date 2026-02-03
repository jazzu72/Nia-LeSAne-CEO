from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # Replace with xAI if available

class PlanningLayer:
    def decompose(self, invocation: str):
        llm = OpenAI(temperature=0.3)
        prompt = PromptTemplate.from_template("Decompose this invocation into steps: {invocation}")
        chain = prompt | llm
        return chain.invoke({"invocation": invocation}).content
