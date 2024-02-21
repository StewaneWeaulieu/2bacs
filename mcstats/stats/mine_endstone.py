from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_endstone',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:end_stone'])
        ])
    ))
