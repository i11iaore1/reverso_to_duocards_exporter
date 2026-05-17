# Reverso to DuoCards Exporter

This project allows you to automatically export favorite words from Reverso and import them into a specified DuoCards deck.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (for dependency management)

## Setup

1. **Install dependencies:**
   Make sure you have `uv` installed. Then, install the project dependencies:
   ```bash
   uv sync
   ```

2. **Environment Variables:**
   Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Open the `.env` file and fill in the required values. You will need to obtain these values from your browser's developer tools (Network tab) while logged into Reverso and DuoCards.

   * `REVERSO_REFRESH`: Your Reverso refresh token.
   * `DUOCARDS_TOKEN`: Your DuoCards authorization token.
   * `DUOCARDS_DECK_ID`: The ID of the DuoCards deck where you want to add the cards.

## Usage

To move favorites from Reverso to DuoCards, use the following command:

```bash
uv run python main.py
```

By default, this moves 10 cards. You can specify a different amount using the `--amount` option:

```bash
uv run python main.py --amount 20
```

*Note: After cards are successfully added to DuoCards, they will be deleted from your Reverso favorites.*
