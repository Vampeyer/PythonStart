def frequency(s):
        '''Displays a frequency analysis of chars in string s.'''
        letter_freq = {}
        other_counter = 0
        for ch in s.lower():
            if ch.isalpha(): # Is ch a letter?
                if ch not in letter_freq: # First time? Start counter at 1
                    letter_freq[ch] = 1
                else:letter_freq[ch] += 1 # Already present, so add 1 to counter 
            else:other_counter += 1 # Not a letter, so add 1 to other counter
               
     
        print('Letter Frequency')
        print('------ ---------')
     
        for ch in sorted(letter_freq.keys()):
            print(f'{ch:^6} {letter_freq[ch]:4d}')
        print(f'other  {other_counter:4d}')
input_str = input('Enter string to analyze:\n')
#Enter string to analyze:
#ABCcba123def

frequency(input_str)

'''
Letter Frequency
------ ---------
  a       2
  b       2
  c       2
  d       1
  e       1
  f       1
  '''