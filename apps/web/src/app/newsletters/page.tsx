import Link from "next/link";

import { getNewsletters, type Newsletter } from "../lib/api";
import { NewsletterForm } from "./newsletter-form";

function formatDate(value: string | null): string {
  if (!value) {
    return "No date";
  }

  return new Intl.DateTimeFormat("en", {
    month: "short",
    day: "numeric",
    year: "numeric",
  }).format(new Date(`${value}T00:00:00`));
}

export default async function NewslettersPage() {
  let newsletters: Newsletter[] = [];
  let loadError: string | null = null;

  try {
    newsletters = await getNewsletters();
  } catch {
    loadError = "Could not load newsletters. Check that the API is running.";
  }

  return (
    <main className="page-shell">
      <header className="topbar">
        <div className="brand">
          <strong>Newsletter RAG Curator</strong>
          <span>Newsletter ingestion</span>
        </div>
        <nav className="nav" aria-label="Primary">
          <Link href="/">Home</Link>
          <Link href="/newsletters">Archive</Link>
          <span>Search</span>
          <span>Insights</span>
        </nav>
      </header>

      <section className="workspace">
        <div className="workspace-header">
          <div>
            <span className="eyebrow">Phase 2</span>
            <h1>Build the archive.</h1>
          </div>
          <p className="lede compact">
            Add newsletter issues as source records with metadata and body text. Retrieval and
            embeddings come later.
          </p>
        </div>

        <div className="split-layout">
          <section className="panel" aria-labelledby="add-newsletter">
            <h2 id="add-newsletter">Add newsletter</h2>
            <NewsletterForm />
          </section>

          <section className="panel" aria-labelledby="newsletter-list">
            <div className="section-heading">
              <h2 id="newsletter-list">Archive</h2>
              <span>{newsletters.length} saved</span>
            </div>

            {loadError ? <p className="notice warning">{loadError}</p> : null}

            {!loadError && newsletters.length === 0 ? (
              <p className="notice">No newsletters yet. Add the first source record.</p>
            ) : null}

            <div className="newsletter-list">
              {newsletters.map((newsletter) => (
                <article className="newsletter-item" key={newsletter.id}>
                  <div>
                    <h3>{newsletter.title}</h3>
                    <p>
                      {newsletter.author ?? "Unknown author"} · {formatDate(newsletter.published_at)}
                    </p>
                  </div>

                  {newsletter.tags.length > 0 ? (
                    <div className="tag-list">
                      {newsletter.tags.map((tag) => (
                        <span key={tag}>{tag}</span>
                      ))}
                    </div>
                  ) : null}

                  <p className="excerpt">{newsletter.body}</p>
                </article>
              ))}
            </div>
          </section>
        </div>
      </section>
    </main>
  );
}
