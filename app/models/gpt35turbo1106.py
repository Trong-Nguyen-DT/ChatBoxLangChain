
from app.config import OPEN_AI_API_KEY

from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor

from app.services.tools import get_current_weather, retrieval_data
from app.models.model_configs.prompts import PROMPT



class ConversationAzureChatGPT35TURBO16K():
    def __init__(self):
        super().__init__()
        self.OPEN_AI_API_KEY = OPEN_AI_API_KEY
        self.llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
        self.tools = [retrieval_data(), get_current_weather]
        self.prompt = PROMPT
        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    
    def run(self, question):
        return self.agent_executor.invoke({"input" : question})