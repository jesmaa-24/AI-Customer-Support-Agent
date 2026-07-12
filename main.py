from agents.research_agent import ResearchAgent

def main():
    print("=" * 50)
    print("      AI Research Agent")
    print("Infosys Springboard Virtual Internship 7.0")
    print("=" * 50)

    agent = ResearchAgent()

    while True:
        query = input("\nEnter your research query (or type 'exit' to quit): ")

        if query.lower() == "exit":
            print("\nThank you for using the AI Research Agent!")
            break

        try:
            response = agent.research(query)
            print("\nResearch Agent Response:")
            print(response)
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()