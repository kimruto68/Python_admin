import time

# Misheveve lines
lines = [
    "Akaulizia mama, umepika mboka gani?",
    'Mama akasema, "Leo nimeunda misheveve"',
    'Kijana akasema, "Situtaka hizi, nilitaka sarati"',
    "Baba bila shaka alifika kumuokoa mama,",
    "Alimuangamiza vipi?",
    "Alianza kwa kutafuna mzee vidole,",
    "Anatafuna mzee vidole ni kama anatafuna omena!",
    "Na kumbe anafanya hesabu ya minus kwa uhai ya mzee ",
    "na muzee huyu ni mkasa!"
]

# Adjusted intervals to match the 24 secs tiktok video duration
intervals = [3, 3, 4, 3, 1, 3, 3, 2, 1,1]  #I adjusted the time intervals manually

# Function to print lines with timed intervals
def print_with_intervals(lines, intervals):
    for i, line in enumerate(lines):
        print(line, flush=True)  
        if i < len(intervals): 
            time.sleep(intervals[i])

# Initialize and run the function
print_with_intervals(lines, intervals)
