# string s tab characterom
sample_text = "This is a\ttest."

# tabsize
large_tabsize = 1000000000

# použitie expandtabs
try:
    modified_text = sample_text.expandtabs(large_tabsize)
    print("Modified text:", modified_text)
except OverflowError as e:
    print("An error occurred:", e)
