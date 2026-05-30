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

export type NewsletterListResponse = {
  newsletters: Newsletter[];
};

export const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
