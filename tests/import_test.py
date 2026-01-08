from rivalite import about
print(about())
import rivalite
print(rivalite.ensure_list(None))
print(rivalite.ensure_list("This should be in []."))
print(rivalite.ensure_list(("Tuple", 8, "a pie!")))
print("End of test")
