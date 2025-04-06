import os
from researchCrew.crew import ResearchCrew

os.mkdir('output', exist_ok = True)


def run():
    """This is a crew runner for crewai multi agent collaborations"""
    inputs = {
        'topic': "Ai in healthcare." }
    results = ResearchCrew().crew().kickoff(inputs= inputs)

    print(results.raw)

if __name__ == "main":
    run()