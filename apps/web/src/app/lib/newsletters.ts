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

const DEFAULT_API_BASE_URL = "http://127.0.0.1:8000";
const DEFAULT_BROWSER_API_BASE_URL = "/api/backend";

export function getApiBaseUrl(): string {
  return process.env.API_BASE_URL ?? process.env.NEXT_PUBLIC_API_BASE_URL ?? DEFAULT_API_BASE_URL;
}

export function getBrowserApiBaseUrl(): string {
  return process.env.NEXT_PUBLIC_BROWSER_API_BASE_URL ?? DEFAULT_BROWSER_API_BASE_URL;
}
