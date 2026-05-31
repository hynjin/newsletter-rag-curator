const DEFAULT_API_BASE_URL = "http://127.0.0.1:8000";

type RouteContext = {
  params: Promise<{
    path: string[];
  }>;
};

function getBackendUrl(path: string[]): URL {
  const apiBaseUrl = process.env.API_BASE_URL ?? process.env.NEXT_PUBLIC_API_BASE_URL ?? DEFAULT_API_BASE_URL;
  const normalizedBaseUrl = apiBaseUrl.endsWith("/") ? apiBaseUrl.slice(0, -1) : apiBaseUrl;
  return new URL(`${normalizedBaseUrl}/${path.join("/")}`);
}

async function proxyRequest(request: Request, context: RouteContext): Promise<Response> {
  const { path } = await context.params;
  const url = getBackendUrl(path);
  const incomingUrl = new URL(request.url);
  url.search = incomingUrl.search;

  try {
    const response = await fetch(url, {
      method: request.method,
      headers: request.headers,
      body: request.method === "GET" || request.method === "HEAD" ? undefined : await request.text(),
      cache: "no-store",
    });

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers,
    });
  } catch (e) {
    // Log the underlying error for local diagnosis and include it in the JSON response.
    // eslint-disable-next-line no-console
    console.error("Proxy error fetching backend URL:", url.toString(), e);

    return Response.json(
      {
        detail: "Backend API is not reachable. Start the FastAPI service and try again.",
        error: String(e),
      },
      { status: 503 },
    );
  }
}

export async function GET(request: Request, context: RouteContext): Promise<Response> {
  return proxyRequest(request, context);
}

export async function POST(request: Request, context: RouteContext): Promise<Response> {
  return proxyRequest(request, context);
}
