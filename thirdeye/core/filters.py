def apply_filters(results, orgs_to_ignore=None, products_to_include=None, ports_to_include=None):
    filtered = []

    for result in results.get("matches", []):
        org = result.get("org", "").lower()
        product = result.get("product", "").lower()
        port = result.get("port", 0)

        if orgs_to_ignore:
            if any(blocked.lower() in org for blocked in orgs_to_ignore):
                continue  # Skip this one

        if products_to_include:
            if not any(p.lower() in product for p in products_to_include):
                continue  # Skip

        if ports_to_include:
            if port not in ports_to_include:
                continue  # Skip

        filtered.append(result)

    return {"matches": filtered}
