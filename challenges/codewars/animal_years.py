def human_years_cat_years_dog_years(human_years: int) -> list[int]:
    return (
        [human_years, 16 + 4 * human_years, 14 + 5 * human_years]
        if human_years > 1
        else [1, 15, 15]
    )
