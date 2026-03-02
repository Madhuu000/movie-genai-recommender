import random

def generate_explanation(movie, recommendations):

    templates = [
        f"If you enjoyed '{movie}', these movies share similar themes, storytelling style, or audience appeal.",
        
        f"People who liked '{movie}' often enjoy these recommendations because they have related genres and entertainment value.",
        
        f"These movies are recommended since they match the viewing patterns of users who loved '{movie}'.",
        
        f"Based on movie similarities and viewer preferences, these films are a great follow-up after watching '{movie}'."
    ]

    explanation = random.choice(templates)

    movie_list = "\n".join([f"- {m}" for m in recommendations])

    return explanation + "\n\nRecommended because:\n" + movie_list