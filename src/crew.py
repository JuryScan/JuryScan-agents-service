# Agents crew definition for JuryScan system
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, llm
from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

from .core import Settings
from .tools import tool_extract_text_from_pdf

api_settings = Settings() # type: ignore

@CrewBase
class JuryScanAgentsCrew():
    """JuryScan Agents Crew"""
    
    agents: List[BaseAgent]
    tasks: List[Task]

    @llm
    def gemini_llm(self) -> LLM:
        """Configuração do modelo de linguagem Gemini para os agentes do JuryScan"""
        return LLM(
            model=api_settings.llm_model,
            api_key=api_settings.google_api_key
        )

    # Definição de agentes ===============
    @agent
    def especialista_extracao(self) -> Agent:
        """Agente especializado em extração de dados estruturados do CNIS"""
        return Agent(
            config=self.agents_config['especialista_extracao'],  # type: ignore[index]
            tools=[tool_extract_text_from_pdf]
        )
    
    @agent
    def auditor_identidade(self) -> Agent:
        """Agente responsável por validar dados de identidade e conformidade"""
        return Agent(
            config=self.agents_config['auditor_identidade'],  # type: ignore[index]
            tools=[]
        )
    
    @agent
    def auditor_previdenciario(self) -> Agent:
        """Agente encarregado de auditar o histórico previdenciário em busca de inconsistências"""
        return Agent(
            config=self.agents_config['auditor_previdenciario'],  # type: ignore[index]
            tools=[]
        )
    
    @agent
    def gerador_relatorio(self) -> Agent:
        """Agente dedicado à geração do relatório final abrangente"""
        return Agent(
            config=self.agents_config['gerador_relatorio'],  # type: ignore[index]
            verbose=True
        )
    
    # Definição de tasks ===============
    @task
    def tarefa_extracao(self) -> Task:
        """Extract structured data from CNIS document"""
        return Task(
            config=self.tasks_config['tarefa_extracao'],  # type: ignore[index]
        )
    
    @task
    def tarefa_validacao_identidade(self) -> Task:
        """Validate identity and compliance data"""
        return Task(
            config=self.tasks_config['tarefa_validacao_identidade'],  # type: ignore[index]
        )
    
    @task
    def tarefa_auditoria_erros(self) -> Task:
        """Audit social security history for inconsistencies"""
        return Task(
            config=self.tasks_config['tarefa_auditoria_erros'],  # type: ignore[index]
        )
    
    @task
    def tarefa_geracao_relatorio(self) -> Task:
        """Generate final comprehensive report"""
        return Task(
            config=self.tasks_config['tarefa_geracao_relatorio'],  # type: ignore[index]
        )

    # Definição Crew ============
    @crew
    def crew(self) -> Crew:
        """Creates the JuryScan Agents Crew with defined agents and tasks"""
        return Crew(
            # Criado automaticamente a partir dos métodos decorados com @agent
            agents=self.agents,
            # Criado automaticamente a partir dos métodos decorados com @task
            tasks=self.tasks,
            # As tarefas serão executadas em sequência
            process=Process.sequential,
            verbose=True
        )