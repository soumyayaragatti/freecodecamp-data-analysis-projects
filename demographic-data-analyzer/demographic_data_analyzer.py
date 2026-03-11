import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv("adult.data.csv")
    # Remove spaces from strings (so filtering works)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Race count
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # Percentage with Bachelors
    percentage_bachelors = round(
        (df[df["education"] == "Bachelors"].shape[0] / len(df)) * 100, 1
    )

    # Advanced education
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Percentage rich with advanced education
    higher_education_rich = round(
        (higher_education[higher_education["salary"] == ">50K"].shape[0] /
         len(higher_education)) * 100, 1
    )

    # Percentage rich without advanced education
    lower_education_rich = round(
        (lower_education[lower_education["salary"] == ">50K"].shape[0] /
         len(lower_education)) * 100, 1
    )

    # Minimum work hours
    min_work_hours = df["hours-per-week"].min()

    # Rich among minimum workers
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(
        (num_min_workers[num_min_workers["salary"] == ">50K"].shape[0] /
         len(num_min_workers)) * 100, 1
    )

    # Country with highest percentage of rich
    country_rich = (
        df[df["salary"] == ">50K"]["native-country"].value_counts() /
        df["native-country"].value_counts() * 100
    )

    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = round(country_rich.max(), 1)

    # Top occupation in India earning >50K
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        ["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top India occupation:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }