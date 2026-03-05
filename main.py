from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_aws import ChatBedrockConverse
from langchain_aws import ChatAnthropicBedrock
from tavily import TavilyClient


tavily = TavilyClient()


@tool
def search(query:str) -> str:
    """
    Tool that seaches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """


    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatAnthropicBedrock(
    model="global.anthropic.claude-sonnet-4-6",
    region_name="us-east-1",
    temperature=0.0
)

tools = [search]

agent = create_agent(model=llm,tools=tools)

def main():


    print("Hello from langchain-course!")

    result=agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})

    print(result)

if __name__ == "__main__":
    main()
