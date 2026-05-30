"use client";

import { FormEvent, useState, useTransition } from "react";
import { useRouter } from "next/navigation";

import { createNewsletter } from "../lib/newsletters-client";

function parseTags(value: string): string[] {
  return value
    .split(",")
    .map((tag) => tag.trim())
    .filter(Boolean);
}

export function NewsletterForm() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);

    const form = event.currentTarget;
    const formData = new FormData(form);

    try {
      await createNewsletter({
        title: String(formData.get("title") ?? ""),
        author: String(formData.get("author") ?? "") || null,
        source_url: String(formData.get("source_url") ?? "") || null,
        published_at: String(formData.get("published_at") ?? "") || null,
        tags: parseTags(String(formData.get("tags") ?? "")),
        body: String(formData.get("body") ?? ""),
      });

      form.reset();
      startTransition(() => router.refresh());
    } catch {
      setError("Could not save this newsletter. Check that the API is running and try again.");
    }
  }

  return (
    <form className="ingestion-form" onSubmit={handleSubmit}>
      <div className="form-grid">
        <label>
          <span>Title</span>
          <input name="title" required maxLength={240} placeholder="The Week in AI" />
        </label>

        <label>
          <span>Author</span>
          <input name="author" maxLength={160} placeholder="Writer or publication" />
        </label>

        <label>
          <span>Source URL</span>
          <input name="source_url" type="url" maxLength={2048} placeholder="https://..." />
        </label>

        <label>
          <span>Published</span>
          <input name="published_at" type="date" />
        </label>
      </div>

      <label>
        <span>Tags</span>
        <input name="tags" placeholder="ai, startups, research" />
      </label>

      <label>
        <span>Body</span>
        <textarea
          name="body"
          required
          rows={12}
          placeholder="Paste the newsletter issue or article text..."
        />
      </label>

      <div className="form-actions">
        <button type="submit" disabled={isPending}>
          {isPending ? "Saving..." : "Save newsletter"}
        </button>
        {error ? <p className="form-error">{error}</p> : null}
      </div>
    </form>
  );
}
