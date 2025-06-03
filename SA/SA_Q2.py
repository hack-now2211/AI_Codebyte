def user_stats(data):
    return {
        user: {
            'avg': round(sum(scores) / len(scores), 2),
            'min': min(scores),
            'max': max(scores)
        } for user, scores in data.items()
    }

scores = {
    "user_1": [80, 90, 85],
    "user_2": [60, 65, 70],
    "user_3": [78, 82, 79],
    "user_4": [92, 88, 94],
    "user_5": [70, 75, 80],
    "user_6": [88, 85, 85],
    "user_7": [95, 98, 92],
    "user_8": [65, 70, 68],
    "user_9": [80, 85, 83],
    "user_10": [75, 78, 74]
}
print(user_stats(scores))