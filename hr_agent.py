import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()  # load OPENAI_API_KEY etc. from .env

async def main() -> None:
    # Reads the API key from the OPENAI_API_KEY environment variable.
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

    agent = AssistantAgent(
        name="hr_assistant",
        model_client=model_client,
        system_message="You are an experienced HR recruiter. "
        "Your responsibility is to generate "
        "professional job descriptions.",
    )

    try:
        # Console streams the agent's messages to the terminal.
        await Console(
            agent.run_stream(
                task="Write a job description for a Junior Python Developer with Roles and Responsibilities in exactly 5 numbered lines."
            )
        )
    finally:
        # Always close the client, otherwise the script can hang.
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())