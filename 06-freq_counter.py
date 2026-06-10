inp_str = input("Enter input string to calculate frequency: ")

freq_counter = {}
for chr in inp_str:
    freq_counter[chr] = freq_counter.get(chr,0)+1

print(f"Frequencies: {freq_counter}")