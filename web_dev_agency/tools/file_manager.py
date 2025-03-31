import os
from agency_swarm.tools import BaseTool
from pydantic import Field

class FileManager(BaseTool):
    operation: str = Field(..., description="Operation: 'read', 'write', 'append', 'delete', 'list_dir'")
    filepath: str = Field("", description="Path of the file")
    content: str = Field("", description="Content for write/append")

    def run(self):
        try:
            if self.operation == "read":
                with open(self.filepath, "r") as file:
                    return file.read()
            elif self.operation == "write":
                with open(self.filepath, "w") as file:
                    file.write(self.content)
                return f"File '{self.filepath}' written successfully."
            elif self.operation == "append":
                with open(self.filepath, "a") as file:
                    file.write(self.content)
                return f"Content appended to '{self.filepath}'."
            elif self.operation == "delete":
                os.remove(self.filepath)
                return f"File '{self.filepath}' deleted successfully."
            elif self.operation == "list_dir":
                files = os.listdir(self.filepath or ".")
                return f"Files in '{self.filepath or '.'}': {', '.join(files)}"
            else:
                return "Invalid operation."
        except Exception as e:
            return f"Error: {str(e)}"
