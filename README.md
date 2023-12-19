# Aiogram Calculator Bot

This is a simple calculator bot built using the Aiogram library. The bot can evaluate mathematical expressions and handle trigonometric functions.

## Getting Started

### Prerequisites

- Python 3.x
- Aiogram library

### Installation

```bash
pip install aiogram
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/wahnkoij/calculating_bot
cd calculating_bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your bot token:

Replace `YOUR_BOT_TOKEN` with your actual bot token in the following line:

```python
bot = Bot(token="YOUR_BOT_TOKEN")
```

4. Run the bot:

```bash
python your_bot_file.py
```

## Features

- Basic arithmetic operations: +, -, *, /, %, **, ^, :
- Trigonometric functions: sin, cos, tan
- Natural logarithm: log

## Commands

- `/start`: Start the bot and display the welcome message.
- `/help`: Display a help message with available commands and usage instructions.
- `/solve expression`: Initiate solving a mathematical expression.

## Example Usage

1. Start the bot.
2. Type a mathematical expression or trigonometric function.

Example:
```plaintext
sin(30.0)
```

Remember to replace placeholders like `yourusername`, `aiogram-calculator-bot`, `your_bot_file.py`, and `YOUR_BOT_TOKEN` with your actual information.
