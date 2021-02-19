import timeit
def prime_num(num) : 
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    
    else:
        return False

# d is the number of characters in the input alphabet (the radix to use)
# q represents A prime number 

def rabin_karp_matcher(text, pattern,d, q): 
	m = len(pattern) ## length of the pattern we are looking for
	n = len(text) ## length of the given text

	p = 0 # hash value for pattern 
	t = 0 # hash value for the window m of text 
	h = 1

	positions = []

	# The value of h would be "pow(d, m-1)%q" but it may take too long if m is large so here is how its computed manually
	for i in range(m-1): 
		h = (h*d)%q 

	# preprocessing : Calculate the hash value of both the pattern and the first window of size m from the text
	for i in range(m): 
		p = (d*p + ord(pattern[i]))%q 
		t = (d*t + ord(text[i]))%q 

	# travel the text window by window, with each window being of size m, so there is no need to go to the last char, the (n-m)th char is our limit
	for i in range(n-m+1): 
		# if the hashed values match, then check the letters one by one
		if p==t: 
			for j in range(m): 
				if text[i+j] != pattern[j]: 
					break
				else: j+=1

			# if hashed values match and the window contains the same text as the pattern then print the found index
			if j==m: 
				positions.append(i)
				print("Pattern Occurs with shift " + str(i)) 

		# Calculate the hash value for the next window of text (under the condition that we didn't reach our limiter yet): Remove leading digit, add trailing digit 
		if i < n-m: 
			t = (d*(t-ord(text[i])*h) + ord(text[i+m]))%q 

			# We might get negative values of t, converting it to 
			# positive 
			if t < 0: 
				t = t+q
	return positions