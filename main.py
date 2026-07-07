from graph.workflow import graph

destination = input("Enter destination: ")

result = graph.invoke({
    "destination": destination
})

print("\n======================")
print("Final Travel Plan")
print("======================\n")

print(result["final"])