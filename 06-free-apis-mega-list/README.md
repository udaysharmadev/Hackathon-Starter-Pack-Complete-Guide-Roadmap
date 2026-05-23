# 06. Free APIs Mega List

APIs are how hackathon projects stop being fake.

A good API can turn a basic idea into something that feels real, responsive, and useful.

## How to use this list

Pick APIs by job, not by hype:
- AI needs a model or reasoning service
- maps need geolocation
- notifications need email or SMS
- forms need authentication and storage
- voice needs speech-to-text or text-to-speech
- dashboards need structured data

## API selection rules

- Use the simplest API that solves the core problem.
- Prefer one strong API over three weak ones.
- Do not add APIs just to look advanced.
- Check free tier rules before the hackathon starts.
- Keep a fallback if the API fails.

## Mega list

See [api-database.md](api-database.md) for the table.

## Best categories for hackathons

| Category | Why it matters |
|---|---|
| AI | Fast wow factor and useful workflows |
| Maps | Strong demo clarity and location use cases |
| Weather | Easy integration and good utility |
| Finance | Practical dashboards and tracking |
| OCR | Excellent for document-heavy workflows |
| Voice | Makes demos feel dynamic |
| Email | Easy notification systems |
| Auth | Required for serious products |
| Payments | Useful for business-like products |
| Open data | Strong social and civic use cases |

## Common API mistakes

- Relying on one unstable endpoint
- Forgetting environment variables
- Not testing rate limits
- Hardcoding secrets
- Building a demo that breaks offline
- Ignoring API latency in the user flow

## API stack pattern

```mermaid
flowchart LR
    A[User action] --> B[Frontend]
    B --> C[Backend route]
    C --> D[API call]
    D --> E[Store result]
    E --> F[Render output]
```

## Build pattern

1. Start with one API.
2. Save the output.
3. Show the result immediately.
4. Add one extra layer only if it strengthens the demo.
5. Keep a fallback mode.
