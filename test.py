from logs.auth_token import token
import search_site
#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic searchbot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

ONE, TWO, THREE, FOUR = range(4)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hello {user.mention_html()}. Type your message error:",
        reply_markup=ForceReply(selective=True),
    )


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """search the user message."""
    search_line = update.message.text
    answer = search_site.get_search(search_line)
    await update.message.reply_text(f"Querry is: {update.message.text}")
    for i in range(5):
        await update.message.reply_text(f"Answer#{i}: {answer[i]}")
  
    reply_keyboard = [[answer[0]],
                      [answer[1]],
                      [answer[2]],
                      [answer[3]],
                      [answer[4]]]

    await update.message.reply_text(

        "Hi! My name is Professor Bot. I will hold a conversation with you. "

        "Send /cancel to stop talking to me.\n\n"

        "Are you a boy or a girl?",

        reply_markup=ReplyKeyboardMarkup(

            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Boy or Girl?"

        ),

    )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - search the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()