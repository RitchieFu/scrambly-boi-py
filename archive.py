# for on_message event 3bld/4bld/5bld
    channel = message.channel
    messageSplit = message.content.lower().split()

    if message.author.id == bot.user.id:
        return

    try:
        scrambleCommands[(messageSplit[0] + ' ' + messageSplit[1])]
    except:
        return

    if len(messageSplit) > 2:
        amt = int(messageSplit[-1])
        if amt > 5: amt = 5
    else:
        amt = 1

    for i in range(amt):
        embed = discord.Embed(title = '', description = scrambleCommands[(messageSplit[0] + ' ' + messageSplit[1])](), color = 0x43a8ff)
        await channel.send(embed = embed)