from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre_total_plays = defaultdict(int)
    genre_tracks = defaultdict(list)

    for i, (genre, play_count) in enumerate(zip(genres, plays)):
        genre_total_plays[genre] += play_count
        genre_tracks[genre].append((i, play_count))

    ranked_genres = sorted(genre_total_plays, key=lambda x: genre_total_plays[x], reverse=True)

    for genre in ranked_genres:
        ranked_tracks = sorted(genre_tracks[genre], key=lambda x: (-x[1], x[0]))

        for i, _ in ranked_tracks[:2]:
            answer.append(i)

    return answer


test_genres = ["classic", "pop", "classic", "classic", "pop"]
test_plays = [500, 600, 150, 800, 2500]

print(solution(test_genres, test_plays))  # [4, 1, 3, 0]
