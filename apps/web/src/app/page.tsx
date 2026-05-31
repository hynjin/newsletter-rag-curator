import Link from "next/link";

type HealthResponse = {
  status: string;
  service: string;
};

type HealthState =
  | { ok: true; data: HealthResponse }
  | { ok: false; message: string };

async function getHealth(): Promise<HealthState> {
  const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

  try {
    const response = await fetch(`${apiBaseUrl}/health`, {
      cache: "no-store",
    });

    if (!response.ok) {
      return {
        ok: false,
        message: `API returned ${response.status}`,
      };
    }

    return {
      ok: true,
      data: (await response.json()) as HealthResponse,
    };
  } catch {
    return {
      ok: false,
      message: "API is not reachable",
    };
  }
}

export default async function Home() {
  const health = await getHealth();

  return (
    <main className="page-shell">
      <header className="topbar">
        <div className="brand">
          <strong>Newsletter RAG Curator</strong>
          <span>Phase 1 foundation</span>
        </div>
        <nav className="nav" aria-label="Primary">
          <Link href="/">Home</Link>
          <Link href="/newsletters">Archive</Link>
          <span>Search</span>
          <span>Insights</span>
        </nav>
      </header>

      <section className="hero">
        <div className="hero-copy">
          <span className="eyebrow">Full-stack RAG workspace</span>
          <h1>Curate newsletter knowledge with grounded retrieval.</h1>
          <p className="lede">
            A focused workspace for turning newsletter archives into searchable, source-backed
            research notes.
          </p>
        </div>

        <aside className="status-panel" aria-label="Backend health status">
          <div className="status-row">
            <div>
              <p className="status-label">Backend</p>
              <p className="status-value">{health.ok ? health.data.service : "Unavailable"}</p>
            </div>
            <span className={`status-pill ${health.ok ? "ok" : "error"}`}>
              {health.ok ? "Healthy" : "Offline"}
            </span>
          </div>
          <p className="status-detail">
            {health.ok
              ? `Health endpoint responded with status "${health.data.status}".`
              : `${health.message}. Start the FastAPI service and refresh this page.`}
          </p>
        </aside>
      </section>

      <section className="milestones" aria-label="Workspace areas">
        <div className="milestone">
          <strong>Archive</strong>
          <Link href="/newsletters">Newsletter records and source metadata.</Link>
        </div>
        <div className="milestone">
          <strong>Search</strong>
          Source passages ranked for research.
        </div>
        <div className="milestone">
          <strong>Insights</strong>
          Saved answers, summaries, and notes.
        </div>
      </section>
    </main>
  );
}
