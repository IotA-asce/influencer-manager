# Requirements

## Functional requirements
- Generate images from prompts using Gemini Nano Banana Pro.
- Store generated images so they are available for later publishing.
- Publish images to Instagram using the media container then publish workflow.
- Schedule posts and safely retry failures without duplicating publishes.
- Keep audit logs that capture prompt details, assets, and publish results.

## Non-functional requirements
- Idempotency: rerunning a job must not double-publish or create duplicate containers unnecessarily.
- Observability: structured logging with job states to trace executions.
- Security: secrets must not be committed to the repository; use environment-based configuration.

## External constraints
- Instagram publishing relies on creating media containers followed by a publish step.
- Media must be hosted at a publicly accessible URL at publish time.
- JPEG is the required image format.
- Instagram imposes a rate limit on API-published posts within a 24-hour window.
- The system must poll the container status_code and ensure readiness before publishing.
