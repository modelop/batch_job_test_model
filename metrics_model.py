# modelop.score
def score(endpoint_input):
    print("Score Called")
    print(str("st_val: " +endpoint_input["st_val"]))
    print(str("end_val: " + endpoint_input["end_val"]))
    print("Score thread returned")
    yield int(endpoint_input["end_val"]) - int(endpoint_input["st_val"])
