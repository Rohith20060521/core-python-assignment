def calculate_positive_feedback_percentage(ratings_list):
    if not ratings_list:
        return 0.0
    total_ratings = len(ratings_list)
    positive_count = 0
    for rating in ratings_list:
        if rating >= 4:
            positive_count += 1
    percentage = (positive_count / total_ratings) * 100
    return round(percentage, 1)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
result_percentage = calculate_positive_feedback_percentage(ratings)
print(f"Positive Feedback: {result_percentage}%")