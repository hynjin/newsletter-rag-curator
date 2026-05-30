import { API_BASE_URL, type Newsletter, type NewsletterListResponse } from "./newsletters";

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
