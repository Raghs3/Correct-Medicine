from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction  # union
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction  # union_update

meds_to_watch.update(*adverse_interactions)  # unpacking list

# print(sorted(meds_to_watch))
# print(*sorted(meds_to_watch), sep="\n")  # unpacking list, sorted produces list
