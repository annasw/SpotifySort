# quicksort to sort my spotify playlist of the 50 best against me songs so that i don't need to think about it and can just do 1v1 comparisons
# this is going to take a long time
# ...

# it SHOULD work even if i fuck up the order in my mind (i.e. if i fuck up the consistency of e.g. A>B, B>C ergo A>C) bc quicksort.

# my tastes are immaculate and if you disagree with them you're an idiot.

# okay obviously just like make a list of your 50-however many favorite songs (or whatever i guess and read it in
# or you can just do it with this exact list of against me! songs, which obviously you should
# i strongly recommend that for each pairing you go listen to both songs in their entirety
# this would have taken me... roughly... 927 minutes (which is what like 15 hours)
songs = [
"I Still Love You Julie Against Me!",
"What We Worked For Against Me!",
"Burn Against Me!",
"Jordan's First Choice Against Me!",
"Those Anarcho Punks Are Mysterious Against Me!",
"Reinventing Axl Rose Against Me!",
"We Did It All for Don Against Me!",
"Pints of Guinness Make You Strong Against Me!",
"Untitled Bonus Track Against Me!",
"We Laugh at Danger (And Break All the Rules) Against Me!",
"Baby, I'm an Anarchist! Against Me!",
"Walking is Still Honest Against Me!",
"Sink, Florida, Sink Against Me!",
"Cavalier Eternal Against Me!",
"Miami Against Me!",
"Pretty Girls (The Mover) Against Me!",
"Up the Cuts Against Me!",
"Thrash Unreal Against Me!",
"White People for Peace Against Me!",
"Stop! Against Me!",
"Borne on the FM Waves of the Heart Against Me!",
"The Ocean Against Me!",
"White Crosses Against Me!",
"I Was a Teenage Anarchist Against Me!",
"Because of the Shame Against Me!",
"Suffocation Against Me!",
"We're Breaking Up Against Me!",
"High Pressure Low Against Me!",
"Ache With Me Against Me!",
"Spanish Moss Against Me!",
"Rapid Decompression Against Me!",
"Bamboo Bones Against Me!",
"Bitter Divisions Against Me!",
"Transgender Dysphoria Blues Against Me!",
"True Trans Soul Rebel Against Me!",
"Unconditional Love Against Me!",
"Drinking With the Jocks Against Me!",
"Osama Bin Laden As the Crucified Christ Against Me!",
"Fuckmylife666 Against Me!",
"Dead Friend Against Me!",
"Paralytic States Against Me!",
"Black Me Out Against Me!",
"Pints of Guinness Make You Strong - Live Against Me!",
"New Wave - Live Against Me!",
"Walking Is Still Honest - Live Against Me!",
"Delicate, Petite & Other Things I'll Never Be Against Me!",
"Haunting, Haunted, Haunts Against Me!",
"Rebecca Against Me!",
"Norse Truth Against Me!",
"People Who Died Against Me!"]

songs = [i[:-12] for i in songs] # i don't need " Against Me!" tagged on to the end of every song

# takes the names of two songs
# returns a comparison of which of said songs is better
# returns False if y better than x, True if x better than y.
# someday computers will do this for us
# until then it is my bad programs
def isBetter(x,y):
	while True:
		print("Is " + x + " better than " + y + "? 1/True or 0/False.")
		result = input("> ")
		if result == "1" or result == "0":
			return result # this is best practice fuck you

# quicksort
# comp = comparison algorithm (as opposed to the traditional <, >)
# i have no idea why the resulting ordered list is in the right order...... # UPDATE: yes i do. fixed.
# this isn't the most efficient implementation but i'm pretty sure the limiting factor is going to be me, not the algorithm... lol
def qs(ls, comp = isBetter):
	if len(ls) <= 1: return ls
	pivot = ls.pop()
	lsA = [i for i in ls if comp(i,pivot) == "0"]
	lsB = [i for i in ls if i not in lsA]
	return qs(lsA) + [pivot] + qs(lsB)

sortedList = qs(songs)[::-1] # yeah i def could have made the list reversal not necessary in the qs method... but fuck it.

f = open("am.txt","w")
for i in sortedList:
	f.write(i)
	f.write("\n")
f.close()

# RESULTS:
#
# worked fine
# sorted my 50-song list in 288 steps (which idk how to measure how efficient one specifc sort was from the # of steps,
# but it seems FAIRLY low to me, given qs is O(nlogn) and esp choosing pivots nonrandomly)
#
# IDEAS FOR IMPROVEMENT:
# - use Elo system to approximate ratings (and update with greater certainty),
# 	so one inaccurate comparison (e.g. Norse Truth > What We Worked For) doesn't permanently fuck up your list
# - pick a pivot randomly (less necessary if you think the great songs are pretty well distributed; more necessary for me)
#	(i realize no one cares but of my final top 20, fully 9 were released on or before AM!'s 1st studio album)
#	(although if we remove live songs (which, aside from new wave on 23LSA, we should), that goes down to... 8)
# - save constantly / in between picks, so you don't have to do all x00 steps consecutively
# - sort spotify playlist based on song rankings (no clue how you'd do this)
# - 
