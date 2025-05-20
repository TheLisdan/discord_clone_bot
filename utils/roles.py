import disnake


async def clone_roles(source_guild: disnake.Guild, target_guild: disnake.Guild):
    existing_roles = {r.name: r for r in target_guild.roles}

    print("Cloning roles...")

    for role in reversed(source_guild.roles):
        if role.name == "@everyone":
            continue

        if role.name in existing_roles:
            continue

        await target_guild.create_role(
            name=role.name,
            permissions=role.permissions,
            colour=role.colour,
            hoist=role.hoist,
            mentionable=role.mentionable,
            emoji=role.emoji,
            icon=role.icon,
            reason="Cloned from source guild",
        )

    print("Roles cloned")
