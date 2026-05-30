export type Newsletter = {
  id: string;
  title: string;
  author: string | null;
  source_url: string | null;
  published_at: string | null;
  tags: string[];
  body: string;
  created_at: string;
  updated_at: string;
};

export type NewsletterPayload = {
  title: string;
  author?: string | null;
  source_url?: string | null;
  published_at?: string | null;
  tags?: string[];
  body: string;
};

type NewsletterListResponse = {
  newsletters: Newsletter[];
};

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export async function getNewsletters(): Promise<Newsletter[]> {
  const response = await fetch(`${API_BASE_URL}/newsletters`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`Failed to load newsletters: ${response.status}`);
  }

  const data = (await response.json()) as NewsletterListResponse;
  return data.newsletters;
}

export async function createNewsletter(payload: NewsletterPayload): Promise<Newsletter> {
  const response = await fetch(`${API_BASE_URL}/newsletters`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`Failed to create newsletter: ${response.status}`);
  }

  return (await response.json()) as Newsletter;
}
