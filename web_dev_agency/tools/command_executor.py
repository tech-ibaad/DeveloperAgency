import subprocess
from agency_swarm.tools import BaseTool
from pydantic import Field

class CommandExecutor(BaseTool):
    command: str = Field(..., description="The full command to execute.")

    def run(self):
        try:
            result = subprocess.run(self.command, shell=True, text=True, capture_output=True)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Error executing command: {str(e)}"
