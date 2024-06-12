from langchain_core.prompts import ChatPromptTemplate



PROMPT = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is DT."),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])