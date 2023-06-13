import sys
import timeit
import string
from collections import defaultdict

def histogram(filename):
  # initialize empty histogram
  histogram = {}
  # verify command line args.
    # take filename and open as file
  with open(filename) as file:
    # read file, remove puncuation, and convert to array
    word_list = file.read().translate(str.maketrans('', '', string.punctuation)).lower().split()

    # loop through words
    for word in word_list:
      # increment if word exists
      if histogram.get(word):
        histogram[word] += 1
      else:
        # add new word count
        histogram[word] = 1
  return histogram

def unique_words(histogram):
  # return the length of the dictionary
  return len(histogram)

def frequency(word, histogram):
  # find word in histogram, else return error statement.
  # if type(histogram) is list:
  #   for entry in histogram:
  #     if entry[0] == word:
  #       return entry[1]
  # return f'Inputted word "{word}" was not found in histogram.'
  freq_dict = defaultdict(int)
  freq_dict.update(histogram)
  return freq_dict.get(word, 0)



if __name__ == '__main__':
  total_time = 0
  iterations = 10

  # timeit takes callable func as arg, lambda is anon one line function.
  for i in range(iterations):
    elapsed_time = timeit.timeit(lambda: histogram("michael_scott.txt"), number=1)
    total_time += elapsed_time
  # avg_time = total_time / iterations

  print(f'Total run time: {total_time}.\n')

  histogram = histogram("michael_scott.txt")

  unique_count = unique_words(histogram)
  print(f'Unique Words: {unique_count}')

  frequency_count = frequency("ever", histogram)
  print(f'Frequency: {frequency_count}')
