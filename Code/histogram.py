def histogram(filename):
  # initialize empty histogram
  histogram = {}
  # take filename and open as file
  with open(filename) as file:
    # split each word into an array.
    word_list = file.read().split()
    # loop through words
    for word in word_list:
      # increment if word exists
      if histogram.get(word):
        histogram[word] += 1
      else:
        # add new word count
        histogram[word] = 1

  return histogram


if __name__ == '__main__':
    histogram = histogram('histogram_text.txt')
    print(histogram)
