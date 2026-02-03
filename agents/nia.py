import os

class NiaAgent:
    def govern(self, plan):
        if os.getenv('NIA_SPECIAL_PASSWORD') != 'AddieMaeLeSane33':
            raise ValueError("Governance failure: Invalid special password")
        # ReAct pattern: Reason, Act, Observe
        # Reason
        reasoning = "Governance: Aligning with purpose and safety"
        # Act
        governed = f"{plan} (governed with safety checks)"
        # Observe
        logger.info(reasoning)
        return governed
