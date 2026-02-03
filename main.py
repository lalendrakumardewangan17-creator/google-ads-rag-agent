from agent.data_loader import load_campaign_data
from agent.kpi_analyzer import compute_kpis
from agent.issue_detector import detect_issues
from agent.decision_engine import build_rag_query
from agent.rag_retriever import retrieve_context
from agent.llm_recommender import generate_recommendation

df = load_campaign_data("data/campaigns.csv")
df = compute_kpis(df)

for _, row in df.iterrows():
    issues = detect_issues(row)

    if not issues:
        continue

    query = build_rag_query(issues)
    context = retrieve_context(query)

    recommendation = generate_recommendation(
        metrics=row.to_dict(),
        context=context
    )

    print("=" * 80)
    print(f"📊 Campaign: {row['campaign']}")
    print("⚠️ Issues:", issues)
    print("💡 Recommendations:\n", recommendation)
