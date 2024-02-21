from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_netherrack',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:netherrack'])
        ])
    ))
