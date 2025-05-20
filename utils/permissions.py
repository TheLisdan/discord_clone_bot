import disnake


def clone_overwrites(source_overwrites, target_guild: disnake.Guild):
    new_overwrites = {}

    role_map = {r.name: r for r in target_guild.roles}

    for target, overwrite in source_overwrites.items():
        if isinstance(target, disnake.Role):
            target_role = role_map.get(target.name)
            if target_role:
                new_overwrites[target_role] = overwrite
    return new_overwrites
