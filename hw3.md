Daniel Miller
dalan.miller@gmail.com

# Assignment 3

## Part 1: Design MapReduce Algorithms

Based on what you learned in class, design a MapReduce algorithm for any 3 out of the following 6 tasks. The idea is to describe the basic roles of the Map function and Reduce function, not to fret about details. Be brief and convincing.

###Inverted index
Given a set of documents, an inverted index is a dataset with key = word and value = list of document ids. Assume you are given a dataset where key = document id and value = document text.

    def map(items):

	#Iterate through the items

	#Split up document text (value) of each item into separate words

	#Reverse the dictionary create a set of the words (if frequency != important)
	# as keys and a set of document ids as values since it's likely words will appear in multiple documents

	emit(word, array_of_doc_ids)

    def reduce(item):

	master = {}

	#Aggregate the dictionaries

	#For each item, add each value in set to master dictionary object, if possible?

	emit(master)

	#Or emit each tuple of ('word', aggregated_set_of_ids(1,2,3,4))


Map:

Input Key: Document ID
Input Value: Document Text
Output Key: Word
Output Value: Array of Doc IDs

Reduce:

Input Key: Word
Input Value: Array of Doc IDs
Output Key: Word
Output Value: Aggregated array of Doc IDs


###Social Network
Consider a simple social network dataset, where key = person and value = some friend of that person. Describe a MapReduce algorithm to count the number of friends each person has.

def map(items):

	#For each item, increment friend count of each person found (also if friend relationships
	# in this social network are mutual, increment friend count for the value person as well?
	# Also this assumes that for each incoming pair of (person, friend) that there are no duplicates.

	emit(person, count)


def reduce(items):

	#For each person key in items, sum values

	emit(person, total)

Map:

Input Key: Person
Input Value: Friend of Person
Output Key: Person
Output Value: Sum of found friends of person

Reduce:

Input Key: Person
Input Value: Sum of found friends of person
Output Key: Person
Output Value: Sums of found friends of person



###Bioinformatics.
Consider a set of sequences where key = sequence id and value = a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA.... Describe an algorithm to trim the last 10 characters from each read, then remove any duplicates generated. (Hint: It's not all that different from the Social Network example.)

def map(items):
	master = set()

	#For each item, take the nucleotide string and slice last ten characters

	master.add(sliced_nucleotides) #Not sure if this structure is available, but handles duplicates

	emit(master)

def reduce(items):

	master = set()
	#Ensure that each new result batch from map is aggregated into a larger set, further
	# ensuring that there are no duplicates from other map results.

	emit(master0)

Map:

Input Key: Sequence ID
Input Value: String of Nucleotides
Output Key: //Not necessary?
Output Value: nucleotide_string[-10:]

Reduce:

Input Key: // None
Input Value: nucleotide_string
Output Key: // None
Output Value: Set of aggregated strings


#Question 2.1

bin/hadoop dfs -put /path/to/file.txt

#Question 2.2

Standalone mode allows for easier debugging as it is just a single process and allows greater oversight
over each thing that is happening in the runtime process.

Pseudo-Distribution allows for an entire hadoop "system" to run in separate Java processes yet only on
a single host machine. This allows one to test at a slightly larger scale than Standalone mode or perhaps
do operations on smaller datasets when a full hadoop cluster is not necessary.

#Question 3.1

Applications that might benefit from increased Task Instance Groups are ones that require more computational
power on the map side or the amount of time taken per map process is way more significant in relation to the
set of operations done on the reduce side. Since they can't store data, they would be used for speeding up
the bulk of the operations.

Another theory is that one would use the Task Instance groups as a way of testing the load of a job, since it
doesn't persist, it would be one way to see with distributed resources on a job performs.

As to why the default is 0, it's probably unlikely that in too many applications that you wouldn't also want them to be able to store data so you would instead increase the number of core
instance groups.

#Question 3.2

16 minutes!
