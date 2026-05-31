import { getApiBaseUrl, type Newsletter, type NewsletterListResponse } from "./newsletters";

export async function getNewsletters(): Promise<Newsletter[]> {
  const apiBaseUrl = getApiBaseUrl();
  const response = await fetch(`${apiBaseUrl}/newsletters`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`Failed to load newsletters: ${response.status} ${response.statusText}`);
  }

  const data = (await response.json()) as NewsletterListResponse;
  return data.newsletters;
}
