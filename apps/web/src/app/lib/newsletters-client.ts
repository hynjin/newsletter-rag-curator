"use client";

import { getBrowserApiBaseUrl, type Newsletter, type NewsletterPayload } from "./newsletters";

export async function createNewsletter(payload: NewsletterPayload): Promise<Newsletter> {
  const apiBaseUrl = getBrowserApiBaseUrl();
  const response = await fetch(`${apiBaseUrl}/newsletters`, {
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
