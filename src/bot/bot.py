from aiogram import executor, Dispatcher

from handlers import start_menu, head_part_handler, story_part_handler, essence_part_handler, proofs_part_handler, \
    claims_part_handler, additions_part_handler, download_doc_handler
from init_bot import dp


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    start_menu.register_handlers(dp)
    head_part_handler.register_handlers(dp)
    story_part_handler.register_handlers(dp)
    essence_part_handler.register_handlers(dp)
    proofs_part_handler.register_handlers(dp)
    claims_part_handler.register_handlers(dp)
    additions_part_handler.register_handlers(dp)
    download_doc_handler.register_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
