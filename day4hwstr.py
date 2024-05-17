# Question 1 Task 1

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
uppercase_reviews= []
review_words = ["good", "bad", "excellent", "poor", "average"]
for sentence in python_reviews:
    for word in review_words:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
    uppercase_reviews.append(sentence)
    
print(uppercase_reviews)

# Question 1 Task 2 

def pos_and_neg_count(python_reviews, positive_words, negative_words):
    total_pos_count = 0
    total_neg_count = 0
    for review in python_reviews:
        positive_count = 0
        negative_count = 0
        review_lower = review.lower()
        review_lower = review_lower.replace(".", "")
        words= review_lower.split()
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count +=1
        total_pos_count += positive_count
        total_neg_count += negative_count
    return total_pos_count, total_neg_count

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

positive_count, negative_count = pos_and_neg_count(python_reviews, positive_words, negative_words)
print("Total positive words: ", positive_count)
print("Total Negative Words: ", negative_count)

#Task 3

def summary(review):
    if len(review) <= 30:
        return review
    find_index = review[:30].rfind(" ")
    if find_index == -1:
        return review[:30] + "..."
    return review [:find_index] + "..."


#  Question 2 

def name_length(first_name, last_name):
    if len(first_name) <2 or len(last_name) <2:
        print("Both first and last name should have at least 2 characters")

first_name= input("First name: ")
last_name= input("Last name: ")
name_length(first_name, last_name)

