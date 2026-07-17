from langgraph.graph import StateGraph, START, END
from src.LanggraphAgenticAI.state.state import State
from src.LanggraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.LanggraphAgenticAI.tools.search_tool import get_tools, create_node_tool
from langgraph.prebuilt import tools_condition, ToolNode
from src.LanggraphAgenticAI.nodes.chatbotwithtools import ChatbotwithToolNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools(self):
        tools = get_tools()
        tool_node = create_node_tool(tools)
        llm = self.llm
        obj_node = ChatbotwithToolNode(llm)
        chatbot_node = obj_node.create_chatbot(tools)
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def setup_graph(self, usecase: str):
        """Sets up the graph for the selected use case."""
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot With Web Search":
            self.chatbot_with_tools()

        return self.graph_builder.compile()