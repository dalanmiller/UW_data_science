# Homework 1


## Part 1: Design MapReduce Algorithms

Based on what you learned in class, design a MapReduce algorithm for any 3 out of the following 6 tasks. The idea is to describe the basic roles of the Map function and Reduce function, not to fret about details. Be brief and convincing.

###Inverted index
Given a set of documents, an inverted index is a dataset with key = word and value = list of document ids. Assume you are given a dataset where key = document id and value = document text.

    def map(key, values):
        """

        """
        for v in values:
            emit(v, )


    def reducek():
        """

        """




###Relational join
i.e., SELECT * FROM Order, LineItem WHERE Order.order_id = LineItem.order_id (Hint: Treat the two tables Order and LineItem as one big concatenated bag of records.)

###Social Network
Consider a simple social network dataset, where key = person and value = some friend of that person. Describe a MapReduce algorithm to count he number of friends each person has.

def map(key, value):

def reduce():


###Social Network (harder)
Use the same dataset as the previous task. The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Describe a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships.

###Bioinformatics.
Consider a set of sequences where key = sequence id and value = a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA.... Describe an algorithm to trim the last 10 characters from each read, then remove any duplicates generated. (Hint: It's not all that different from the Social Network example.)

###Matrix Multiply.
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value.  Design a MapReduce algorithm to compute matrix multiplication.
