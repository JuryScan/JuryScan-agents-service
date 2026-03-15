# Agents crew definition for JuryScan system
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class JuryScanAgentsCrew():
    """Crew for managing AI agents in the JuryScan system"""
    
    agents: List[BaseAgent]
    tasks: List[Task]

    # @agent

    # @task

    # @crew