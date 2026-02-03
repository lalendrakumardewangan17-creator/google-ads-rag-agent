def build_rag_query(issues: list[str]) -> str:
    """
    Convert detected issues into a semantic search query
    """

    if not issues:
        return "Google Ads campaign optimization best practices"

    issue_text = ", ".join(issues)

    query = (
        f"Google Ads optimization strategies for "
        f"{issue_text.lower()} in search and display campaigns"
    )

    return query
