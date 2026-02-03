import logging
from dotenv import load_dotenv
from argparse import ArgumentParser
from agents.nia import NiaAgent
from agents.savon import SavonAgent
from agents.kano import KanoAgent
from layers.planning import PlanningLayer
from layers.memory import MemoryLayer
from layers.tooling import ToolingLayer
from layers.execution import ExecutionLayer
from layers.self_improvement import SelfImprovementLayer
from observability.monitoring import MonitoringLayer

load_dotenv()

logger = logging.getLogger("NiaLeSane")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

def main(invocation: str):
    logger.info(f"Enhanced brain initialized | Invocation: {invocation}")

    memory = MemoryLayer()
    tooling = ToolingLayer()
    monitoring = MonitoringLayer()

    planning = PlanningLayer()
    plan = planning.decompose(invocation)
    logger.info(f"Plan generated: {plan}")

    nia = NiaAgent()
    savon = SavonAgent()
    kano = KanoAgent()

    governed_plan = nia.govern(plan)
    secured_plan = kano.secure(governed_plan)
    optimized_plan = savon.optimize(secured_plan) if 'finance' in invocation.lower() else secured_plan

    execution = ExecutionLayer(tooling, memory)
    result = execution.execute(optimized_plan)
    logger.info(f"Execution complete: {result}")

    monitoring.log_metrics(result)  # Track performance

    improvement = SelfImprovementLayer()
    improvement.reflect_and_propose(result)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--invocation", required=True, help="Initial invocation for Nia")
    args = parser.parse_args()
    main(args.invocation)
