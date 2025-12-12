# 0001 - Architecture Style

- Status: PROPOSED
- Deciders: Team
- Date: 2025-12-12

## Context
We need a structure that cleanly separates business rules (prompts, jobs, scheduling) from integrations (Gemini, storage, Instagram). Testing and iteration speed require clear seams for mocking.

## Decision
Adopt a hexagonal (ports and adapters) architecture with domain models, application use cases, and infrastructure adapters. Interfaces/ports define contracts consumed by the application layer; adapters implement those contracts for specific services (Gemini image generation, asset storage, Instagram publishing, scheduler/clock, logging).

## Consequences
- Positive: Easier testing through port mocks; clearer separation of concerns; adapters can be swapped without changing use cases.
- Negative: Slightly more boilerplate and interface definitions; requires discipline to keep business logic out of adapters.
