import gpt2_bot.irc, gpt2_bot.commands, gpt2_bot.gpt2, gpt2_bot.config

def assemble_bot(config_path):
    config = gpt2_bot.config.config(config_path)

    ircbot = gpt2_bot.irc.IRCBot(config_path)

    ircbot.register_command("ping", gpt2_bot.commands.ping_command)
    ircbot.register_command("ignore", gpt2_bot.commands.ignore_command)
    ircbot.register_command("unignore", gpt2_bot.commands.unignore_command)
    ircbot.register_command("temp", gpt2_bot.commands.temp_command)
    ircbot.register_command("shitposting", gpt2_bot.commands.shitposting_command)

    gpt2_bot.gpt2.init(ircbot)

    return ircbot
