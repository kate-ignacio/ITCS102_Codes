movie_genre = ["romance", "horror"," action","comedy","drama"]
movie_title = []

while True:
    ans = input("Do you know any movie --> (Yes/NO)")
    if ans.lower() == "Yes":
        print("what is its genre --> ? select from the list")
        for x in movie_genre:
            print(x)
        movie_genre = input("movie_type --> ")

        title = input("what is the title of the movie? --> ")
        movie_title.append(title)
        continue
    else:
        print("Thank you")
        break 
    for x in movie_title:
     print(x)