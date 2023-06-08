import sys
import timeit
import string

def histogram(args):
  # initialize empty histogram
  histogram = {}
  # verify command line args.
  if len(args) == 2:
    filename = args[1]
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
  else:
    raise Exception("Please input valid filename as command line argument.")



def unique_words(histogram):
  # return the length of the dictionary
  if type(histogram) is dict:
    return len(histogram)
  return

def frequency(word, histogram):
  # find word in histogram, else return error statement.
  if type(histogram) is dict:
    return histogram.get(word, f'Inputted word "{word}" not found in histogram.')
  return



if __name__ == '__main__':
  total_time = 0
  iterations = 10000

  # timeit takes callable func as arg, lambda is anon one line function.
  for i in range(iterations):
    elapsed_time = timeit.timeit(lambda: histogram(sys.argv), number=1)
    total_time += elapsed_time
  # avg_time = total_time / iterations

  print(f'Total run time: {total_time}.\n')

  histogram = histogram(sys.argv)

  unique_count = unique_words(histogram)
  print(f'Unique Words: {unique_count}')

  frequency_count = frequency("ever", histogram)
  print(f'Frequency: {frequency_count}')
