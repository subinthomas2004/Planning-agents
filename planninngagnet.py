
from crewai import Agent, Task, Crew, LLM

# Initialize the local LLM
llm = LLM(
    model="ollama/qwen2.5:3b",
    base_url="http://localhost:11434",
    temperature=0
)

# Create the planning agent
planner = Agent(
    role="Planning Agent",
    goal="Break goals into clear, achievable steps",
    backstory=(
        "You are an expert learning planner who creates "
        "simple, practical, and achievable learning plans."
    ),
    llm=llm,
    verbose=True
)

# Create the planning task
planning_task = Task(
    description=(
        "Create a 7-day plan to learn Python programming. "
        "Give one practical learning task for each day."
    ),
    expected_output=(
        "A clear, numbered 7-day Python learning plan "
        "with one practical task for each day."
    ),
    agent=planner
)

# Create the crew
crew = Crew(
    agents=[planner],
    tasks=[planning_task],
    verbose=True
)

# Execute the task
result = crew.kickoff()

# Print the output
print("\n--- Planning Agent Output ---\n")
print(result)
