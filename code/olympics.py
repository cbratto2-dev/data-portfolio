"""Selected calculations. Pass the course dataset as a DataFrame."""
def summarize(athletes):
    latest_games = athletes.groupby("Season")["Games"].transform("max")
    latest = athletes.loc[athletes["Games"].eq(latest_games)]
    measurements = latest.groupby(["Season", "Games"])[["Height", "Weight"]].mean()
    country_rows = athletes["Country"].value_counts().head(10)
    return measurements, country_rows
