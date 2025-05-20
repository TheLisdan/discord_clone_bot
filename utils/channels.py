import disnake
from utils.permissions import clone_overwrites


async def clone_channels(source_guild: disnake.Guild, target_guild: disnake.Guild):
    category_map = {}

    print("Cloning channels...")

    for category in source_guild.categories:
        new_category = await target_guild.create_category(
            name=category.name,
            overwrites=clone_overwrites(category.overwrites, target_guild),
            position=category.position,
        )
        category_map[category.id] = new_category

    for channel in source_guild.channels:
        if isinstance(channel, disnake.CategoryChannel):
            continue

        overwrites = clone_overwrites(channel.overwrites, target_guild)
        target_category = category_map.get(channel.category_id)

        if isinstance(channel, disnake.TextChannel):
            await target_guild.create_text_channel(
                name=channel.name,
                category=target_category,
                news=channel.is_news(),
                nsfw=channel.nsfw,
                overwrites=overwrites,
                position=channel.position,
                reason="Cloned from source guild",
                topic=channel.topic,
                slowmode_delay=channel.slowmode_delay,
                default_auto_archive_duration=channel.default_auto_archive_duration,
                default_thread_slowmode_delay=channel.default_thread_slowmode_delay,
            )
        elif isinstance(channel, disnake.VoiceChannel):
            await target_guild.create_voice_channel(
                bitrate=channel.bitrate,
                category=target_category,
                name=channel.name,
                nsfw=channel.nsfw,
                overwrites=overwrites,
                position=channel.position,
                reason="Cloned from source guild",
                rtc_region=channel.rtc_region,
                slowmode_delay=channel.slowmode_delay,
                user_limit=channel.user_limit,
                video_quality_mode=channel.video_quality_mode,
            )
        elif isinstance(channel, disnake.ForumChannel):
            await target_guild.create_forum_channel(
                available_tags=channel.available_tags,
                category=target_category,
                default_auto_archive_duration=channel.default_auto_archive_duration,
                default_layout=channel.default_layout,
                default_reaction=channel.default_reaction,
                default_sort_order=channel.default_sort_order,
                default_thread_slowmode_delay=channel.default_thread_slowmode_delay,
                name=channel.name,
                nsfw=channel.nsfw,
                overwrites=overwrites,
                position=channel.position,
                reason="Cloned from source guild",
                slowmode_delay=channel.slowmode_delay,
                topic=channel.topic,
            )
        elif isinstance(channel, disnake.StageChannel):
            await target_guild.create_stage_channel(
                bitrate=channel.bitrate,
                category=target_category,
                name=channel.name,
                nsfw=channel.nsfw,
                overwrites=overwrites,
                position=channel.position,
                reason="Cloned from source guild",
                rtc_region=channel.rtc_region,
                slowmode_delay=channel.slowmode_delay,
                topic=channel.topic,
                user_limit=channel.user_limit,
                video_quality_mode=channel.video_quality_mode,
            )

    print("Channels cloned")
