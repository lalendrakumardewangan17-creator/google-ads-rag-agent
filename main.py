from agent.decision_engine import build_rag_query
from agent.rag_retriever import retrieve_context

issues = ["Low CTR", "High CPA"]
query = build_rag_query(issues)

context = retrieve_context(query)

print("📄 Retrieved Context:\n", context)
