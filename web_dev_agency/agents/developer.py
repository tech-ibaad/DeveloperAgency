from agency_swarm import Agent
from tools import CommandExecutor, FileManager, WebScraper

developer = Agent(
    name="Web Developer",
    description="Develops web applications using Next.js, Tailwind CSS, and ShadCN UI.",
    instructions="./agents/developer_instructions.md",
    tools=[CommandExecutor, FileManager, WebScraper],
)
