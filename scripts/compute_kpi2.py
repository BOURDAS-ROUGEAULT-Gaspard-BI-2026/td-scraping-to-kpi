import json

# Second KPI: a different definition.
# Instead of one exact skill, it groups several equivalent skills (any cloud provider)
# under one question: "does this posting require cloud skills at all?"
CLOUD_PROVIDERS = ["aws", "azure", "gcp", "google cloud"]

def load_extracted(path="data/extracted.json"):
    # extracted.json was written without an explicit encoding on Windows (cp1252).
    with open(path, encoding="cp1252") as f:
        return json.load(f)["postings"]

def kpi_cloud(postings):
    n = len(postings)
    matching = [
        p for p in postings
        if any(c in s.lower() for s in p.get("required_skills", []) for c in CLOUD_PROVIDERS)
    ]
    return {
        "kpi_label": "% of postings mentioning any cloud provider (AWS, Azure, GCP)",
        "kpi_value": round(len(matching) / n, 3) if n else 0.0,
        "n_matching": len(matching),
        "n_postings_analyzed": n,
    }

if __name__ == "__main__":
    print(json.dumps(kpi_cloud(load_extracted()), indent=2))
