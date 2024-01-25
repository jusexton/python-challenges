def score_to_tally(score: int) -> str:
    five_count = "e <br>" * (score // 5)
    left_over = ["", "a", "b", "c", "d"][score % 5]
    return f"{five_count}{left_over}"
