#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

from logs.auth_token import token
import logging
import search_site

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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

VARIANT_ROUTES, VARIANTS, TYPING = map(chr, range(6, 9))
# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
ONE, TWO, THREE, FOUR, FIVE = range(5)
# Querry data
# WATERS, AGILENT, THERMO, SHIMADZU = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Waters", callback_data=str(ONE)),
            InlineKeyboardButton("Agilent", callback_data=str(TWO)),
            InlineKeyboardButton("Thermo", callback_data=str(THREE)),
            InlineKeyboardButton("Shimadzu", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text("Choose a vendor", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Waters", callback_data=str(ONE)),
            InlineKeyboardButton("Agilent", callback_data=str(TWO)),
            InlineKeyboardButton("Thermo", callback_data=str(THREE)),
            InlineKeyboardButton("Shimadzu", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    await query.edit_message_text(text="Choose a vendor", reply_markup=reply_markup)
    return START_ROUTES


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Enter Waters error message:", callback_data=str(TWO)),
            InlineKeyboardButton("Back to vendor choose", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Using Waters support database", reply_markup=reply_markup
    )
    return END_ROUTES


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Enter Agilent error message:", callback_data=str(TWO)),
            InlineKeyboardButton("Back to vendor choose", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Using Agilent support database", reply_markup=reply_markup
    )
    return END_ROUTES


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons."""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Enter Thermo error message:", callback_data=str(TWO)),
            InlineKeyboardButton("Back to vendor choose", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Using Thermo support database", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return END_ROUTES


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Enter Shimadzu error message:", callback_data=str(TWO)),
            InlineKeyboardButton("Back to vendor choose", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Using Shimadzu support database", reply_markup=reply_markup
    )
    return END_ROUTES


async def user_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:

    """Prompt user to input error message"""

    text = "Please type error message:"
    await update.callback_query.edit_message_text(text=text)

    await update.callback_query.answer()

    return TYPING


# async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

#     """Save input for search"""


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("[1]", callback_data=str(ONE)),
            InlineKeyboardButton("[2]", callback_data=str(TWO)),
            InlineKeyboardButton("[3]", callback_data=str(THREE)),
            InlineKeyboardButton("[4]", callback_data=str(FOUR)),
            InlineKeyboardButton("[5]", callback_data=str(FIVE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="That what I found:", reply_markup=reply_markup
    )
    # error_text = update.message.text
    # error = search_site.get_search(error_text)

    # return VARIANTS
    return VARIANT_ROUTES


async def ans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    """Save input for search"""
    if "1" in update.message.text:
        print(search.error[0])
    error_text = update.message.text
    logger.info(error_text)

    await update.message.reply_text("That what I found:")
    return ConversationHandler.END


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
            ],

            TYPING: [MessageHandler(filters.TEXT & ~filters.COMMAND, search)],

            # VARIANTS: [CallbackQueryHandler(results)],

            VARIANT_ROUTES: [
                [MessageHandler(filters.TEXT & ~filters.COMMAND, ans)],
                [MessageHandler(filters.TEXT & ~filters.COMMAND, ans)],
                [MessageHandler(filters.TEXT & ~filters.COMMAND, ans)],
                [MessageHandler(filters.TEXT & ~filters.COMMAND, ans)],
                [MessageHandler(filters.TEXT & ~filters.COMMAND, ans)],
            ],

            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(user_input, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(THREE) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()