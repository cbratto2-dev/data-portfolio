"""Calculation from the ASOS course exercise."""
weekly_revenue = [65, 77, "66", "74", 64, 82, "86", 72, "80", 96, 101, "35", "72", "68"]
cleaned = [int(value) for value in weekly_revenue]
for month, values in (("June", cleaned[:4]), ("July", cleaned[4:9]), ("August", cleaned[9:])):
    print(month, sum(values), sum(values) / len(values))
