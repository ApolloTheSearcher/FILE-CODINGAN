music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset({'pop', 'electronic', 'relaxing', 'slow', 'synth'})

# Union ( result should be a frozenset )
frozen_tag_union = my_tags.union(music_tags) 
# Intersection( normal set )
regular_tag_intersect = music_tags & my_tags
# Difference( result should be a frozenset )
frozen_tag_difference = my_tags - music_tags
# Symmetric Difference ( normal set )
regular_tag_sd = music_tags.symmetric_difference(my_tags)

# Print all
print(frozen_tag_union)
print(regular_tag_intersect)
print(frozen_tag_difference)
print(regular_tag_sd)
