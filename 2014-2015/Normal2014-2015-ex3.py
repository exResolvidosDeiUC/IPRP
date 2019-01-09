def melhor_filme(filmes, novas):
    filmes.setdefault(novas[0], [])
    for classific in novas[1:]:
        filmes[novas[0]].append(classific)
    medias = {}
    for filme, classifics in filmes.items():
        medias.setdefault(filme, sum(classifics) / len(classifics)) if len(classifics) > 3 else None
    max_media = max(medias.values())
    for filme, media in medias.items():
        if media == max_media:
            return filme, media
