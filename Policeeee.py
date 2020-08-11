from .. import loader, utils
import logging
from asyncio import sleep
logger = logging.getLogger(__name__)
def register(cb):
    cb(PoliceMod())
@loader.tds
class PoliceMod(loader.Module):
	strings = {"name": "Police"}
	@loader.owner
	async def policecmd(self, message):
		light = ("ðŸ”´"*3)+("âšª"*3)+("ðŸ”µ"*3)
		for i in range(30):
			await message.edit("\n".join([[light, light[::-1]][i%2]]*3))
			await sleep(0.7)
