from histogram import histogram
import sys
import random

# random word based on uniform distribution
def random_word(histogram):
  # convert histogram keys to list and grab random key
  random_word = random.choice(list(histogram.keys()))
  return random_word

import timeit

# random word based on weight distribution
def weighted_word(histogram):
  # convert keys to list
  keys = list(histogram.keys())
  # convert values to list
  values = list(histogram.values())
  # return random word based on weights
  random_word = random.choices(keys, values)[0]

  return random_word

if __name__ == '__main__':
  # create histogram and initialize stats counter
  count = {}
  histogram = histogram(sys.argv)

  # evaluate run time
  total_time = 0
  iterations = 10000

  for i in range(iterations):
    elapsed_time = timeit.timeit(lambda: weighted_word(histogram), number=1)
    total_time += elapsed_time

  print(f'Total run time: {total_time}.\n')




  def counter(word):
    if count.get(word):
      count[word] += 1
    else:
      count[word] = 1

  # determine weighted probability stats
  for i in range(1000):
    # grab weighted word selection
    word = weighted_word(histogram)
    # add word to stats counter
    counter(word)
  print(f'Weighted Stats:\n{count}')



