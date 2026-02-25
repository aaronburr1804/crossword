import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
 
df = pd.read_csv('data.csv')

df['solve_time_mins'] = df['solve_time_secs'] / 60

plt.figure(figsize=(16, 12))
for day in days:
    plt.plot(df['solve_time_mins'][df['weekday'] == day], label=day)

plt.ylabel('Solve Time (minutes)')
plt.title('Puzzles Solved Over Time')
plt.legend()
plt.show()
plt.savefig('plot.png')