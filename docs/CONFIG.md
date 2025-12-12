# Configuration

Influencer Manager reads its configuration from environment variables. Local development can use a `.env` file for convenience, while CI environments should source values from GitHub Actions secrets mapped explicitly into workflow `env` blocks.

## Environment variables

| Variable | Required | Default / Example | Notes |
| --- | --- | --- | --- |
| `IM_ENV` | No | `local` | Deployment environment name. |
| `IM_LOG_LEVEL` | No | `INFO` | Logging verbosity. |
| `GEMINI_API_KEY` | For generation | _n/a_ | Preferred Gemini API key variable. `GOOGLE_API_KEY` is also supported. |
| `GOOGLE_API_KEY` | For generation | _n/a_ | Alias used when `GEMINI_API_KEY` is not set. |
| `IM_GEMINI_MODEL` | No | `gemini-3-pro-image-preview` | Gemini model id (e.g., `gemini-2.5-flash-image`). |
| `IM_IG_ACCESS_TOKEN` | For publishing | _n/a_ | Instagram Graph API access token (JPEG-only publishing limitations apply). |
| `IM_IG_USER_ID` | For publishing | _n/a_ | Instagram user id associated with the access token. |
| `IM_GRAPH_API_BASE_URL` | No | `https://graph.facebook.com` | Graph API base URL. |
| `IM_GRAPH_API_VERSION` | No | `v21.0` | Graph API version. |
| `IM_META_APP_ID` | Not used yet | _n/a_ | Placeholder for future OAuth integration. |
| `IM_META_APP_SECRET` | Not used yet | _n/a_ | Placeholder for future OAuth integration. |

## CI setup

To enable authenticated runs in GitHub Actions, add the following repository secrets:

- `GEMINI_API_KEY`
- `IM_IG_ACCESS_TOKEN`
- `IM_IG_USER_ID`

Workflows only access these secrets when they are explicitly mapped into the job or step `env` configuration.
