from agency_swarm import Agency
from agents import planner, copywriter, designer, developer

agency = Agency([
    planner,  
    [planner, copywriter],  
    [planner, designer],  
    [planner, developer],  
    [designer, developer]  
])

agency.demo_gradio(height=900)
