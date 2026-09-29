"""JanSetu's two focused ADK agents.

Run locally with: adk web agents
The policy agent is the only agent allowed to use Google Search grounding.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search


integrity_agent = Agent(
    name="civic_integrity_agent",
    model="gemini-2.0-flash-001",
    description="Checks whether a citizen report is specific, plausible, and a likely duplicate.",
    instruction="""
You are JanSetu's civic integrity agent for India. Review one complaint at a time.
Return strict JSON with: genuine (boolean), confidence (0-100), category, priority (0-100),
duplicateSignals (array), reason, and needsHumanReview (boolean).
Require a concrete public problem, an identifiable place, and an observable impact.
Never reject a report only because it is multilingual, emotional, short, or informal.
Mark needsHumanReview true for low confidence, safety threats, allegations about a person,
or suspected manipulation. Do not call the web search tool for routine verification.
""",
)


policy_agent = Agent(
    name="area_policy_agent",
    model="gemini-2.0-flash-001",
    description="Finds local complaint patterns and turns them into evidence-backed civic priorities.",
    instruction="""
You are JanSetu's area intelligence agent for India. Analyse the supplied nearby complaints.
Return strict JSON with: headline, topCategory, rankedIssues, recommendedAction,
evidenceNotes, confidence, and sources.
Use the Google Search tool only when the user explicitly asks for current policy, scheme,
department, infrastructure, or public data context. When searching, prefer official Indian
government sources, cite the URLs in sources, and clearly separate web evidence from citizen data.
Do not invent counts, places, or government commitments.
""",
    tools=[google_search],
)


# The two agents are intentionally independent so the inexpensive integrity check never
# triggers a web search. The host API can route requests to either agent by name.
root_agent = policy_agent
