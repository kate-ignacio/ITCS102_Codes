
#hobby
#name
#desc

SpongeBob = "SpongeBob SquarePants is a cartoon about a sea sponge who lives in a pineapple under the sea."
cartoon = ["Mickey Mouse", "Donald Duck", SpongeBob]
disney = ["Minnie Mouse", "Goofy", cartoon, "Daisy Duck"]
classic = ["Tom and Jerry", "Looney Tunes", disney, "Popeye"]
cartoon_type = {"old_school": classic, "new": "Adventure Time", "korean": "Larva"}

print(cartoon_type["old_school"][2][2])
