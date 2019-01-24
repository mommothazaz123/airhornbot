import os

from discord.ext.commands import Bot


class VoiceState:
    def __init__(self):
        self.vc = None


bot = Bot('.')
vc = VoiceState()

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))


@bot.command(pass_context=True)
async def airhorn(ctx):
    summoned_channel = ctx.message.author.voice_channel
    if summoned_channel is None:
        return await bot.say('You are not in a voice channel.')

    if not vc.vc:
        vc.vc = await bot.join_voice_channel(summoned_channel)
    else:
        await vc.vc.move_to(summoned_channel)

    player = vc.vc.create_ffmpeg_player('airhorn.mp3')
    player.start()


bot.run(os.environ.get("TOKEN"))
