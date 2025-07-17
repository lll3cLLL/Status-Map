# Status Map

This repository contains assets and API definitions for integrating **NovaTalks** chat and ticket data with **Intercom**.

## Project Goals

The main objective of this project is to synchronize conversations and support tickets from NovaTalks into Intercom. This allows teams that rely on Intercom for customer interactions to view and manage NovaTalks messages directly within Intercom.

## Intercom API Specification

The file [`api.intercom.io.json`](api.intercom.io.json) located at the repository root is the OpenAPI definition for the Intercom API. It can be used to generate client libraries or to understand the available endpoints when building the integration.

## Setup

Future scripts that perform the synchronization should use the following environment variables:

- `INTERCOM_ACCESS_TOKEN` – personal access token for the Intercom API
- `NOVATALKS_API_KEY` – API key or token for accessing NovaTalks

To run these scripts, install the required dependencies in a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Additional dependencies or setup steps may be documented alongside the scripts once they are added.

