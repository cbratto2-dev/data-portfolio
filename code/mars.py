"""Selected calculations. Pass the course dataset as a DataFrame."""
def summarize(weather):
    month_labels = [f"Month {number}" for number in range(1, 13)]
    monthly = weather.groupby("month")[["min_temp", "pressure"]].mean()
    return monthly.reindex(month_labels)
