from discord_logger import DiscordLogger

options = {
    "application_name":"1997",
    "service_name": "1997",
    "service_icon_url": "https://media.discordapp.net/attachments/856846018666430484/895441634039312384/image0-15.png?width=491&height=480",
    "service_environment": "1997",
    "display_hostname": True,
    "default_level": "info",
}

logger = DiscordLogger(webhook_url="https://discord.com/api/webhooks/905274813822668884/aPQssy2eYwac77RIvPa3-_crA_wX5UoV7TA3_3x9ssAGteropOoVG34fUq47Bwek4B4N", **options)
logger.construct(title="1997", description="`1997")

response = logger.send()