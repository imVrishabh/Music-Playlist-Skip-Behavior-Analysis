# Topic: Music Playlist Skip Behavior Analysis
# Name: Vrishabh Deshmukh
# ERP: 6606287

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("music_playlist.csv")
print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

plt.figure(figsize=(6,4))
sns.countplot(x='skipped', data=df, palette="Set2")
plt.title("Skip vs Non-Skip Songs")
plt.xlabel("Skipped (1 = Yes, 0 = No)")
plt.ylabel("Count")
plt.show()

genre_skip = df.groupby('genre')['skipped'].mean().sort_values()
plt.figure(figsize=(8,5))
genre_skip.plot(kind='bar', color="skyblue")
plt.title("Skip Rate by Genre")
plt.ylabel("Skip Probability")
plt.show()

top_skipped = df[df['skipped']==1]['song'].value_counts().head(10)
plt.figure(figsize=(10,5))
top_skipped.plot(kind='bar', color="salmon")
plt.title("Top 10 Skipped Songs")
plt.ylabel("Skip Count")
plt.show()

artist_skip = df.groupby('artist')['skipped'].mean().sort_values()
plt.figure(figsize=(10,5))
artist_skip.plot(kind='bar', color="lightgreen")
plt.title("Skip Rate by Artist")
plt.ylabel("Skip Probability")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="tempo", hue="skipped", multiple="stack", palette="coolwarm")
plt.title("Tempo Distribution by Skip Behavior")
plt.xlabel("Tempo (BPM)")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="skipped", y="duration", data=df, palette="Set3")
plt.title("Song Duration vs Skip Behavior")
plt.xlabel("Skipped (1 = Yes, 0 = No)")
plt.ylabel("Duration (seconds)")
plt.show()


print("\n✅ Analysis Complete! Visualizations generated.")
